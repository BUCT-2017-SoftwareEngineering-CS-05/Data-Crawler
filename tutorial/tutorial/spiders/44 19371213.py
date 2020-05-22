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
    name = 'info44'

    def start_requests(self):

        base_url = "http://www.19371213.com.cn/collection/zdwwjs/201811"
        l = ['06', '13', '11']
        for i in l:
            url = base_url + '/t201811' + i + '_5907'
            for j in range(100, 1000):
                url0 = url + str(j) + '.html'
                yield scrapy.Request(url=url0, callback=self.parse)

    def parse(self, response):
        if response.status == '404':
            return
        # print(response.body.decode('utf-8'))
        baseurl = 'http://www.19371213.com.cn/collection/zdwwjs/201811'
        item = TutorialItem()
        item['midx'] = '44'
        item['name'] = response.xpath('/html/body/div[6]/div/div/div/div[2]/div/div/article/section/div[2]/header/h4/text()').get().strip()
        t = ''
        for i in response.xpath('/html/body/div[6]/div/div/div/div[2]/div/div/article/section/div[2]/div/div/div//img'):
            t = i.xpath('@src').get()[1:]
        item['pic'] = baseurl + t
        t = ''
        for i in response.xpath('/html/body/div[6]/div/div/div/div[2]/div/div/article/section/div[2]/div/div/div//p'):
            if i.xpath('text()').get() != None:
                t = t + i.xpath('text()').get().strip()
        item['text'] = t
        print(item['name'])
        print(item['text'])
        print(item['pic'])
        yield item

