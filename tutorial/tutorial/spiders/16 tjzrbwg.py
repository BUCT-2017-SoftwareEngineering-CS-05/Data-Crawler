# 76 - 119
# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem
from bs4 import BeautifulSoup
from urllib import parse
from tutorial.requests import SeleniumRequest
from tutorial.Spider import SeleniumSpider
from tutorial.tools import waitForXpath
from bs4 import BeautifulSoup


class InfoSpider(SeleniumSpider):
    name = 'info16'

    def start_requests(self):
        start_page = 1
        end_page = 19
        base_url = "https://www.tjnhm.com/index.php?p=kxyj&lanmu=4&c_id=16&page="
        for i in range(start_page, end_page):
            url = base_url + str(i)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.status == '404':
            return
        # print(response.body.decode('utf-8'))
        # print(response.xpath('/html/body/div[3]/div/dl/dd/div[1]/text()').get())
        baseurl = 'https://www.tjnhm.com/'
        for i in response.xpath('/html/body/div[2]/div[1]/div[2]/ul/li'):
            link = baseurl + i.xpath('a/@href').get()
            yield SeleniumRequest(link, callback=self.detail_parse)

    def detail_parse(self, response):
        items = TutorialItem()
        baseurl = 'https://www.tjnhm.com/'
        items['midx'] = '16'
        url = ''
        if response.xpath('/html/body/div[2]/div[1]/div[2]/p[1]/span/img/@src').get() != None:
            url = response.xpath('/html/body/div[2]/div[1]/div[2]/p[1]/span/img/@src').get()
        else:
            url = response.xpath('/html/body/div[2]/div[1]/div[2]/p[1]/img/@src').get()
        if url == None:
            return
        items['pic'] = baseurl + url
        items['name'] = response.xpath('/html/body/div[2]/div[1]/div[2]/h1/text()').get().strip()
        t = ''
        for i in response.xpath('//*[@id="aboutus_text"]//span'):
            if i.xpath('text()').get() == None:
                return
            t = t + i.xpath('text()').get().strip()
        items['text'] = t
        print(items['name'])
        print(items['text'])
        print(items['pic'])
        yield items
