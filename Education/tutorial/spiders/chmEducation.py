# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import eduItem
from lxml import html





class EduSpider(scrapy.Spider):
    name = 'chmEducation'
    # allowed_domains = ['www.dpm.org.cn']
    # start_urls = ['https://www.dpm.org.cn/activity/educations/p/1.html']
    def start_requests(self):
        for page in range(3,14):
            URL = 'http://www.chnmuseum.cn/fw/hd/zxhd/jyhdyy/index_{}.shtml'.format(page)
            # print(URL)
            yield scrapy.Request(url=URL,callback=self.parse)

    def parse(self, response):
        index = 11
        rootUrl = 'http://www.chnmuseum.cn'
        print(response.xpath('/html/body/div[4]/div/div/div/ul[2]/li[1]'))
        for line in response.xpath('/html/body/div[4]/div/div/div/ul[2]/li'):  # 教育信息爬取
            item = eduItem()
            item['mid'] = index
            # print(item['mid'])
            item['name'] = line.xpath('./a/text()').extract()
            print(item['name'])
            # print(line.xpath('./a/@href').extract())
            item['url'] = rootUrl+line.xpath('./a/@href').extract()[0][1:]
            print(item['url'])

            # print(line.xpath('./div[@class="jchg-info"]/a[@class="jchg-name"]/@href').extract()[0])
            yield item
            # print(URL)

