__author__ = 'Bach'
__time__ = '2017/5/31'

import time
from macaca import WebDriverException

from Public.BasePage import BasePage
from Public.Decorator import teststep
from Public.Decorator import teststeps
from Public.ConfigParser import getConfig

class MyPage(BasePage):
    @teststep
    def wait_page(self, timeout = 10000):
        """以设置按钮的ID为依据"""
        try:
            self.driver \
                .wait_element_by_id(getConfig('MyPage', 'setting'), timeout=timeout)
            return True
        except WebDriverException:
            return False

    @teststep
    def login_status(self):
        """获取登录状态根据登录注册按钮状态"""
        self.driver \
            .element_by_id(getConfig('MyPage', 'login_status')).text()

    @teststep
    def click_setting(self):
        """点击设置按钮"""
        self.driver \
            .element_by_id(getConfig('MyPage', 'setting')).click()

    @teststep
    def click_login(self):
        """点击登录注册按钮"""
        self.driver \
            .element_by_id(getConfig('MyPage', 'login_status')).click()

    @teststep
    def click_repayment(self):
        """点击去还款"""
        self.driver \
            .element_by_id(getConfig('MyPage', 'repayment')).click()

    @teststep
    def click_withdraw(self):
        """点击取现按钮"""
        self.driver \
            .element_by_id(getConfig('MyPage', 'withdraw')).click()

    @teststep
    def click_installment(self):
        """点击我的分期"""
        self.driver \
            .element_by_id(getConfig('MyPage', 'installment')).click()

    @teststep
    def click_fund_manege(self):
        """点击资金管理"""
        self.driver \
            .element_by_id(getConfig('MyPage', 'fund_manage')).click()

    @teststep
    def click_order(self):
        """点击我的订单"""
        self.driver \
            .element_by_id(getConfig('MyPage', 'my_order')).click()

    @teststep
    def click_certification(self):
        """点击信用认证"""
        self.driver \
            .element_by_id(getConfig('MyPage', 'certification')).click()

    @teststep
    def click_coupon(self):
        """点击优惠券"""
        self.driver \
            .element_by_id(getConfig('MyPage', 'coupon')).click()

    @teststep
    def click_invite(self):
        """点击有奖邀请"""
        self.driver \
            .element_by_id(getConfig('MyPage', 'invite')).click()

    @teststep
    def click_help(self):
        """点击帮助中心"""
        self.driver \
            .element_by_id(getConfig('MyPage', 'help')).click()

    @teststep
    def go_to_homepage(self):
        """回到首页"""
        self.driver \
            .element_by_id(getConfig('MyPage', 'home_page')).click()

    @teststep
    def go_to_mall(self):
        """打开商城"""
        self.driver \
            .element_by_id(getConfig('MyPage', 'mall_page')).click()

    @teststeps
    def is_login(self):
        """检测登录状态"""
        loginstatus = self.login_status()
        if loginstatus == '点击登录/注册':
            return False
        else:
            return True
