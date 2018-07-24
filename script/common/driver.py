import os

from appium import webdriver

server_url = 'http://127.0.0.1:4723/wd/hub'

config = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'platformVersion': '6.0',
    'app': os.path.abspath('app-debug.apk'),
    'appWaitActivity': 'idv.haojun.calculatorrecorder.activity.LoginActivity',
}

def get_driver():
	return webdriver.Remote(server_url, config)
