import sys
import time
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class PageLoad(BaseAction):

    # 定位登录链接
    load_mark = By.XPATH, "//a[@href='/iwebshop/index.php?controller=simple&action=login']"
    # 定位用户名
    username = By.XPATH, "//input[@type='text']"
    # 定位密码
    password = By.XPATH, "//input[@type='password']"
    # 定位登录按钮
    load_button = By.XPATH, "//input[@type='submit']"
    # 定位登录后文本域
    load_text = By.XPATH, "//p[@class='loginfo']"
    # 定位退出按钮
    load_quit = By.XPATH, "//a[@class='reg']"
    # 定位登录前账户或密码错误提示 用户名和密码不匹配
    load_wrong = By.XPATH, "//div[@class ='prompt']"
    # 定位登录前账户为空是 提示填写用户名或邮箱
    load_username_null = By.XPATH, "//tbody/tr[1]/td/label[@class='invalid-msg']"
    # 定位登录前密码为空是 提示填写密码
    load_password_null = By.XPATH, "//tbody/tr[2]/td/label[@class='invalid-msg']"

    # 文本域
    def get_load_text(self):
        return self.get_att(self.load_text)

    # 获取文本 填写用户名或邮箱
    def get_tooltip_text1(self):
        return self.get_att(self.load_username_null)

    # 获取文本 填写密码
    def get_tooltip_text2(self):
        return self.get_att(self.load_password_null)

    # 获取文本 用户名和密码不匹配
    def get_tooltip_text3(self):
        return self.get_att(self.load_wrong)

    def click_load_quit(self):
        self.click(self.load_quit)

    def click_load_mark(self):
        self.click(self.load_mark)

    def input_text_username(self, text):
        self.send_text(self.username, text)

    def input_text_password(self, text):
        self.send_text(self.password, text)

    def click_load_button(self):
        self.click(self.load_button)

    def load_get_photo(self):
        loading_start = "./Image/"
        now_time = time.strftime("%Y_%m_%d %H_%M_%S")
        loading_end = "--" + str(sys.exc_info()[1]) + ".jpg"
        loading_file = loading_start + now_time + loading_end
        return loading_file

    def get_scr(self, loc):
        self.driver.get_screenshot_as_file(loc)

    def get_ass(self):
        self.get_scr(self.load_get_photo())

    def ass_true_or_false(self, text1, text2):
        try:
            assert text1 == text2
        except AssertionError:
            self.get_ass()
