from selenium.webdriver.common.by import By

desired_caps = {
    "deviceName": "iPhone 13",
    "platformName": "IOS",
    "version" : "12.0",
    "app": "https://sampeTest.com/appium/BookDoc.apk",
    "realDevice": true
}

    def test_textfields(self):
        self.driver.find_element(By.ID, "userEmail").send_keys("QATest@mail.com ")
        self.driver.find_element(By.ID, "password").send_keys("QATEST101")
        self.driver.find_element(By.ID, "firstName").send_keys("QATEST)
        self.driver.find_element(By.ID, "lastName").send_keys("TESTQA")
        self.driver.execute_script("arguments[0].click()",date1)
        self.driver.find_element(By.XPATH, "//*[@id='dateOfBirth']/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select/option[5]").click()
        self.driver.find_element(By.XPATH,"//*[@id='dateOfBirth']/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select/option[91]").click()
        self.driver.find_element(By.XPATH, "//*[@id='dateOfBirth']/div[2]/div[2]/div/div/div[2]/div[2]/div[4]/div[4]").click()
        time.sleep(5)
        
    def login_facebook(self):
        self.driver.find_elemeny(By.ID, "Facebook").click()