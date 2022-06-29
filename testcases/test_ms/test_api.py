"""
@Filename:  testcases/test_api
@Author:   lianpengwei
@Time:    2022/6/20 14:30
@Describe:  ...
"""
import pytest
import requests

from commons.ddt_util import read_testcase_yaml
from commons.request_util import RequestUitl


class TestApi:

    # # 1.获取鉴权码access token接口
    # @pytest.mark.parametrize('caseinfo', read_testcase_yaml('./testcases/test_ms/get_token.yaml'))
    # def test_get_token(self, caseinfo):
    #     RequestUitl().standard_yaml_testcase(caseinfo)
    #
    # # 2.获取公众号已创建的标签接口
    # @pytest.mark.parametrize('caseinfo', read_testcase_yaml('./testcases/test_ms/select_tags.yaml'))
    # def test_select_tags(self, caseinfo):
    #     RequestUitl().standard_yaml_testcase(caseinfo)
    #
    # # 3.创建标签接口
    # @pytest.mark.parametrize('caseinfo', read_testcase_yaml('./testcases/test_ms/create_tag.yaml'))
    # def test_create_tag(self, caseinfo):
    #     RequestUitl().standard_yaml_testcase(caseinfo)
    #
    # # 4.编辑标签接口
    # @pytest.mark.parametrize('caseinfo', read_testcase_yaml('./testcases/test_ms/edit_tag.yaml'))
    # def test_edit_tag(self, caseinfo):
    #     RequestUitl().standard_yaml_testcase(caseinfo)
    #
    # # 5.删除标签接口
    # @pytest.mark.parametrize('caseinfo', read_testcase_yaml('./testcases/test_ms/del_tag.yaml'))
    # def test_del_tag(self, caseinfo):
    #     RequestUitl().standard_yaml_testcase(caseinfo)
    #
    # # 6.文件上传接口
    # @pytest.mark.parametrize('caseinfo', read_testcase_yaml('./testcases/test_ms/file_upload.yaml'))
    # def test_file_upload(self, caseinfo):
    #     RequestUitl().standard_yaml_testcase(caseinfo)

    # 7.自定义MD5加密接口
    @pytest.mark.parametrize('caseinfo', read_testcase_yaml('./testcases/test_ms/md5_case.yaml'))
    def test_md5_case(self, caseinfo):
        RequestUitl().standard_yaml_testcase(caseinfo)

    # 9.sign签名接口
    @pytest.mark.parametrize('caseinfo', read_testcase_yaml('./testcases/test_ms/sign_case.yaml'))
    def test_sign_case(self, caseinfo):
        RequestUitl().standard_yaml_testcase(caseinfo)