"""断言的公共方法"""


def assert_common(self, rep, status_code=200, msg="操作成功！"):
    """
     断言的公共方法
    :param self:  unittest.TestCode实例对象
    :param rep:   response 接口的响应对象
    :param status_code: 响应状态码--默认200
    :param msg:响应消息----默认操作成功
    :return:无
    """

    # 断言状态码---默认200
    self.assertEqual(status_code, rep.status_code)
    # 断言success
    self.assertTrue(rep.json().get("success"))
    # 断言code
    self.assertEqual(10000, rep.json().get("code"))
    # 断言msg --默认操作成功
    self.assertEqual(msg, rep.json().get("message"))
