# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem
from urllib import parse
from tutorial.requests import SeleniumRequest
from tutorial.Spider import SeleniumSpider
from tutorial.tools import waitForXpath
from bs4 import BeautifulSoup
import re


class InfoSpider(SeleniumSpider):
    name = 'info87'

    def start_requests(self):
        baseurl = 'http://www.chinajiandu.cn/Collection/List/'
        urllist = ['wj', 'xhj', 'yym']
        for i in urllist:
            url = baseurl + i
            yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        if response.status == '404':
            return
        baseurl = 'http://www.chinajiandu.cn'
        # print(response.body.decode('utf-8'))
        for i in response.xpath('/html/body/div[3]/div/ul[2]/li'):
            url = baseurl + i.xpath('a/@href').get()
            # print(url)
            yield scrapy.Request(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        html = response.body.decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        item = TutorialItem()
        # print(html)
        item['midx'] = '87'
        item['name'] = re.findall(r'<h1>(.*?)</h1>', str(soup.find_all('div', class_='title')[0]))[0]
        s = str(soup.find_all('div', class_='imgstyle imgfull')[0])
        item['pic'] = re.findall(r'href="(.*?)"',s)[0]
        item['text'] = soup.find_all('div', class_='cont')[0].text.strip()
        print(item['name'])
        print(item['text'])
        print(item['pic'])
        yield item

    def selenium_func(self, request):
        waitForXpath(self.browser, '/html/body/div[3]/div/ul[2]/li')