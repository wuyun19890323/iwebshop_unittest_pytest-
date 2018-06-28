import sys
import os
import unittest
sys.path.append(os.getcwd())
from base.base_driver import browser_fire
from page.page_load import PageLoad


class TestLoad(unittest.TestCase):

    # 这是一种写作方式，可以不用yml文件来读取数据
    # 网址
    url = "http://localhost/iwebshop/"
    # 登录后的文本
    login_after_text = "您好，欢迎您来到iwebshop购物！[安全退出]"
    # 填写用户名或邮箱、填写密码、用户名和密码匹配
    tooltip_text1 = '填写用户名或邮箱'
    tooltip_text2 = '填写密码'
    tooltip_text3 = '用户名和密码不匹配'
    # 输入账户
    username_text1 = "admin"
    username_text2 = "admin1"
    # 输入密码
    password_text1 = "123456"
    password_text2 = "1234567"

    def login_text(self, text):
        text = text + self.login_after_text
        return text

    def get_ass(self):
        self.driver.get_scr(self.driver.load_get_photo())

    def setUp(self):
        self.driver = browser_fire()
        self.scr_load = PageLoad(self.driver)
        self.scr_load.get_url(self.url)
        self.scr_load.maxi_wait(30)

    def tearDown(self):
        self.driver.quit()

    # 正确账户正确密码
    # 其中还必须测试账号前后空格和中间空格，密码字母大小写
    def test_load001(self):
        # 点击登录链接
        self.scr_load.click_load_mark()
        # 输入用户名
        self.scr_load.input_text_username(self.username_text1)
        # 输入密码
        self.scr_load.input_text_password(self.password_text1)
        # 点击登录按钮
        self.scr_load.click_load_button()
        # 断言 文本域-安全退出
        self.scr_load.ass_true_or_false(self.login_text(self.username_text1), self.scr_load.get_load_text())
        # 安全退出
        self.scr_load.click_load_quit()

    # 正确账户错误密码
    def test_load002(self):
        # 点击登录链接
        self.scr_load.click_load_mark()
        # 输入用户名
        self.scr_load.input_text_username(self.username_text1)
        # 输入密码
        self.scr_load.input_text_password(self.password_text2)
        # 点击登录按钮
        self.scr_load.click_load_button()
        # 断言 用户名和密码不匹配
        self.scr_load.ass_true_or_false(self.tooltip_text3, self.scr_load.get_tooltip_text3())

    # 正确账户密码为空
    def test_load003(self):
        # 点击登录链接
        self.scr_load.click_load_mark()
        # 输入用户名
        self.scr_load.input_text_username(self.username_text1)
        # 输入密码
        self.scr_load.input_text_password("")
        # 点击登录按钮
        self.scr_load.click_load_button()
        # 断言 填写密码
        self.scr_load.ass_true_or_false(self.tooltip_text2, self.scr_load.get_tooltip_text2())

    # 错误账户正确密码
    def test_load004(self):
        # 点击登录链接
        self.scr_load.click_load_mark()
        # 输入用户名
        self.scr_load.input_text_username(self.username_text2)
        # 输入密码
        self.scr_load.input_text_password(self.password_text1)
        # 点击登录按钮
        self.scr_load.click_load_button()
        # 断言 填写密码
        self.scr_load.ass_true_or_false(self.tooltip_text3, self.scr_load.get_tooltip_text3())

    # 错误账户错误密码
    def test_load005(self):
        # 点击登录链接
        self.scr_load.click_load_mark()
        # 输入用户名
        self.scr_load.input_text_username(self.username_text2)
        # 输入密码
        self.scr_load.input_text_password(self.password_text2)
        # 点击登录按钮
        self.scr_load.click_load_button()
        # 断言 填写密码
        self.scr_load.ass_true_or_false(self.tooltip_text3, self.scr_load.get_tooltip_text3())

    # 错误账户密码为空
    def test_load006(self):
        # 点击登录链接
        self.scr_load.click_load_mark()
        # 输入用户名
        self.scr_load.input_text_username(self.username_text2)
        # 输入密码
        self.scr_load.input_text_password("")
        # 点击登录按钮
        self.scr_load.click_load_button()
        # 断言 填写密码
        self.scr_load.ass_true_or_false(self.tooltip_text2, self.scr_load.get_tooltip_text2())

    # 空账户正确密码
    def test_load007(self):
        # 点击登录链接
        self.scr_load.click_load_mark()
        # 输入用户名
        self.scr_load.input_text_username("")
        # 输入密码
        self.scr_load.input_text_password(self.password_text1)
        # 点击登录按钮
        self.scr_load.click_load_button()
        # 断言 填写密码
        self.scr_load.ass_true_or_false(self.tooltip_text1, self.scr_load.get_tooltip_text1())

    # 空账户错误密码
    def test_load008(self):
        # 点击登录链接
        self.scr_load.click_load_mark()
        # 输入用户名
        self.scr_load.input_text_username("")
        # 输入密码
        self.scr_load.input_text_password(self.password_text2)
        # 点击登录按钮
        self.scr_load.click_load_button()
        # 断言 填写密码
        self.scr_load.ass_true_or_false(self.tooltip_text1, self.scr_load.get_tooltip_text1())

    # 空账户空密码
    def test_load009(self):
        # 点击登录链接
        self.scr_load.click_load_mark()
        # 输入用户名
        self.scr_load.input_text_username("")
        # 输入密码
        self.scr_load.input_text_password("")
        # 点击登录按钮
        self.scr_load.click_load_button()
        # 断言 填写密码
        self.scr_load.ass_true_or_false(self.tooltip_text1, self.scr_load.get_tooltip_text1())

if __name__ == '__main__':
    unittest.main()
