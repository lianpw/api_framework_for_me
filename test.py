"""
@Filename:  /test
@Author:   lianpengwei
@Time:    2022/6/20 16:46
@Describe:  ...
"""
import os
import re

# data = '{"access_token":"58_hkaT4wa5todzW7pYcnp4UjZyabaXIfUq3t4f-rPNMNN20AESaycf-qHv1Cv1aSNRv6IK1Wol-PxLw5BKwgzBeRv_lEw0wESBzmaptf9Can2nBG37aMyz0TKB0Xs82kJx0uX-Ao6wlkZ73KKkSJTfAFANEO","expires_in":7200}'
# res = re.search('"access_token":"(.*?)",', data)
# # print(res)
# print(res.group(1))

# data = 'my name is lianpw'
# res = re.match('my (.*?) is lianpw', data)
# print(res)
# print(res.group())
# print(res.group(1))

# res = re.search('(.*) name', 'my ame')
# print(res)
# print(res.group(1))
# lists = ['10',  '20']
# def add(a, b):
#     print(a, b)
#
# add(*lists)

# path1 = os.getcwd()
# path2 = os.path.dirname(__file__)
# print(path1)
# print(path2)
# from hotloads.debug_talk import DebugTalk
#
# DebugTalk().test()

# str = '{"error_code":0,"message":"MD5\\u52a0\\u5bc6\\u767b\\u9646\\u6210\\u529f\\uff01"}'
# print(str.encode('utf-8').decode('unicode_escape'))
# str1 = "MD5\u52a0\u5bc6\u767b\u9646\u6210\u529f\uff01"
# print('str1', str1)

# s = '\\u82e6\\u6d77\\u65e0\\u6daf\\u56de\\u5934\\u662f\\u5cb8'
# print(s.encode("utf-8").decode("unicode_escape"))

# str = '\u4eac\u4e1c\u653e\u517b\u7684\u722c\u866b'
#
# print(eval('u"%s"' % str))
# print(f'u"{str}"')
import requests

url = 'http://101.34.221.219:5000/md5login'

header = {
            "User-Agent":"PostmanRuntime/7.26.3",
            "Content-Type":"charset=utf-8",
        }

data = {
    'username': '21232f297a57a5a743894a0e4a801fc3',
    'password': '202cb962ac59075b964b07152d234b70'
}

url2 = 'https://api.weixin.qq.com/cgi-bin/tags/get?access_token=58_Iw6OFVwbljbnc7Yg8e4ms8so2Dv5K4tjHYQiSG6C7SX62iwWmMsToP2wVq5ookjkyphL5rnXjwfgqgQO7kZxvWUvq51UE6yAi3JjhSql_SmB03C_VGHYYu469ZOfEi0C5TOiCioTGc2-SSWlGYSeADAMEY'

# res = requests.post(url, data=data)
# print(res.encoding)
# print(res.apparent_encoding)
# res.encoding = res.apparent_encoding
# print(res.text)
# print(res.content)
# print(res.content.decode("unicode_escape"))
# print(res.headers)

# print('-'*100)
# res2 = requests.get(url2)
# print(res2.text)
# print(res2.content)
# print(res2.content.decode("unicode_escape"))


f='\u4f18\u8863\u5e93\u4fc3\u9500'
# print(f)
print(f.decode('unicode-escape'))