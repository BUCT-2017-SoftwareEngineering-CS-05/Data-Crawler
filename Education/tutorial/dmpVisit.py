import scrapy
from tutorial.items import visitItem

class VisSpider(scrapy.Spider):
    name = 'dmpVisit'

    def start_requests(self):
        URL = 'https://www.dpm.org.cn/Visit.html#block3'
        yield scrapy.Request(url=URL,callback=self.parse)

    def parse(self, response):
        print(response.xpath('/html/body/div[4]/div[2]/div/div[2]/div[2]/div[1]/h1/span/text()').extract())
        print(response.xpath('/html/body/div[4]/div[2]/div/div[2]/div[2]/div[1]/ul/li[1]/text()').extract())

        item1 = visitItem()
        season = []
        season.extend(response.xpath('/html/body/div[4]/div[2]/div/div[2]/div[2]/div[1]/h1/span[1]/text()').extract())
        season.extend(response.xpath('/html/body/div[4]/div[2]/div/div[2]/div[2]/div[1]/h1/span[2]/text()').extract())
        item1['season'] = "".join(season)
        time = []
        time.extend(response.xpath('/html/body/div[4]/div[2]/div/div[2]/div[2]/div[1]/ul/li[1]/text()').extract())
        time.extend(response.xpath('/html/body/div[4]/div[2]/div/div[2]/div[2]/div[1]/ul/li[1]/span/text()').extract())
        time.extend(response.xpath('/html/body/div[4]/div[2]/div/div[2]/div[2]/div[1]/ul/li[2]/text()').extract())
        time.extend(response.xpath('/html/body/div[4]/div[2]/div/div[2]/div[2]/div[1]/ul/li[2]/span/text()').extract())
        item1['time'] = "".join(time)
        yield item1
        item2 = visitItem()

        season = []
        season.extend(response.xpath('/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/h1/span[2]/text()').extract())
        season.extend(response.xpath('/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/h1/span[1]/text()').extract())
        item2['season'] = "".join(season)
        time = []
        time.extend( response.xpath('/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/ul/li[1]/text()').extract())
        time.extend(response.xpath('/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/ul/li[1]/span/text()').extract())
        time.extend( response.xpath('/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/ul/li[2]/text()').extract())
        time.extend(response.xpath('/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/ul/li[2]/span/text()').extract())
        item2['time'] = "".join(time)
        yield item2

        # item['time'] = response.xpath('/html/body/div[4]/div[2]/div/div[2]/div[2]/div[1]/ul/text()').extract
        # for line in response.xpath('/html/body/div[4]/div[2]/div/div/div[2]/ul/li'):  # 学术信息爬取
        #     item = visitItem()
        # #     print(line.xpath('./h1/a/text()').extract())
        #     item['season'] = line.xpath('./h1/a/text()').extract()
        # #     print(line.xpath('./a/@href').extract())
        #     item['time'] = rootUrl + line.xpath('./h1/a/@href').extract()[0]
        #     yield item
