# 76 - 119
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
    name = 'info84'

    def start_requests(self):
        baseurl = 'http://61.187.53.122/List.aspx?lang=zh-CN&page='
        for i in range(1, 11):
            url = baseurl + str(i)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.status == '404':
            return
        baseurl = 'http://61.187.53.122/'
        # print(response.body.decode('utf-8'))
        for i in response.xpath('//*[@id="thumbnailUL"]/li'):
            url = baseurl + i.xpath('div/a/@href').get()
            # print(url)
            yield scrapy.Request(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        html = response.body.decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        item = TutorialItem()
        # print(html)
        item['midx'] = '84'
        item['name'] = soup.find_all('div', class_='title')[0].text
        baseurl = 'http://61.187.53.122'
        s = str(soup.find_all('a', id="linkPicture")[0])
        item['pic'] = baseurl + re.findall(r'src="(.*?)"', s)[0]
        item['text'] = soup.find_all("div", class_="c-all-des")[0].text.strip()
        print(item['name'])
        print(item['text'])
        print(item['pic'])
        yield item
