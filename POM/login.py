from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class login():
    
    fullname=(By.NAME, "name")
    checkbox=(By.CSS_SELECTOR,"[class*='form-check']>label[for*='exampleCheck1']")
    confirmmsg=(By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    
    def __init__(self,driver):
        self.driver=driver
    
    def getname(self, text):
        self.driver.find_element(*login.fullname).send_keys(text)
    
    def getemail(self, text):
        self.driver.find_element_by_xpath("//input[@name='email']").send_keys("nayaksarmistha@gmail.com")
        
    def getpassword(self, text):
        self.driver.find_element_by_id("exampleInputPassword1").send_keys("P@ssword")
        
    def selectcheckbox(self):
        self.driver.find_element_by_xpath("//input[@id='exampleCheck1']").click()
        
    def checkboxtext(self):
        return self.driver.find_element(*login.checkbox)
        
            
    def selectradiobutton(self):
        self.driver.find_element_by_id('inlineRadio1').click()
        
    def getdate(self, text):
        self.driver.find_element_by_xpath("//input[@name='bday']").send_keys(text)
        
    def submit(self):
        self.driver.find_element_by_xpath("//input[@value='Submit']").click()
        
    def submitconfirmmsg(self):
        return self.driver.find_element(*login.confirmmsg)