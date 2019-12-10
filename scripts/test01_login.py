import unittest

from parameterized import parameterized

import api
from api.api_login import ApiLogin
from tools.assert_common import assert_common
from tools.read_json import read_login


class TestLogin(unittest.TestCase):
    """测试方法---登录"""

    @classmethod
    def setUpClass(cls):
        """初始化"""
        cls.login = ApiLogin()

    @parameterized.expand(read_login("login.json"))
    def test01_login(self, mobile, password):
        """测试方法"""
        rep = self.login.api_login(mobile, password)
        print(rep.json())
        print(rep.status_code)
        # 提取token
        token = rep.json().get("data")
        api.HEADERS['Authorization'] = 'Bearer ' + token
        print('登录后的headers的值', api.HEADERS)
        # 断言
        assert_common(self, rep)
