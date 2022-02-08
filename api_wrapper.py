#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ====#====#====#====
# Author: lidemin
# CreateDate:
# LastUpdate:
# Description: 封装测试用例所需调用的接口
# Version:0.1.0
# ====#====#====#====
from requester import Requester
import json
import os

import test_const


with open(os.path.dirname(__file__) + '/request_header.json', mode='r') as f:
    header_data = json.loads(f.read())


class ApiWrapper:
    def __init__(self):
        self.requester = Requester

    # ===============================login_mobile===============================
    def do_login_mobile_android(self, region, account, password):
        global header_data
        headers = header_data['header_logout']
        params = {
            'region': region,
            'account': account,
            'password': password
        }
        url = test_const.host + test_const.do_login
        response = self.requester.post_request(url=url, headers=headers, data=params)
        return response
