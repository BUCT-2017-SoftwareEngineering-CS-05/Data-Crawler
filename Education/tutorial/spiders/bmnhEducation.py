# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import eduItem
from lxml import html





class EduSpider(scrapy.Spider):
    name = 'bmnhEducation'
    # allowed_domains = ['www.dpm.org.cn']
    # start_urls = ['https://www.dpm.org.cn/activity/educations/p/1.html']
    def start_requests(self):
        for page in range(2,6):
            URL = 'http://www.bmnh.org.cn/jyhd/hdjs/2/list_{}.shtml'.format(page)
            # print(URL)
            yield scrapy.Request(url=URL,callback=self.parse)

    def parse(self, response):
        index = 8
        rootUrl = 'http://www.bmnh.org.cn/'
        for line in response.xpath('/html/body/div[3]/div[2]/div[2]/p'):  # 教育信息爬取
            item = eduItem()
            item['mid'] = index
            # print(item['mid'])
            item['name'] = line.xpath('./a/span/text()').extract()
            # print(line.xpath('./a/@href').extract())
            item['url'] = rootUrl+line.xpath('./a/@href').extract()[0]
            # print(line.xpath('./div[@class="jchg-info"]/a[@class="jchg-name"]/@href').extract()[0])
            yield item
            # print(URL)

