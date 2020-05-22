import functools
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def waitFor(browser, select_arg, select_method, timeout=2):
    element = WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located((select_method, select_arg))
    )


# 用xpath选择器等待元素
waitForXpath = functools.partial(waitFor, select_method=By.XPATH)

# 用css选择器等待元素
waitForCss = functools.partial(waitFor, select_method=By.CSS_SELECTOR)
