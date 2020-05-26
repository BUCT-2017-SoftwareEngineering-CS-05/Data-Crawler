# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import eduItem
from lxml import html





class EduSpider(scrapy.Spider):
    name = 'cstmEducation'
    # allowed_domains = ['www.dpm.org.cn']
    # start_urls = ['https://www.dpm.org.cn/activity/educations/p/1.html']
    def start_requests(self):
        for page in range(8):
            URL = 'http://cstm.cdstm.cn/e/extend/science/scienceOrder.ctrl.php?page={}&action=getMoreActivity'.format(page)
            # print(URL)
            yield scrapy.Request(url=URL,callback=self.parse)

    def parse(self, response):
        index = 2
        rootUrl = 'http://cstm.cdstm.cn/'
        for line in response.xpath('/html/body/div[1]/div/div[@class="jchg-cont"]'):  # 教育信息爬取
            item = eduItem()
            item['mid'] = index
            # print(item['mid'])
            item['name'] = line.xpath('./div[@class="jchg-info"]/a[@class="jchg-name"]/text()').extract()
            # print(line.xpath('./a/@href').extract())
            item['url'] =  line.xpath('./div[@class="jchg-info"]/a[@class="jchg-name"]/@href').extract()[0]
            # print(line.xpath('./div[@class="jchg-info"]/a[@class="jchg-name"]/@href').extract()[0])
            yield item
            # print(URL)

