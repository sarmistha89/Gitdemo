import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from POM.login import login
from BaseClass import BaseClass
from Homepagedata import Homepagedata
@pytest.mark.usefixture("setup")
class Testlogin(BaseClass):
    
    def test_login(self, getdata):
        Homepage=login(self.driver)
        Homepage.getname(getdata["firstname"])
        Homepage.getemail(getdata["email"])
        Homepage.getpassword(getdata["password"])
        Homepage.selectcheckbox()

        checktext=Homepage.checkboxtext().text
        log=self.logging()
        log.info(checktext)
        assert "Check me out" in checktext

        self.getgender(getdata["Gender"])
        Homepage.selectradiobutton()
        Homepage.getdate(getdata["DOB"])

        Homepage.submit()

        successmsg=Homepage.submitconfirmmsg().text
        log.info(successmsg)
        assert "Success!" in successmsg
        self.driver.refresh()
        
    @pytest.fixture(params=Homepagedata.testdata)
    def getdata(self, request):
        return request.param
    def getdata(self, request):
        return request.param
    def getdata(self, request):
        return request.param
            

        