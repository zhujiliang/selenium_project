# coding:utf-8
from selenium import webdriver
import unittest
import time
from common.login import logintest


class SystemManagement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.result = logintest(cls.driver)  # 只登陆一次
        cls.driver.get("http://47.98.18.190:58888/uc")
        time.sleep(5)

    def test_SystemManagement_01(self):
        u'''boss2系统管测试'''
        self.driver.find_elements_by_class_name("el-input__inner")[0].send_keys(18616959404)
        self.driver.find_element_by_class_name("el-button").click()
        # 获取表格里面的手机号
        sel = self.driver.find_elements_by_class_name("el-table_1_column_2")[1]
        print(sel.text)
        self.driver.find_element_by_class_name("el-button--default").click()
        print(u"赠金充值测试")
        time.sleep(2)
        self.driver.find_elements_by_class_name("el-menu-item")[2].click()
        print(u"赠金充值设置测试")
        time.sleep(2)
        self.driver.find_elements_by_class_name("el-menu-item")[3].click()
        self.driver.find_elements_by_class_name("el-input__inner")[0].send_keys("18616959404")
        self.driver.find_element_by_class_name("el-button--primary").click()
        self.driver.find_element_by_class_name("el-button--default").click()
        print(u"赠金充值记录测试")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.quit()


if __name__ == __name__:
    unittest.main()
