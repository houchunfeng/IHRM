import unittest

from parameterized import parameterized

import api

from api.api_employee import ApiEmployee
from tools.assert_common import assert_common
from tools.read_json import read_login


class TestEmployee(unittest.TestCase):
    """测试方法---员工管理"""

    @classmethod
    def setUpClass(cls):
        """初始化"""
        cls.employee = ApiEmployee()

    @parameterized.expand(read_login("employee.json"))
    def test01_insert_employee(self, username, mobile, workNumber):
        """测试添加员工"""
        rep = self.employee.insert_employee(username, mobile, workNumber)
        print("insert_employee",rep.json())
        print(rep.status_code)

        # 提取用户的id
        api.USER_ID = rep.json().get("data").get("id")
        # 断言
        assert_common(self, rep)

    def test02_delete_employee(self):
        """测试删除员工"""
        rep = self.employee.delete_employee()
        print("delete_employee",rep.json())
        # 断言
        assert_common(self, rep)
