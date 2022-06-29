"""
@Filename:  commons/request_util
@Author:   lianpengwei
@Time:    2022/6/20 16:10
@Describe:  ...
"""
import json
import re
import traceback

import jsonpath
import requests

from commons.assert_util import assert_util
from commons.log_util import error_log, info_log
from commons.yaml_util import write_yaml
from hotloads.debug_talk import DebugTalk


class RequestUitl:

    session = requests.session()
    url = None

    # 规范yaml测试用例
    def standard_yaml_testcase(self, caseinfo):
        try:
            info_log("----------接口测试开始----------")
            # print('caseinfo: ', caseinfo)
            caseinfo_keys = caseinfo.keys()
            if 'name' in caseinfo_keys and 'request' in caseinfo_keys and 'validate' in caseinfo_keys:
                info_log(f'接口名称：{caseinfo["name"]}')
                request_keys = caseinfo['request'].keys()
                if 'method' in request_keys and 'base_url' in request_keys and 'url' in request_keys:
                    method = caseinfo['request'].pop('method')
                    base_url = caseinfo['request'].pop('base_url')
                    url = caseinfo['request'].pop('url')
                    res = self.send_all_request(method, base_url, url, **caseinfo['request'])
                    text_result = res.text
                    # text_result = res.content.decode('unicode-escape')
                    print('text_result: ',text_result)
                    json_result = None
                    try:
                        json_result = res.json()
                    except Exception:
                        info_log('返回的结果不是json格式!')
                    if 'extract' in caseinfo_keys:
                        for key, value in caseinfo['extract'].items():
                            if '(.*?)' in value or '(.+?)' in value:
                                zz_value = re.search(value, text_result)
                                if zz_value:
                                    data = {key: zz_value.group(1)}
                                    write_yaml(data)
                                else:
                                    pass
                                    # print('extract提取中间变量, 正则写法有误或者接口返回有误!')
                            else:
                                js_value = jsonpath.jsonpath(json_result, value)
                                if js_value:
                                    data = {key: js_value[0]}
                                    write_yaml(data)
                                else:
                                    pass
                                    # print('extract提取中间变量, jsonpath写法有误或者接口返回有误!')
                    # 断言
                    yq_result = caseinfo['validate']
                    info_log(f'预期结果：{yq_result}')
                    sj_result = json_result
                    info_log(f'实际结果：{text_result}')
                    status_code = res.status_code
                    assert_util(yq_result, sj_result, status_code)
                    info_log('接口测试成功')
                    info_log('----------接口测试结束----------\n')
                else:
                    error_log('request下面必须包含有method,base_url,url这三个二级关键字')
            else:
                error_log('在YAML用例里面必须包含有一级关键字：name,request,validate')
        except Exception:
            error_log(f'规范yaml测试用例报错: {traceback.format_exc()}')

    # 统一请求封装
    def send_all_request(self, method, base_url, url, **kwargs):
        try:
            method = method.lower()
            info_log(f'请求方式：{method}')
            url = base_url + url
            RequestUitl.url = url
            url = self.replace_get_value(url)
            info_log(f'请求路径：{url}')
            for key, value in kwargs.items():
                if key in ['headers', 'params', 'data', 'json']:
                    kwargs[key] = self.replace_get_value(value)
                    info_log(f'请求{key}参数：{kwargs[key]}')
                elif key == 'files':
                    for file_key, file_value in value.items():
                        value[file_key] = open(file_value, 'rb')
            # print('kwargs: ', kwargs)
            return RequestUitl.session.request(method, url, **kwargs)
        except Exception:
            error_log(f'统一请求封装报错: {traceback.format_exc()}')

    # 热加载替换取值
    def replace_get_value(self, data):
        try:
            if data:
                data_type = type(data)
                if isinstance(data, dict) or isinstance(data, list):
                    str_data = json.dumps(data)
                else:
                    str_data = str(data)
                for i in range(str_data.count('${')):
                    start_index = str_data.index('${')
                    end_index = str_data.index('}', start_index)
                    old_value = str_data[start_index:end_index+1]
                    print('old_value: ', old_value)
                    function_name = old_value[2:old_value.index('(')]
                    # print('function_name: ', function_name)
                    args_value = old_value[old_value.index('(')+1: -2]
                    # print('args_value: ', args_value)
                    if args_value:
                        all_args_value = args_value.split(',')
                        new_value = getattr(DebugTalk(), function_name)(*all_args_value)
                    else:
                        new_value = getattr(DebugTalk(), function_name)()
                    print('new_value: ', new_value)
                    if isinstance(new_value, int) or isinstance(new_value, float):
                        if data != RequestUitl.url and function_name != 'get_random':
                            str_data = str_data.replace('"' + old_value + '"', str(new_value))
                        else:
                            str_data = str_data.replace(old_value, str(new_value))
                    else:
                        str_data = str_data.replace(old_value, str(new_value))
                if isinstance(data, dict) or isinstance(data, list):
                    data = json.loads(str_data)
                else:
                    data = data_type(str_data)
                # print('data: ', data)
                return data
            else:
                return data
        except Exception:
            error_log(f'热加载替换取值报错: {traceback.format_exc()}')


if __name__ == '__main__':
    data = 'https://api.weixin.qq.com?access_token=${read_extract(access_token)}'
    RequestUitl().replace_get_value(data)