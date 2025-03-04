"""
Copyright (c) SIOS Technology, Inc. All rights reserved.

MIT License
"""

import logging

# ディフォルトのログレベルを設定
DEFAULT_LOG_LEVEL = 'INFO'
# DEFAULT_LOG_LEVEL = 'DEBUG'

# ログのフォーマットを設定
DEFAULT_LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s:%(lineno)d %(funcName)s %(message)s"


def setup_logger(log_level:str=DEFAULT_LOG_LEVEL):
  """
  ログの基本設定を行う
  """
  logging.basicConfig(
    level=log_level,
    format=DEFAULT_LOG_FORMAT,
    datefmt="[%X]"
  )
