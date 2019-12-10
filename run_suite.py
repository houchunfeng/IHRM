# coding:utf-8
import unittest

from tools.HTMLTestReportCN import HTMLTestRunner

suits = unittest.defaultTestLoader.discover("./scripts")
# 打印到html的报告中
with open("./report/report.html", "wb")as f:
    HTMLTestRunner(stream=f).run(suits)

# 直接讲错误信息打印在console中
unittest.TextTestRunner().run(suits)