"""
@Filename:  commons/log_util
@Author:   lianpengwei
@Time:    2022/6/28 11:55
@Describe:  ...
"""
import logging.handlers
import os

import yaml


def info_log(message):
    LogUtil.get_logger().info(message)


def error_log(message):
    LogUtil.get_logger().error(message)
    raise AssertionError(message)


class LogUtil:

    logger = None

    @classmethod
    def get_path(cls):
        return os.path.dirname(__file__).split('commons')[0]

    @classmethod
    def read_log_config(cls, key, one_key='log'):
        filepath = cls.get_path() + 'config.yaml'
        with open(filepath, 'r', encoding='utf-8') as f:
            return yaml.load(f, yaml.FullLoader)[one_key][key]

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            cls.logger = logging.getLogger()

            log_level = cls.read_log_config('log_level')
            if log_level == 'debug':
                cls.logger.setLevel(logging.DEBUG)
            elif log_level == 'info':
                cls.logger.setLevel(logging.INFO)
            elif log_level == 'warning':
                cls.logger.setLevel(logging.WARNING)
            elif log_level == 'error':
                cls.logger.setLevel(logging.ERROR)
            elif log_level == 'critical':
                cls.logger.setLevel(logging.CRITICAL)
            else:
                print('设置的日志等级有误!!!')

            sh = logging.StreamHandler()
            filepath = cls.get_path() + 'logs' + os.sep + cls.read_log_config('log_filename')
            rh = logging.handlers.RotatingFileHandler(filepath, 'w', encoding='utf-8')

            fmt = logging.Formatter(cls.read_log_config('log_format'))

            sh.setFormatter(fmt)
            rh.setFormatter(fmt)

            cls.logger.addHandler(sh)
            cls.logger.addHandler(rh)
        return cls.logger


if __name__ == '__main__':

    info_log('this is a message')