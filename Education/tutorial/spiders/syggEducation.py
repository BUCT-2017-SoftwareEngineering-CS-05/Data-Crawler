# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import eduItem
from tutorial.selenium.myscrapy import SeleniumRequest
from tutorial.selenium.myscrapy import SeleniumSpider

from lxml import html


class EduSpider(scrapy.Spider):
    name = 'sygg'
    # allowed_domains = ['www.dpm.org.cn']
    # start_urls = ['https://www.dpm.org.cn/activity/educations/p/1.html']

    def start_requests(self):
        for page in range(1, 6):
            URL = 'http://www.sypm.org.cn/news_list3/newsCategoryId=71&FrontNews_list01-001_pageNo={}&FrontNews_list01-001_pageSize=20.html#'.format(page)
            # print(URL)
            yield scrapy.Request(url=URL,callback=self.parse)

    def parse(self, response):
        index = 29
        # / html / body / div[5] / div / div[2] / div[2] / ul / li[1]
        # print(response.xpath('/html/body/div/div/div[2]/div[2]/ul[1]/li[2]/div/a/h3'))
       # ' / html / body / div / div / div[2] / div[2] / ul[1] / li[2] / div / a / h3 / strong'
        for line in response.xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[1]/ul/li[@class="content column-num1"]'):  # 教育信息爬取
            # print(1)
            item = eduItem()
            item['mid'] = index
            # print(item['mid'])
            item['name'] = line.xpath('./div/ul/li[1]/h3/a/@title').extract()[0]
            print(item['name'])
            # print(line.xpath('./h2/a/@href').extract())
            item['url'] = "http://www.sypm.org.cn/" + line.xpath('./div/ul/li[1]/h3/a/@href').extract()[0]
            print(item['url'])
            # '/ html / body / div[1] / div[4] / div[1] / div / div[2] / div / div[2] / div / div / div[2] / div / div / \
            #   div[1] / ul / li[1] / div / ul / li[2]'
            item['details'] = line.xpath('./div/ul/li[2]/text()').extract()[0].strip()
            yield item
