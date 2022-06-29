"""
@Filename:  commons/ddt_util
@Author:   lianpengwei
@Time:    2022/6/27 14:46
@Describe:  ...
"""
import json
import traceback

import yaml


# 读取测试用例yaml数据
from commons.log_util import error_log


def read_testcase_yaml(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            caseinfo = yaml.load(f, yaml.FullLoader)
            if len(caseinfo) >= 2:
                return caseinfo
            else:
                if 'parameterize' in dict(*caseinfo).keys():
                    new_caseinfo = parameterize_ddt(*caseinfo)
                    return new_caseinfo
                else:
                    return caseinfo
    except Exception:
        error_log(f'读取测试用例yaml数据报错: {traceback.format_exc()}')


# 解析parameterize数据驱动
def parameterize_ddt(caseinfo):
    try:
        # print('caseinfo:', caseinfo)
        caseinfo_str = json.dumps(caseinfo)
        data_list = caseinfo['parameterize']
        length = True
        for param in data_list:
            if len(param) != len(data_list[0]):
                length = False
                error_log(f'该条数据不符合长度要求: {param}')
                continue
        # 替换值
        new_caseinfo = []
        if length:
            for i in range(1, len(data_list)):
                # print('len(data_list):', len(data_list))
                row_caseinfo = caseinfo_str
                for j in range(len(data_list[i])):
                    # print('len(data_list[i])', len(data_list[i]))
                    if isinstance(data_list[i][j], int) or isinstance(data_list[i][j], float):
                        row_caseinfo = row_caseinfo.replace('"$ddt{' + data_list[0][j] + '}"', str(data_list[i][j]))
                    else:
                        row_caseinfo = row_caseinfo.replace('$ddt{' + data_list[0][j] + '}', str(data_list[i][j]))
                new_caseinfo.append(json.loads(row_caseinfo))
        return new_caseinfo
    except Exception:
        error_log(f'数据驱动ddt报错: {traceback.format_exc()}')


if __name__ == '__main__':
    res = read_testcase_yaml('../testcases/test_ms/get_token.yaml')
    print(res)