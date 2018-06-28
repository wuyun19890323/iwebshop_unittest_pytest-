from time import sleep
from selenium import webdriver
import unittest, time, sys


class Test_01(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost/iwebshop/")
        self.driver.maximize_window()
        sleep(2)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_link_text("登录").click()
        sleep(1)

    def tearDown(self):
        sleep(2)
        self.driver.find_element_by_link_text("安全退出").click()
        sleep(2)
        self.driver.quit()

    def test01(self):
        self.driver.find_element_by_css_selector("[type='text']").send_keys('admin')
        self.driver.find_element_by_css_selector("[type='password']").send_keys("123456")
        sleep(1)
        self.driver.find_element_by_css_selector("[type='submit']").click()
        text = self.driver.find_element_by_css_selector(".loginfo").text
        nowtime = time.strftime("%Y_%m_%d %H_%M_%S")
        try:
            self.assertIn("admin", text)
        except AssertionError:
            self.driver.get_screenshot_as_file("../Image/%s--%s.jpg" %(nowtime, sys.exc_info()[1]))
            raise

if __name__ == '__main__':
    unittest.main()

