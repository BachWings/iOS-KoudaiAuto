import time
from macaca import WebDriverException

from Public.BasePage import BasePage
from Public.Decorator import teststep
from Public.Decorator import teststeps

# from App.PageObject.GesturePasswordPage import GesturePasswordPage
# from Public.LoginStatus import LoginStatus
from PocketWallet.PageObject.PocketWalletHomePage import PocketWalletHomePage
from PocketWallet.TestData.Account import VALID_ACCOUNT
from Public.ConfigParser import getConfig


class LoginPage(BasePage):
    @teststep
    def wait_page_pwd(self, timeout=10000):
        """以登录页面的“登录”Button的ID为依据"""
        try:
            self.driver\
                .wait_for_element_by_id(getConfig('LoginPage', 'enter_pwd'), timeout=timeout) \
                and self.driver.element_by_id(getConfig('LoginPage', 'enter_pwd')).text == "登录"
            return True
        except WebDriverException:
            return False

    @teststep
    def wait_page_verification(self, timeout=10000):
        """以登录页面的“登录”Button的ID为依据"""
        try:
            self.driver\
                .wait_for_element_by_id(getConfig('LoginPage', 'enter_pwd'), timeout=timeout) \
                and self.driver.element_by_id(getConfig('LoginPage', 'enter_pwd')).text == "登录\注册"
            return True
        except WebDriverException:
            return False

    @teststep
    def verification(self):
        """点击验证码登录tab"""
        self.driver\
            .element_by_id(getConfig('LoginPage', 'verification_login_tab'))\
            .click()


    @teststep
    def close(self):
        self.driver\
            .element_by_id(getConfig('LoginPage', 'close'))\
            .click()

    @teststep
    def input_account(self, account):
        """以“请输入手机号码”的id为依据"""
        self.driver\
            .element_by_id(getConfig('LoginPage', 'enter_account'))\
            .clear()\
            .send_keys(account)

    @teststep
    def input_password(self, pwd):
        """以“请输入登录密码或者验证码”的id为依据"""
        self.driver\
            .element_by_id(getConfig('LoginPage', 'enter_pwd'))\
            .clear()\
            .send_keys(pwd)

    @teststep
    def input_verification(self, ver):
        """输入验证码"""
        self.driver\
            .element_by_id(getConfig('LoginPage', 'enter_pwd'))\
            .clear()\
            .send_keys(ver)

    @teststep
    def login(self):
        """以“登录”Button的id为依据"""
        self.driver\
            .element_by_id(getConfig('LoginPage', 'login_btn'))\
            .click()

    '''@teststep
    def switch_webview(self):
        """切换到webview，操作H5"""
        contexts = self.driver.contexts
        self.driver.context = contexts[-1]

    @teststep
    def switch_native(self):
        """切换到native"""
        contexts = self.driver.contexts
        self.driver.context = contexts[0]'''

    @teststeps
    def new_valid_login_pwd(self):
        """用给定的account与password进行登录"""
        login = LoginPage()
        login.wait_page_pwd()
        login.input_account(VALID_ACCOUNT.account())
        login.input_password(VALID_ACCOUNT.password())
        login.login()
        time.sleep(1)

    @teststeps
    def new_valid_login_verification(self):
        """用验证码登录"""
        login = LoginPage()
        login.verification()
        login.wait_page_verification()
        login.input_account(VALID_ACCOUNT.account())
        login.input_verification(VALID_ACCOUNT.verification())
        login.login()
        time.sleep(1)





