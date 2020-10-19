# -*- coding: utf-8 -*-
import sys
import uuid
import requests
import base64
import hashlib
import json
from imp import reload

reload(sys)

YOUDAO_URL = 'https://openapi.youdao.com/ocrtransapi'
APP_KEY = '您的应用ID'
APP_SECRET = '您的应用密钥'

def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def encrypt(signStr):
    hash_algorithm = hashlib.md5()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)


def connect(file_content):
    f = open(file_content, 'rb')  # 二进制方式打开图文件
    q = base64.b64encode(f.read()).decode('utf-8')  # 读取文件内容，转换为base64编码
    f.close()

    data = {}
    # data['from'] = '源语言'
    # data['to'] = '目标语言'
    data['from'] = 'auto'
    data['to'] = 'auto'
    data['type'] = '1'
    data['q'] = q
    salt = str(uuid.uuid1())
    signStr = APP_KEY + q + salt + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['salt'] = salt
    data['sign'] = sign

    response = do_request(data)
    result=json.loads(str(response.content, encoding="utf-8"))
    print(result)

    translateResults=result['resRegions']
    print(translateResults)
    pictransresult=""
    for i in translateResults:
        pictransresult=pictransresult+i['tranContent']+"\n"
    return pictransresult

