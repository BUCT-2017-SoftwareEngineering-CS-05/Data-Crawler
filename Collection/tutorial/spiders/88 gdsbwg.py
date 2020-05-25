# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem
from tutorial.requests import SeleniumRequest
from tutorial.Spider import SeleniumSpider
from tutorial.tools import waitForXpath
from bs4 import BeautifulSoup
import re


class InfoSpider(SeleniumSpider):
    name = 'info88'

    def start_requests(self):
        baseurl = 'http://www.gdmuseum.com/gdmuseum/_300746/_300758/'
        urllist = ['tc45', 'qtq', 'yq43', 'sh87', 'jmd50', 'zx59', 'dy']
        for i in urllist:
            url = baseurl + i + '/index.html'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.status == '404':
            return
        baseurl = 'http://www.gdmuseum.com'
        for i in response.xpath('/html/body/div[7]/div[2]/div[4]/div[2]/div/div[2]/div[1]/div'):
            url = baseurl + i.xpath('a/@href').get()
            yield SeleniumRequest(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        html = response.body.decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        item = TutorialItem()
        baseurl = 'http://www.gdmuseum.com'
        item['midx'] = '88'
        s = str(soup.find_all('div', class_="js_title show_title")[0])
        item['name'] = re.findall(r'<p>(.*?)</p>', s)[0]
        s = str(soup.find_all('div', class_="li_cont")[0])
        item['pic'] = baseurl + re.findall(r'src="(.*?)"', s)[0]
        s = str(soup.find_all('div', class_='cont')[0])
        t = ''
        for i in re.findall(r'<p>(.*?)</p>', s):
            t = t + i
        item['text'] = t
        print(item['name'])
        print(item['text'])
        print(item['pic'])
        yield item

    def selenium_func(self, request):
        waitForXpath(self.browser, '/html/body/div[7]/div[1]/div/div[2]/div[3]/ul/li/div/img')
