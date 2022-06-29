"""
@Filename:  commons/assert_util
@Author:   lianpengwei
@Time:    2022/6/21 16:20
@Describe:  ...
"""
import traceback

import jsonpath

from commons.database_util import DatabaseUtil
from commons.log_util import info_log, error_log


# 断言
def assert_util(yq_result, sj_result, status_code):
    try:
        # print('yq_result: ', yq_result)
        # print('sj_result: ', sj_result)
        all_flag = 0
        if yq_result:
            for yq in yq_result:
                for key, value in yq.items():
                    if key == 'code':
                        # print('状态码断言')
                        flag = code_assert(value, status_code)
                        all_flag = all_flag + flag
                    elif key == 'equals':
                        # print('相等断言')
                        flag = equals_assert(value, sj_result)
                        all_flag = all_flag + flag
                    elif key == 'contains':
                        # print('包含断言')
                        flag = contains_assert(value, sj_result)
                        all_flag = all_flag + flag
                    elif key == 'db_equals':
                        # print('数据库断言')
                        flag = db_assert(value, sj_result)
                        all_flag = all_flag + flag
                    else:
                        info_log('框架不支持此种断言方式!')
        else:
            # print('没有断言!')
            all_flag = -1
        # 判断断言结果
        if all_flag == 0:
            info_log('结果断言成功')
        elif all_flag == -1:
            info_log('没有断言!')
        else:
            error_log('结果断言失败!')
    except Exception:
        error_log(f'断言报错: {traceback.format_exc()}')


# 状态码断言
def code_assert(value, status_code):
    flag = 0
    for assert_key, assert_value in value.items():
        if assert_key == 'status_code':
            if assert_value != status_code:
                flag = flag + 1
                error_log(f'状态码断言失败: {assert_value}不等于{assert_value}')
    return flag


# 相等断言
def equals_assert(value, sj_result):
    flag = 0
    for assert_key, assert_value in value.items():
        lists = jsonpath.jsonpath(sj_result, f'$..{assert_key}')
        if lists:
            if assert_value != lists[0]:
                flag = flag + 1
                error_log(f'相等断言失败: {assert_key}不等于{assert_value}!')
        else:
            flag = flag + 1
            error_log(f'相等断言失败: 返回的结果中没有{assert_key}!')
    return flag


# 包含断言
def contains_assert(value, sj_result):
    flag = 0
    if str(value) not in str(sj_result):
        flag = flag + 1
        error_log(f'包含断言失败: 返回的结果中没有{value}')
    return flag


# 数据库断言
def db_assert(value, sj_result):
    flag = 0
    for sql, key in value.items():
        lists = jsonpath.jsonpath(sj_result, f'$..{key}')
        # print('lists: ', lists)
        if lists:
            res = None
            try:
                res = DatabaseUtil.get_sql_one(sql)
                # print('res: ', res)
            except Exception:
                flag = flag + 1
                error_log(f'数据库断言失败: sql查询异常或语法有误{traceback.format_exc()}')
                break
            if res is None:
                flag = flag + 1
                error_log(f'数据库断言失败: 查询没有结果返回!')
            else:
                if res[0] == lists[0]:
                    info_log('数据库断言成功')
                else:
                    flag = flag + 1
                    error_log(f'数据库断言失败: sql查询结果不等于实际结果!')
        else:
            flag = flag + 1
            error_log(f'数据库断言失败: 返回结果中不包含{key}')
    return flag
