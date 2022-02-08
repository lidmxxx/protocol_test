#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ====#====#====#====
# Author: lidemin
# CreateDate:
# LastUpdate:
# Description: 测试用例集
# Version:0.1.0
# ====#====#====#====
import pytest

from api_wrapper import ApiWrapper as call_api
import test_data
import assert_utils as asserter


class TestAPI:
    # ===============================login_mobile===============================
    @pytest.mark.parametrize("region, account, password", test_data.test_login_mobile)
    def test_login_mobile(self, region, account, password):
        res = call_api().do_login_mobile_android(region, account, password)
        asserter.assert_equal(res['success'], True)


if __name__ == '__main__':
    pytest.main(['test_suite.py', '--html=./report/report.html'])
