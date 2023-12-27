from utilities.readProperties import ReadConfig


class Test_url:
    def test_url_1(self,setup):
        self.driver = setup

        baseurl = ReadConfig.getApplicationURL()

        print(baseurl)

        self.driver.get(baseurl)

