import unittest
from appium import webdriver
from time import sleep

class appiumAPK(unittest.TestCase):
    def __init__(self):
        self.desiredCaps = {}
        self.desiredCaps['app'] = "c:\\Sample Android App Login Test_v4.0_apkpure.com"
        self.desiredCaps['appPackage'] = "com.loginmodule.learning"
        self.desiredCaps['appActivity'] = "com.loginmodule.learning.activites.LoginActivity"
        self.desiredCaps['deviceName'] = '1e5234ae'
        self.desiredCaps['platformName'] = 'Android'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub",self.desiredCaps)
    def register(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw
        self.driver.find_element_by_id('com.loginmodule.learning:id/textViewLinkRegister').click()
        sleep(1)
        self.driver.find_element_by_id('com.loginmodule.learning:id/textInputEditTextName').send_keys(self.name)
        self.driver.find_element_by_id('com.loginmodule.learning:id/textInputEditTextEmail').send_keys(self.email)
        self.driver.find_element_by_id('com.loginmodule.learning:id/textInputEditTextPassword').send_keys(self.pw)
        self.driver.find_element_by_id('com.loginmodule.learning:id/textInputEditTextConfirmPassword').send_keys(self.pw)
        self.driver.find_element_by_id('com.loginmodule.learning:id/appCompatButtonRegister').click()
        sleep(1)
        nameCheck = self.driver.find_element_by_class_name('android.widget.TextView').text
        if not nameCheck == '':
            print('negative check, fill in the correct information')
        else:
            print('positive check, all information are filled correctly')

if __name__ == '__main__':
    name = 'test'
    email = 'test@tes.com'
    pw = 'test123'
    appiumAPK.register(name, email, pw)

