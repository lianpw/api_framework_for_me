"""
@Filename:  hotloads/debug_talk
@Author:   lianpengwei
@Time:    2022/6/21 10:50
@Describe:  ...
"""
import hashlib
import os
import random
import time

import yaml


class DebugTalk:

    def get_path(self):
        return os.path.dirname(__file__).split('hotloads')[0]

    def read_extract(self, key, filename='extract.yaml'):
        filepath = self.get_path() + os.sep + filename
        with open(filepath, 'r', encoding='utf-8') as f:
            return yaml.load(f, yaml.FullLoader)[key]

    def get_random(self, min, max):
        return random.randint(int(min), int(max))

    # 获取基础路径
    def get_base_url(self, key, base='base_url'):
        filepath = self.get_path() + os.sep + 'config.yaml'
        with open(filepath, 'r', encoding='utf-8') as f:
            return yaml.load(f, yaml.FullLoader)[base][key]

    # md5加密
    def md5(self, args):
        # 以指定的编码格式编码字符串
        utf8_str = str(args).encode('utf-8')
        # md5加密
        md5_str = hashlib.md5(utf8_str).hexdigest()
        return md5_str

    # sign签名
    def signs(self, yaml_path):
        # print('yaml_path: ', yaml_path)
        all_args_dict = {}
        with open(os.path.dirname(__file__).split('hotloads')[0] + yaml_path, 'r', encoding='utf-8') as f:
            yaml_content = yaml.load(f, yaml.FullLoader)
            # print('yaml_content: ', yaml_content)
            for caseinfo in yaml_content:
                caseinfo_keys = caseinfo.keys()
                if 'request' in caseinfo_keys:
                    request_value = caseinfo['request']
                    print('request_value: ', request_value)
                    if 'url' in request_value.keys():
                        url = request_value['url']
                        print('url: ', url)
                        # url_args = url.split('?')[1]
                        url_args = url[url.index("?") + 1:]
                        print(url_args)
                        args_list = url_args.split('&')
                        print(args_list)
                        for args in args_list:
                            all_args_dict[args[0:args.index('=')]] = args[args.index('=')+1:]
                        print(all_args_dict)
                        # 判断params, data是否在request的key里面
                        for key, value in request_value.items():
                            if key in ["params","data"]:
                                for args_key, args_value in value.items():
                                    all_args_dict[args_key] = args_value
                        print(all_args_dict)
                        from commons.request_util import RequestUitl
                        all_args_dict = RequestUitl().replace_get_value(all_args_dict)
                        print(all_args_dict)
                        all_args_dict = dict_asic_sort(all_args_dict)
                        print(all_args_dict)
        # 第二步
        new_str = ''
        for key, value in all_args_dict.items():
            new_str = new_str + str(key) + '=' + str(value) + '&'
        new_str = new_str[0:-1]
        print(new_str)
        # 第3-5步
        appid = "www"
        appsecret = "ccc"
        nonce = str(random.randint(1000000000, 9999999999))
        timestamp = str(time.time())
        new_str = 'appid=' + appid + '&' + 'appsecret=' + appsecret + '&' + new_str + '&' + 'nonce=' + nonce + '&' + 'timestamp=' + timestamp
        print(new_str)
        # 第六步
        sign = self.md5(new_str).upper()
        print(sign)
        return sign



# 把字典的key按照asic码升序排序
def dict_asic_sort(all_args_dict):
    keys = all_args_dict.keys()
    # print(keys)
    l = list(keys)
    l.sort()
    new_dict = {}
    for i in l:
        new_dict[i] = all_args_dict[i]
    return new_dict


if __name__ == '__main__':
    DebugTalk().signs('testcases/test_ms/sign_case.yaml')