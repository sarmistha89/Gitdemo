import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.checkout import checkout
from POM.confirmation import confirmation

class Testoperationone(BaseClass):
    
    def test_e2e(self):
        logger=self.logging()
        homepage=HomePage(self.driver)        
        checkoutpage=homepage.shopitems()
        products=checkoutpage.shoppingcart()
        
        for product in products:            
            productname=product.find_element_by_xpath("div/h4[@class='card-title']/a").text
            logger.info(productname)
            if productname == "Blackberry":            
                product.find_element_by_xpath("div/button").click()
                
        checkoutpage.firstcheckout()
        cartname=checkoutpage.cartnameVerify() #self.driver.find_element_by_xpath("//a[contains(text(),'Blackberry')]").text
        print(cartname)

        assert cartname == "Blackberry"

        Confirmationpage=checkoutpage.finalCheckout()
        Confirmationpage.getcountry("Ind")
        self.visibilityoftext("India")
        Confirmationpage.selectcheckbox()
        Confirmationpage.submit()
        alertmessage= Confirmationpage.asserttext() 
        print(alertmessage)

        assert "Success" in alertmessage
        self.driver.get_screenshot_as_file("screen.png")
        
        print("changed by gitusa")
    


