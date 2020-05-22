import logging
import scrapy
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class SeleniumSpider(scrapy.Spider):
    SetHeadless = True
    EnableBrowserCookies = True

    def __init__(self, *args, **kwargs):
        super(SeleniumSpider, self).__init__(*args, **kwargs)
        self.browser = self._get_browser()

    def _get_browser(self):
        logging.getLogger('selenium').setLevel('ERROR')
        logging.getLogger('urllib3').setLevel('ERROR')
        return self._use_firefox()

    def _use_firefox(self):
        profile = webdriver.FirefoxProfile()
        options = webdriver.FirefoxOptions()
        profile.set_preference('permissions.default.image', 2)
        profile.set_preference('browser.migration.version', 9001)
        profile.set_preference('permissions.default.stylesheet', 2)
        profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')

        if hasattr(self, "EnableBrowserCookies") and self.EnableBrowserCookies:
            profile.set_preference("network.cookie.cookieBehavior", 2)

        if self.SetHeadless:
            profile.set_preference("network.cookie.cookieBehavior", 2)
        options.add_argument('--disable-gpu')
        options = Options()
        options.headless = True
        return webdriver.Firefox(firefox_profile=profile, options=options, firefox_options=options)

    def selenium_func(self, request):
        pass

    def closed(self, reason):
        self.browser.quit()
