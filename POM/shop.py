
class shop():
    
    def __init__(self, driver):
        self.driver = driver
        
    def shopitems(self):
        self.driver.find_element_by_link_text("Shop").click()