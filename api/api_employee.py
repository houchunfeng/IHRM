"""员工管理"""
import requests

import api


class ApiEmployee():
    def __init__(self):
        # 添加员工
        self.url_insert = api.BASE_URL + "/api/sys/user"
        # 员工 删、更新、查询
        self.url_DUF = api.BASE_URL + "/api/sys/user/{}"

    def insert_employee(self, username, mobile, workNumber):
        """添加员工"""
        data = {
            "username": username,
            "mobile": mobile,
            "workNumber": workNumber,
        }
        return requests.post(url=self.url_insert, json=data, headers=api.HEADERS)

    def delete_employee(self):
        """删除员工"""
        return requests.delete(url=self.url_DUF.format(api.USER_ID), headers=api.HEADERS)

    def update_employee(self, user_id):
        """更新员工"""
        return requests.put(url=self.url_DUF.format(user_id), headers=api.HEADERS)

    def select_employee(self):
        """查询员工"""
        pass
