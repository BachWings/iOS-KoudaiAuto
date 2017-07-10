__author__ = 'Bach'
__time__ = '2017/6/9'

import time
from macaca import WebDriverException

from Public.BasePage import BasePage
from Public.Decorator import teststep
from Public.Decorator import teststeps
from Public.ConfigParser import getConfig

class MallPage(BasePage):
    @teststep
    def wait_page(self, timeout=10000):
        """以充值Button的xpath为依据"""
        try:
            self.driver\
                .wait_for_element_by_xpath(getConfig('MallPage', 'recharge'), timeout=timeout)
            return True
        except WebDriverException:
            return False

    @teststep
    def click_recharge(self):
        """点击充值按钮"""
        self.driver \
            .element_by_xpath(getConfig('MallPage', 'recharge')).click()

    @teststep
    def click_digital(self):
        """点击数码按钮"""
        self.driver \
            .element_by_xpath(getConfig('MallPage', 'digital')).click()

    @teststep
    def click_cosmetic(self):
        """点击美妆按钮"""
        self.driver \
            .element_by_xpath(getConfig('MallPage', 'cosmetic')).click()

    @teststep
    def click_electronics(self):
        """点击家电按钮"""
        self.driver \
            .element_by_xpath(getConfig('MallPage', 'electronics')).click()

    @teststep
    def click_mombaby(self):
        """点击母婴按钮"""
        self.driver \
            .element_by_xpath(getConfig('MallPage', 'mombaby')).click()
