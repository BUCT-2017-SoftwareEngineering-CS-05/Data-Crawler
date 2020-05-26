# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import eduItem
from tutorial.selenium.myscrapy import SeleniumRequest
from tutorial.selenium.myscrapy import SeleniumSpider

from lxml import html


class EduSpider(scrapy.Spider):
    name = 'nt'
    # allowed_domains = ['www.dpm.org.cn']
    # start_urls = ['https://www.dpm.org.cn/activity/educations/p/1.html']

    def start_requests(self):
        URL = 'http://www.ntmuseum.com/colunm4/'
        # print(URL)
        yield SeleniumRequest(url=URL, callback=self.parse, dont_filter=True)


    def parse(self, response):
        index = 45
        # / html / body / div[5] / div / div[2] / div[2] / ul / li[1]
        # print(response.xpath('/html/body/div/div/div[2]/div[2]/ul[1]/li[2]/div/a/h3'))
       # ' / html / body / div / div / div[2] / div[2] / ul[1] / li[2] / div / a / h3 / strong'
       #  print(response.xpath('/html/body/form/div[3]/table/tr/td/table/tr[3]/td/table/tr[3]/td/table/tr/td[3]/div/span[2]/div/table[1]/tr[1]'))
        for line in response.xpath('/html/body/section[2]/div[3]/div[2]/div[2]/ul[2]/li'):  # 教育信息爬取
            # print(1)
            item = eduItem()
            item['mid'] = index
            # print(item['mid'])
            #                             '/html/body/div[3]/div/div/ul/li[17]/a'
            # '/html/body/div[8]/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/section/div[2]/header/h3/a'
            item['name'] = line.xpath('./a/text()').extract()[0]
            print(item['name'])
            # print(line.xpath('./a/@href').extract())
            item['url'] = line.xpath('./a/@href').extract()[0]
            print(item['url'])
            # item['details'] = line.xpath('./span/text()').extract()[0].strip()
            yield item

