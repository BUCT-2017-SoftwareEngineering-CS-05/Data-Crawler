# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import eduItem
from tutorial.selenium.myscrapy import SeleniumRequest
from tutorial.selenium.myscrapy import SeleniumSpider

from lxml import html


class EduSpider(scrapy.Spider):
    name = 'dq'
    # allowed_domains = ['www.dpm.org.cn']
    # start_urls = ['https://www.dpm.org.cn/activity/educations/p/1.html']

    def start_requests(self):
        URL = 'http://www.dqsbwg.com/news.asp?classname=%BF%C6%C6%D5%D6%AA%CA%B6&idname=&begpage=0'
        # print(URL)
        yield SeleniumRequest(url=URL, callback=self.parse, dont_filter=True)


    def parse(self, response):
        index = 37
        # / html / body / div[5] / div / div[2] / div[2] / ul / li[1]
        # print(response.xpath('/html/body/div/div/div[2]/div[2]/ul[1]/li[2]/div/a/h3'))
       # ' / html / body / div / div / div[2] / div[2] / ul[1] / li[2] / div / a / h3 / strong'
        for i in range(2,28,2):
            for line in response.xpath('/html/body/table[3]/tr/td/table/tr/td[2]/table/tr[2]/td/div/table/tr[{}]'.format(i)):  # 教育信息爬取
                # print(1)
                item = eduItem()
                item['mid'] = index
                # print(item['mid'])
                #                             '/html/body/div[3]/div/div/ul/li[17]/a'
                item['name'] = line.xpath('./td/a/font/text()').extract()[0]
                print(item['name'])
                # print(line.xpath('./h2/a/@href').extract())
                item['url'] = "http://www.dqsbwg.com/" + line.xpath('./td/a/@href').extract()[0]
                print(item['url'])
                # item['details'] = line.xpath('./li/span/text()').extract()[0].strip()
                yield item
