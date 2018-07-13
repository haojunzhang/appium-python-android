# -*- coding: utf-8 -*-

from appium import webdriver

def appium_start():
	config = {
        'platformName': 'Android',
        'deviceName': 'emulator-5554',
        'platformVersion': '6.0',
        'app': 'C:\\app-debug.apk',
        'unicodeKeyboard': True,
        'resetKeyboard': True
    }
	return webdriver.Remote('http://127.0.0.1:4723/wd/hub', config) 