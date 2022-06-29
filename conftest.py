"""
@Filename:  /conftest
@Author:   lianpengwei
@Time:    2022/6/20 15:42
@Describe:  ...
"""
import pytest

from commons.log_util import LogUtil
from commons.yaml_util import clear_yaml


@pytest.fixture(scope='session', autouse=True)
def clear_extract():
    clear_yaml()


res = LogUtil.get_path()
print(res)