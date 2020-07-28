from POM.checkout import checkout

class HomePage:
    
    def __init__(self,driver):
        self.driver = driver
    
    def shopitems(self):
        self.driver.find_element_by_link_text("Shop").click()
        checkoutpage=checkout(self.driver)
        return checkoutpage