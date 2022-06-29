"""
@Filename:  commons/yaml_util
@Author:   lianpengwei
@Time:    2022/6/20 14:20
@Describe:  ...
"""
import os

import yaml


# 获取路径
def get_path():
    return os.getcwd().split('commons')[0]


# 读取extract.yaml数据
def read_yaml(key, filename='extract.yaml'):
    filepath = get_path() + os.sep + filename
    with open(filepath, 'r', encoding='utf-8') as f:
        return yaml.load(f, yaml.FullLoader)[key]


# 写入extract.yaml数据
def write_yaml(data, filename='extract.yaml'):
    filepath = get_path() + os.sep + filename
    with open(filepath, 'a', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True)


# 清空extract.yaml数据
def clear_yaml(filename='extract.yaml'):
    filepath = get_path() + os.sep + filename
    with open(filepath, 'w', encoding='utf-8') as f:
        f.truncate()


if __name__ == '__main__':
    data = {'name': 18}
    write_yaml(data)
    res = read_yaml('name')
    print(res)