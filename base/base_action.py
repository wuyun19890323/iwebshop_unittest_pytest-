from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver
    # # 网址
    # url = "http://localhost/iwebshop/"

    # 连接网站
    def get_url(self, url):
        self.driver.get(url)

    # 最大化，隐性等待
    def maxi_wait(self, loc):
        self.driver.maximize_window()
        self.driver.implicitly_wait(loc)

    def find_element(self, loc):
        return self.driver.find_element(loc[0], loc[1])

    def click(self, loc):
        self.find_element(loc).click()

    def send_text(self, loc, text):
        self.find_element(loc).send_keys(text)

    def get_att(self, loc):
        return self.find_element(loc).text

    # def find_element(self, loc):
    #     by = loc[0]
    #     value = loc[1]
    #     if by == By.XPATH:
    #         value = self.make_xpath_with_feature(value)
    #     return WebDriverWait(self.driver, 30).until(lambda x: x.find_element(by, value))
    #
    # def find_elements(self, loc):
    #     by = loc[0]
    #     value = loc[1]
    #     if by == By.XPATH:
    #         value = self.make_xpath_with_feature(value)
    #     return WebDriverWait(self.driver, 30).until(lambda x: x.find_elements(by, value))
    #
    # def make_xpath_with_unit_feature(self, loc):
    #     key_index = 0
    #     value_index = 1
    #     option_index = 2
    #     args = loc.split(",")
    #     feature = ""
    #     if len(args) == 2:
    #         feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and "
    #     elif len(args) == 3:
    #         if args[option_index] == "1":
    #             feature = "@" + args[key_index] + "='" + args[value_index] + "'" + "and "
    #         elif args[option_index] == "0":
    #             feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and "
    #     return feature
    #
    # def make_xpath_with_feature(self, loc):
    #     feature_start = "//*["
    #     feature_end = "]"
    #     feature = ""
    #     if isinstance(loc, str):
    #         # 如果是正常的xpath
    #         if loc.startswith("//"):
    #             return loc
    #         feature = self.make_xpath_with_unit_feature(loc)
    #     else:
    #         # loc 列表
    #         for i in loc:
    #             feature += self.make_xpath_with_unit_feature(i)
    #     feature = feature.rstrip("and")
    #     loc = feature_start + feature + feature_end
    #     return loc
