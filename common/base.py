# coding:utf-8
# base 底层的封装，对selenium的二次封装
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchFrameException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoAlertPresentException


class Base():
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        self.poll = 0.5

    def findElement(self, loctor):
        '''args:
        loctor 传元祖 ，如（"id", "xx"）'''
        element = WebDriverWait(self.driver, self.timeout, self.poll).until(lambda x: x.find_element(*loctor))
        return element

    def findElements(self, loctor):
        '''args:
        loctor 传元祖 ， 如（"id", "xx"）'''
        elements = WebDriverWait(self.driver, self.timeout, self.poll).until(lambda x: x.find_element(*loctor))
        return elements

    def findElementNew(self, loctor):
        '''找到了返回element， 没找到抛异常'''
        element = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.presence_of_element_located(loctor))
        return element

    def findElementsNew(self, loctor):
        '''找到了返回elements， 没有找到抛出异常'''
        elements = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.presence_of_all_elements_located(loctor))
        return elements

    def sendKeys(self, loctor, text):
        '''输入文本'''
        ele = self.findElement(loctor)
        ele.sendkeys(text)

    def click(self, loctor):
        '''点击按钮'''
        ele = self.findElement(loctor)
        ele.click()

    def clear(self, loctor):
        '''清除'''
        ele = self.findElement(loctor)
        ele.clear()

    def moveToElement(self, loctor):
        '''鼠标悬停事件'''
        mos = self.findElement(loctor)
        ActionChains(driver).move_to_element(mos).perform()

    def is_text_in_element(self, locator, text):
        '''判断给定的text在这个元素的文本上
        要么返回true,要么返回false,不要让它抛异常了
        '''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.text_to_be_present_in_element(locator, text))
            return result
        except:
            return False


if __name__ == "__main__":
    driver = webdriver.Firefox()
    base = Base(driver)
    driver.get("http://www.t.xqcx.com/uc")
