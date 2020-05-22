#-*- codeing = utf-8 -*-
#@Time : 2020/5/20 16:47
#@Author : 张文天
#@File : baidu.py
#@Software: PyCharm

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

print(driver.title)
driver.quit()