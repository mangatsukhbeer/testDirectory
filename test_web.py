import pytest

@pytest.mark.usefixtures("setupDriver")
class TestOne:

    def test_loadWebsite(self):

        self.driver.get('https://www.google.ca')
        assert self.driver.title == "Google"
        print(self.driver.title)
