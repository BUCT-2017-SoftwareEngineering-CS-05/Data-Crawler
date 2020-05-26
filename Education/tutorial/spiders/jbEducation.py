# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import eduItem
from lxml import html


class EduSpider(scrapy.Spider):
    name = 'jbEducation'
    # allowed_domains = ['www.dpm.org.cn']
    # start_urls = ['https://www.dpm.org.cn/activity/educations/p/1.html']
    def start_requests(self):
        for page in range(1,5):
            URL = 'http://www.jb.mil.cn/cyhd/jzhd/index_{}.html'.format(page)
            # print(URL)
            yield scrapy.Request(url=URL,callback=self.parse)

    def parse(self, response):
        index = 4
        rootUrl = 'http://www.jb.mil.cn/cyhd/jzhd/'
        for line in response.xpath('/html/body/div[4]/div/div[3]/ul/li'):  # 教育信息爬取
            item = eduItem()
            item['mid'] = index
            # print(item['mid'])
            item['name'] = line.xpath('./a/h3/text()').extract()
            # print(line.xpath('./a/@href').extract())
            item['url'] = rootUrl + line.xpath('./a/@href').extract()[0][1:]
            yield item