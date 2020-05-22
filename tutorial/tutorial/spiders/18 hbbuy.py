# 76 - 119
# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem
from urllib import parse
from tutorial.requests import SeleniumRequest
from tutorial.Spider import SeleniumSpider
from tutorial.tools import waitForXpath
from bs4 import BeautifulSoup


class InfoSpider(scrapy.Spider):
    name = 'info18'

    def start_requests(self):
        start_page = 1208
        end_page = 1218
        base_url = "http://www.hebeimuseum.org.cn/contents/25/"
        for i in range(start_page, end_page):
            url = base_url + str(i) + '.html'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.status == '404':
            return
        item = TutorialItem()
        baseurl = 'http://www.hebeimuseum.org.cn'
        # print(response.body.decode('utf-8'))
        item['midx'] = '18'
        item['name'] = response.xpath('/html/body/div[4]/div[2]/div[2]/div/dl/dd/h3/text()').get()
        t = ''
        tag = ''
        if len(response.xpath('/html/body/div[4]/div[2]/div[2]/div/dl/dd/div//span')) != 0:
            tag = response.xpath('/html/body/div[4]/div[2]/div[2]/div/dl/dd/div//span')
        elif len(response.xpath('/html/body/div[4]/div[2]/div[2]/div/dl/dd/p[4]//span')) != 0:
            tag = response.xpath('/html/body/div[4]/div[2]/div[2]/div/dl/dd/p[4]//span')
        elif len(response.xpath('/html/body/div[4]/div[2]/div[2]/div/dl/dd/p[3]//span')) != 0:
            tag = response.xpath('/html/body/div[4]/div[2]/div[2]/div/dl/dd/p[3]//span')
        else:
            tag = response.xpath('/html/body/div[4]/div[2]/div[2]/div/dl/dd/p/span')
        # print(tag)
        for i in tag:
            t = t + i.xpath('text()').get().strip()
        item['text'] = t
        item['pic'] = baseurl + response.xpath('/html/body/div[4]/div[2]/div[2]/div/dl/dt/img/@src').get()
        print(item['name'])
        print(item['text'])
        print(item['pic'])
        yield item

