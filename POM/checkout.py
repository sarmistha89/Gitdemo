from selenium.webdriver.common.by import By
from POM.confirmation import confirmation
class checkout:
    
    def __init__(self,driver):
        self.driver = driver
        
    cartList=(By.XPATH,"//div[@class='card h-100']")
    productsname=(By.XPATH, "div/h4[@class='card-title']/a")
    cartname=(By.XPATH, "//a[contains(text(),'Blackberry')]")

        
    def shoppingcart(self):
        return self.driver.find_elements(*checkout.cartList)
    
    def productName(self):
        return self.product.find_element(*checkout.productsname).text
    
    def cartnameVerify(self):
        return self.driver.find_element(*checkout.cartname).text
    
    def firstcheckout(self):
        self.driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
    
    def finalCheckout(self):
        self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        Confirmationpage=confirmation(self.driver)
        return Confirmationpage
        

        