import scrapy
from tutorial.items import academyItem

class VisSpider(scrapy.Spider):
    name = 'dmpAcademy'
    def start_requests(self):
        for page in range(1,11):
            URL = 'https://www.dpm.org.cn/learning/dynamic/p/{}.html'.format(page)
            yield scrapy.Request(url=URL,callback=self.parse)
    def parse(self, response):
        index =1
        rootUrl = 'www.dpm.org.cn'
        print(response.xpath('/html/body/div[4]/div[2]/div/div/div[2]/ul/li'))
        for line in response.xpath('/html/body/div[4]/div[2]/div/div/div[2]/ul/li'):  # 学术信息爬取
            item = academyItem()
        #     print(line.xpath('./h1/a/text()').extract())
            item['name'] = line.xpath('./h1/a/text()').extract()
        #     print(line.xpath('./a/@href').extract())
            item['url'] = rootUrl + line.xpath('./h1/a/@href').extract()[0]
            yield item
