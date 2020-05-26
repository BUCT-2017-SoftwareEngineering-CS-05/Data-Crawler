# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import eduItem
from lxml import html


class EduSpider(scrapy.Spider):
    name = 'luxEducation'
    # allowed_domains = ['www.dpm.org.cn']
    # start_urls = ['https://www.dpm.org.cn/activity/educations/p/1.html']
    def start_requests(self):

            URL = 'http://www.luxunmuseum.com.cn/jiaoyuhuodongjieshao/'
            # print(URL)
            yield scrapy.Request(url=URL,callback=self.parse)

    def parse(self, response):
        index = 6
        rootUrl = 'http://www.luxunmuseum.com.cn/'
        for line in response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/div[@class="list_list"]'):  # 教育信息爬取
            item = eduItem()
            item['mid'] = index
            # print(item['mid'])
            item['name'] = line.xpath('./div[@class="list_l l"]/dt/a/text()').extract()
            # print(line.xpath('./a/@href').extract())
            item['url'] = rootUrl + line.xpath('./div[@class="list_l l"]/dt/a/@href').extract()[0]
            yield item