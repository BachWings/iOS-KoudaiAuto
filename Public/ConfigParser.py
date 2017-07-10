__author__ = 'Bach'
__time__ = '2017/5/19'

import configparser
import os

path = os.getcwd()

def getConfig(section, key):
    config = configparser.ConfigParser()
    config.read('../PageObject/PwProperties.ini', encoding="utf-8")
    return config.get(section, key)

