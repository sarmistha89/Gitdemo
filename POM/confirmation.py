from selenium.webdriver.common.by import By
class confirmation:
    
    def __init__(self, driver):
        self.driver = driver
        
    confirmtext= (By.CLASS_NAME, "alert-success")
        
    def getcountry(self, country_name):
        self.driver.find_element_by_xpath("//input[@id='country']").send_keys(country_name)
        
    def selectcheckbox(self):
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        
    def submit(self):
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        
    def asserttext(self):
        return self.driver.find_element(*confirmation.confirmtext).text
        
        