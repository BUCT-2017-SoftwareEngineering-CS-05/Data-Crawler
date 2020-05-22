# 76 - 119
# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem
from urllib import parse
from tutorial.requests import SeleniumRequest
from tutorial.Spider import SeleniumSpider
from tutorial.tools import waitForXpath
from bs4 import BeautifulSoup


class InfoSpider(SeleniumSpider):
    name = 'info11'

    def start_requests(self):
        start_page = 341
        end_page = 349
        base_url = "http://www.chnmuseum.cn/zp/zpml/cpjs_cpfl/?wwfl="
        for i in range(start_page, end_page):
            url = base_url + str(i)
            yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        if response.status == '404':
            return
        # print(response.body.decode('utf-8'))
        # print(response.xpath('/html/body/div[3]/div/dl/dd/div[1]/text()').get())

        for i in response.xpath('//*[@id="ulHtml"]/li'):
            link = i.xpath('dl/dt/a/@href').get()
            pic = i.xpath('dl/dt/a/img/@src').get()
            yield scrapy.Request(link, meta={'pic': pic}, callback=self.detail_parse)

    def detail_parse(self, response):
        items = TutorialItem()
        items['midx'] = '11'
        items['pic'] = response.meta['pic']
        items['name'] = response.xpath('/html/body/div[3]/div/dl/dt/div[1]/text()').get().strip()
        html = str(response.body.decode('utf-8'))
        soup = BeautifulSoup(html, 'html.parser')
        t = ''
        for i in soup.find('div', class_='wwms').children:
            if i.string != None:
                t = t + i.string.strip()
        items['text'] = t
        yield items

    def selenium_func(self, request):
        waitForXpath(self.browser, '//*[@id="ulHtml"]/li')
