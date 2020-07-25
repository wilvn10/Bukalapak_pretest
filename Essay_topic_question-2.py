# This is the code for question number 2
# all of the identity data were retrieved from identity.py file

from selenium import webdriver
from time import sleep
from identity import fullName, email, gender, userName, pw
class webTest:
    def __init__(self, url, fullName, email, gender, userName, pw):
        self.driver = webdriver.Chrome()
        self.url = url
        self.fullName = fullName
        self.email = email
        self.gender = gender
        self.username = userName
        self.pw = pw
        self.driver.get(url)
        sleep(1)

    def register(self):
        
        # click "Register"
        self.driver.find_element_by_xpath("/html/body/div[1]/div/section/header/div[3]/div/div/div[2]/div/a[1]/p")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@id='user_name']").send_keys(self.fullName)
        self.driver.find_element_by_xpath("//input[@id='email_or_phone']").send_keys(self.email)
        self.driver.find_element_by_id("user_username").clear()
        self.driver.find_element_by_xpath("//input[@id='user_username']").send_keys(self.userName)
        self.driver.find_element_by_xpath("//input[@id='user_password']").send_keys(self.pw)
        self.driver.find_element_by_xpath("//input[@id='user_password_confirmation']").send_keys(self.pw)
        if gender == 'man':
            self.driver.find_element_by_xpath("/html/body/main/div[2]/div/form/div[3]/label[1]/span")\
                .click()
        elif gender == 'woman':
            self.driver.find_element_by_xpath("/html/body/main/div[2]/div/form/div[3]/label[2]/span")\
                .click()
        else:
            print('enter a valid gender')
            self.driver.quit()
            return
        sleep(1)
        # element = self.driver.find_element_by_class_name("c-fld__error").text
        testEmail = self.driver.find_element_by_xpath("/html/body/main/div[2]/div/form/div[2]/div/div[3]").text
        testUsername = self.driver.find_element_by_xpath("/html/body/main/div[2]/div/form/div[4]/div/div[4]").text
        # test email and username availability
        if not testEmail == '':
            print('Enter your valid e-mail or phone')
            # uncomment the code below to close the windows when something is wrong
            # self.driver.quit()
            return
        if not testUsername == '':
            print('This username is not available')
            # uncomment the code below to close the windows when something is wrong
            # self.driver.quit()
            return
        sleep(1)
        # click terms and condition
        self.driver.find_element_by_xpath("//*[@id='new_user']/div[8]/label/span")\
            .click()
        sleep(1)
        # self.driver.find_element_by_xpath("//button[@name='commit']").click()

    def login(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div/section/header/div[3]/div/div/div[2]/div/a[2]/p")\
            .click()
        sleep(1)
        self.driver.find_element_by_xpath("//input[@id='user_session_username']").send_keys(self.email)
        self.driver.find_element_by_xpath("//input[@id='user_session_password']").send_keys(self.pw)
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div/form/button/i').click()
        
    def searchProduct(self, productName):
        sleep(4)
        self.driver.find_element_by_xpath("//input[@id='v-omnisearch__input']").send_keys(productName)
        self.driver.find_element_by_xpath("//button[@title='Cari']").click()

if __name__ == '__main__':
    test = webTest("https://bukalapak.com", fullName, email, gender, userName, pw)
    # uncomment the code below to showcase the register process
    # test.register()

    # code below shows the login process
    test.login()

    # then it search for a product
    test.searchProduct('Sepeda Jokowi')
