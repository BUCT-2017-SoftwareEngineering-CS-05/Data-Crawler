# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import eduItem
from lxml import html





class EduSpider(scrapy.Spider):
    name = '1937Education'
    # allowed_domains = ['www.dpm.org.cn']
    # start_urls = ['https://www.dpm.org.cn/activity/educations/p/1.html']
    def start_requests(self):

            URL = 'http://www.1937china.com/views/jyhd_bwcxljsm/bwcxljsm.html'
            # print(URL)
            yield scrapy.Request(url=URL,callback=self.parse)

    def parse(self, response):
        index = 9
        rootUrl = 'http://www.1937china.com/'
        print(response.xpath('/html/body/div[3]/div[2]/div'))
        for line in response.xpath('/html/body/div[3]/div[2]/div/div[2]/div/ul/li'):  # 教育信息爬取
            item = eduItem()
            item['mid'] = index
            # print(item['mid'])
            item['name'] = line.xpath('./a/p/text()').extract()
            print(item['name'])
            # print(line.xpath('./a/@href').extract())
            item['url'] = line.xpath('./a/@href').extract()[0]
            print(item['url'])

            # print(line.xpath('./div[@class="jchg-info"]/a[@class="jchg-name"]/@href').extract()[0])
            yield item
            # print(URL)

