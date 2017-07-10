__author__ = 'Bach'

import time


from macaca import WebDriverException
from Public.BasePage import BasePage
from Public.Decorator import teststep
from Public.Decorator import teststeps
from Public.ConfigParser import getConfig


class PocketWalletHomePage(BasePage):
    @teststep
    def handle_alert(self):

        if self.driver.element_if_exists('id', 'com.android.packageinstaller:id/permission_allow_button'):
            self.driver.element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
            time.sleep(1)
            self.handle_alert()
        else:
            pass

    @teststep
    def wait_page(self, timeout=10000):
        """以“信用付”的xpath为标志"""
        try:
            self.driver \
                .wait_for_element_by_id(getConfig('HomePage', 'xyf_id'), timeout=timeout)
            return True
        except WebDriverException:
            return False

    @teststep
    def login_status(self):
        """获取登录状态"""
        self.driver \
            .element_by_id(getConfig('HomePage', 'available_money')).text
        # print(self.driver.element_by_id('cn.pocketwallet.pocketwallet:id/tv_current_available_money').text)

    @teststep
    def click_usr_account(self):
        """以“注册、认证钱包”的id为标志"""
        self.driver \
            .element_by_id(getConfig('HomePage', 'usr_center')).click()

    @teststep
    def click_msg_center(self):
        """以消息中心的id为标志"""
        self.driver \
            .element_by_id(getConfig('HomePage', 'msg_center')).click()

    @teststep
    def click_xyf(self):
        """以信用付的id为标志"""
        self.driver \
            .element_by_id(getConfig('HomePage', 'xyf_id')).click()

    @teststep
    def click_tx(self):
        """以提现的id为标志"""
        self.driver \
            .element_by_id(getConfig('HomePage', 'tx_id')).click()

    @teststep
    def click_te(self):
        """以提额的id为标志"""
        self.driver \
            .element_by_id(getConfig('HomePage', 'te_id')).click()

    @teststep
    def click_hk(self):
        """以还款的id为标志"""
        self.driver \
            .element_by_id(getConfig('HomePage', 'hk_id')).click()

    @teststeps
    def is_login(self):
        """判断是否登录"""
        loginstatus = self.login_status()
        if loginstatus == '尚未登录':
            return False
        else:
            return True

