# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import eduItem
from lxml import html


class EduSpider(scrapy.Spider):
    name = 'sx'
    # allowed_domains = ['www.dpm.org.cn']
    # start_urls = ['https://www.dpm.org.cn/activity/educations/p/1.html']
    def start_requests(self):
        for page in range(1,11):
            URL = 'http://www.shanximuseum.com/activity_list/p/{}.html'.format(page)
            print(URL)
            yield scrapy.Request(url=URL,callback=self.parse)
    def parse(self, response):
        index = 21
        rootUrl = 'http://www.luxunmuseum.com.cn/'
        print(1)
        for line in response.xpath('/html/body/div[6]/div[2]/div/div[3]/div[1]/div'):  # 教育信息爬取
            item = eduItem()
            item['mid'] = index
            # print(item['mid'])
            item['name'] = line.xpath('./div[2]/a/text()').extract()
            # print(line.xpath('./a/@href').extract())
            item['url'] = rootUrl + line.xpath('./div[2]/a/@href').extract()[0]
            yield item