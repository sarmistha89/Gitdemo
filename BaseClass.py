import pytest
import inspect
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

@pytest.mark.usefixtures("setup")
class BaseClass:
    
    
    def visibilityoftext(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, text))).click()
    
    def getgender(self, text):
        select=Select(self.driver.find_element_by_id('exampleFormControlSelect1'))
        select.select_by_visible_text(text)
        
    def logging(self):
        loggerName= inspect.stack()[1][3]
        logger=logging.getLogger(loggerName)

        fileHandler=logging.FileHandler('logfile.log')
        formatter=logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger