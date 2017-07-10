import random


# data base of valid account
# we can add a or multiple valid account in it, like this '{'account': 'xxxxxxxxxxx', 'password': 'yyyyyyyy'},'
_VALID_ACCOUNT = (
    {'account': '13914747011', 'password': '123qwe', 'ver': '1234', 'pay_password': 'qwe123'},
)


class Account:
    def __init__(self):
        self.valid_account = _VALID_ACCOUNT[random.randint(0, len(_VALID_ACCOUNT)) - 1]

    def account(self):
        return self.valid_account['account']

    def password(self):
        return self.valid_account['password']

    def verification(self):
        return self.valid_account['ver']

    def pay_password(self):
        return self.valid_account['pay_password']


# global variable
# a instance of valid account
# it can be used in any place via 'from CarInsurance.TestData.Account import VALID_ACCOUNT'
VALID_ACCOUNT = Account()
