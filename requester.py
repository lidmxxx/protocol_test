#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ====#====#====#====
# Author: lidemin
# CreateDate:
# LastUpdate:
# Description: 通用请求方法
# Version:0.1.0
# ====#====#====#====
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


class Requester:
    @staticmethod
    def post_request(url, headers, data):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=url, headers=headers, data=data, verify=False)
        return response.json()
