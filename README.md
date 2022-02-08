# 接口测试自动化

基于 pytest 开发完成，可以实现批量执行

## 依赖

Python 3.6+

requests

pytest

## 执行命令

```sh
python3 test_suite.py
```

## 使用说明

1. 同一模块，所有的测试用例写在 `test_suite.py` 文件内
2. 通用请求方法写在 `requester.py` 文件内
3. 自定义请求头配置在 `request_header.json` 文件内
4. 自定义断言写在 `assert_utils.py` 文件内
5. 每一个测试用例所需要调用的接口方法封装在 `api_wrapper.py` 文件内，`test_suite.py` 文件内不涉及具体接口调用
6. 接口地址配置在 `test_const.py` 文件内
7. 测试数据写在 `test_data.py` 文件内

