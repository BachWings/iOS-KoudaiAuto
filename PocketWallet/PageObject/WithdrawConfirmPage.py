__author__ = 'Bach'
__time__ = '2017/6/14'

import time


from macaca import WebDriverException
from Public.BasePage import BasePage
from Public.Decorator import teststep
from Public.Decorator import teststeps
from Public.ConfigParser import getConfig
from PocketWallet.TestData.Account import VALID_ACCOUNT


class WithdrawConfirmPage(BasePage):
    @teststep
    def wait_page(self, timeout=10000):
        """根据页头提现确认"""
        try:
            self.driver \
                .wait_for_element_by_name(getConfig('WithdrawConfirmPage', 'withdraw_confirm'), timeout=timeout)
            return True
        except WebDriverException:
            return False
    @teststep
    def switch_webview(self):
        """切换到webview，操作H5"""
        contexts = self.driver.contexts
        for i in contexts:
            print(i)
        self.driver.context = contexts[-1]

    @teststep
    def switch_native(self):
        """切换到native"""
        contexts = self.driver.contexts
        self.driver.context = contexts[0]

    @teststep
    def input_sum(self):
        """输入金额"""
        self.driver \
            .element_by_xpath(getConfig('WithdrawConfirmPage', 'value')) \
            .clear() \
            .send_keys('600')

    @teststep
    def no_installment(self):
        """不分期"""
        self.driver \
            .element_by_xpath(getConfig('WithdrawConfirmPage', 'no_intallment')) \
            .click()

    @teststep
    def six_installments(self):
        """分六期"""
        self.driver \
            .element_by_xpath(getConfig('WithdrawConfirmPage', 'six_installments')) \
            .click()

    @teststep
    def twelve_installments(self):
        """十二期"""
        self.driver \
            .element_by_xpath(getConfig('WithdrawConfirmPage', 'twelve_insallments')) \
            .click()

    @teststep
    def click_submit(self):
        """点击提交"""
        self.driver \
            .element_by_xpath(getConfig('WithdrawConfirmPage', 'submit')) \
            .click()

    @teststep
    def is_withdraw(self, timeout=10000):
        """检测借款是否成功"""
        print()
        try:
            self.driver \
                .wait_for_element_by_xpath(getConfig('WithdrawConfirmPage', 'complete'), timeout=timeout)
            return True
        except WebDriverException:
            return False

    @teststep
    def input_password(self, pwd):
        """输入支付密码"""
        self.driver \
            .element_by_xpath(getConfig('WithdrawConfirmPage', 'password')) \
            .clear() \
            .send_keys(pwd)

    @teststep
    def click_confirm(self):
        """点击确认"""
        self.driver \
            .element_by_xpath(getConfig('WithdrawConfirmPage', 'confirm')) \
            .click()

    @teststeps
    def withdraw(self):
        """提现操作"""
        withdrawconfirm = WithdrawConfirmPage()
        withdrawconfirm.switch_webview()
        withdrawconfirm.input_sum()
        withdrawconfirm.click_submit()
        withdrawconfirm.input_password(VALID_ACCOUNT.pay_password())
        withdrawconfirm.click_confirm()

