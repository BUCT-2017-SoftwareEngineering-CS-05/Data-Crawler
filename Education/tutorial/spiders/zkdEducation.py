# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import eduItem
from lxml import html





class EduSpider(scrapy.Spider):
    name = 'zkdEducation'
    # allowed_domains = ['www.dpm.org.cn']
    # start_urls = ['https://www.dpm.org.cn/activity/educations/p/1.html']
    def start_requests(self):
            URL = 'http://www.zkd.cn/bjyr/index.jhtml'
            # print(URL)
            yield scrapy.Request(url=URL,callback=self.parse)

    def parse(self, response):
        index = 10
        rootUrl = 'http://www.zkd.cn/'
        print(response.xpath('/html/body/div[3]/div/div[2]/div[4]/ul/li'))
        for line in response.xpath('/html/body/div[3]/div/div[2]/div[4]/ul/li'):  # 教育信息爬取
            item = eduItem()
            item['mid'] = index
            # print(item['mid'])
            item['name'] = line.xpath('./a/text()').extract()
            print(item['name'])
            # print(line.xpath('./a/@href').extract())
            item['url'] = line.xpath('./a/@href').extract()[0]
            print(item['url'])

            # print(line.xpath('./div[@class="jchg-info"]/a[@class="jchg-name"]/@href').extract()[0])
            yield item
            # print(URL)

