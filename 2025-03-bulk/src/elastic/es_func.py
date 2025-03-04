"""
Copyright (c) SIOS Technology, Inc. All rights reserved.

MIT License
"""

from typing import Iterable

from elastic.es_consts import SEARCH_INDEX
from elasticsearch import Elasticsearch, helpers


def create_es_client(elasticsearch_endpoint:str, api_key_encoded:str) -> Elasticsearch:
  """
  Elasticsearch へアクセスするための client を生成する。
  """
  es_client: Elasticsearch = None
  if elasticsearch_endpoint != '' and api_key_encoded != '':
    es_client = Elasticsearch(hosts=elasticsearch_endpoint, api_key=api_key_encoded)
  return es_client


def streaming_bulk_wrapper(es_client:Elasticsearch, actions:Iterable) -> int:
  """
  bulk を使って、データを投入する。
  (streaming_bulk を使用する)

  return 投入したドキュメント数
  
  see https://elasticsearch-py.readthedocs.io/en/latest/helpers.html
  """
  success_count: int = 0
  for response in helpers.streaming_bulk(client=es_client, actions=actions):
    if response[0]:
      success_count += 1

  return success_count


def refresh_index(es_client:Elasticsearch, index_name:str=SEARCH_INDEX):
  """
  bulk 後などに、refresh を呼び出す。
  """
  es_client.indices.refresh(index=index_name)
