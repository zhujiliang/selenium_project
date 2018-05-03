# coding:utf-8
from selenium import webdriver
import unittest
import time
from page.login_page import LoginPage


class XiangQiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.result = LoginPage(cls.driver)  # 只登陆一次
        cls.driver.get("http://47.98.18.190:58888/uc")
        time.sleep(5)

    def test_login_01(self):
        u'''uc登陆测试'''
        self.assertTrue(self.result == "朱继亮")

    @classmethod
    def tearDownClass(cls):
        cls.quit()


if __name__ == "__name__":
    unittest.main()
