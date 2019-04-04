#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import sys
import os
import time

# 参数1：钉钉机器人的webhook地址
# 参数2：群组里面需要强提醒的成员绑定钉钉的手机号，格式有要求；
# [138xxxxxxx,156xxxxxxx]
# 参数3：markdown的消息体
# 参数4：存放日志的文件路径，可使用默认

headers = {'Content-Type': 'application/json;charset=utf-8'}
time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def log(log_file, info):
    #需要注意日志路径的权限
    if os.path.isfile(log_file) == False:
               f = open(log_file, 'a+')

    f = open(log_file,'a+')
    f.write(info)
    f.close()

def msg(api_url, user, text, log_file = "/var/log/zabbix_dingtalk.log" ):
    # 将获取到的user 字符串转换成list，然后追加每个电话到markdown文本后面
    user_list = user[1:-1].split(",")
    for i in user_list:
        text = text + "\n\n@" + i
    print text

    json_text= {
     "msgtype": "markdown",
        "markdown": {
            "title":"zabbix monitor",
            "text": text
        },
        "at": {
            "isAtAll": "false",
            "atMobiles": user
        }
    }

    r=requests.post(api_url,data=json.dumps(json_text),headers=headers).json()
    code = r["errcode"]
    if code == 0:
        log(log_file, time + ":消息发送成功 返回码:" + str(code) + "\n")
    else:
        log(log_file, time + ":消息发送失败 返回码:" + str(code) + "\n")
        exit(3)

if __name__ == '__main__':
    api_url = sys.argv[1]
    user    = sys.argv[2]
    text    = sys.argv[3]
    log_file= sys.argv[4]
    if log_file == "":
        log_file = "/var/log/zabbix_dingtalk.log"
    msg(api_url, user, text, log_file)
