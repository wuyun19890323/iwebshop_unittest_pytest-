from selenium import webdriver


# 浏览器实例化：火狐
def browser_fire():
    driver = webdriver.Firefox()
    return driver


# 浏览器实例化：谷歌
def browser_chrome():
    driver = webdriver.Chrome()
    return driver
