"""
Copyright (c) SIOS Technology, Inc. All rights reserved.

MIT License

text を読み込んで、bulk により 文章と登録するツール

Usage: python bulk_from_txt.py chunked_textfilepath

登録先のindex名などは、es_consts.py に記載しておく。
"""

from io import TextIOWrapper
import os
import sys
import logging

from typing import Iterable
from dotenv import load_dotenv

from elasticsearch import Elasticsearch

from elastic.es_consts import INGEST_PIPELINE, SEARCH_INDEX
from elastic.es_func import create_es_client, refresh_index, streaming_bulk_wrapper

from common.setup_logger import setup_logger


def initialize_es() -> Elasticsearch:
    """
    Elasticsearchの初期化を行う。
    """
    load_dotenv(verbose=True)
    elasticsearch_endpoint = os.getenv('elasticsearch_endpoint')
    write_api_key_encoded = os.getenv('write_api_key_encoded')

    if not elasticsearch_endpoint or not write_api_key_encoded:
        logger.error('please set elasticsearch_endpoint and write_api_key_encoded in .env')
        return None

    es_client = create_es_client(elasticsearch_endpoint, write_api_key_encoded)
    logger.debug(f'{es_client.info()=}')
    return es_client


def data_generator(input_file: TextIOWrapper, index_name: str = SEARCH_INDEX, ingest_pipeline_name: str = INGEST_PIPELINE) -> Iterable:
    """
    ファイルを1行ずつ読み取り、ドキュメント登録可能な形式にして返す。
    """
    for chunk_no, content in enumerate(input_file):
        # 末尾の改行文字を削除する。
        line_content = content.rstrip('\r\n')

        # 1行ずつ処理する。
        yield {
            '_index': index_name,
            'pipeline': ingest_pipeline_name,
            '_source': {
                'chunk_no': chunk_no,
                'content': f"{line_content}"
            }
        }


def bulk_from_file(es_client: Elasticsearch, input_text_filename: str, index_name: str = SEARCH_INDEX, refresh: bool = False):
    """
    1つのtextファイルを1行ずつ読み込んで、elasticsearch にドキュメント登録する。
    """
    try:
        with open(file=input_text_filename, buffering=-1, encoding="utf-8") as input_file:
            success_count = streaming_bulk_wrapper(es_client=es_client, actions=data_generator(input_file))
            logger.info(f'{success_count=}')
            
            if refresh and success_count > 0:
                refresh_index(es_client, index_name=index_name)
    except Exception as e:
        logger.error(f'Error processing file {input_text_filename}: {e}')


# ----- main -----
if __name__ == "__main__":
    logger = setup_logger(__name__)

    es_client = initialize_es()

    if es_client is None:
        logger.error('Initialization failed.')
        sys.exit(1)

    if len(sys.argv) < 2:
        logger.error('Usage: python bulk_from_txt.py <chunked_textfilepath>')
        sys.exit(1)

    text_filepath: str = sys.argv[1]

    bulk_from_file(es_client=es_client, input_text_filename=text_filepath, index_name=SEARCH_INDEX, refresh=True)
