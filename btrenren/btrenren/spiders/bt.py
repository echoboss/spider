# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# from scrapy.spiders import  Rule
from btrenren.items import BtrenrenItem
# from scrapy_redis.spiders import RedisCrawlSpider


class BtSpider(CrawlSpider):
# class BtSpider(RedisCrawlSpider):
    name = 'bt'
    allowed_domains = ['www.btrenren.com']
    start_urls = ['http://www.btrenren.com/']
    # redis_key = 'bt:start_urls'

    rules = (
        Rule(LinkExtractor(allow=r'/index/p/\d+.html'),),
        Rule(LinkExtractor(allow=r'/subject/\d+.html'), callback='parse_item')
    )
    #
    # def __init__(self, *args, **kwargs):
    #     domain = kwargs.pop('domain', '')
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(BtSpider, self).__init__(*args, **kwargs)




    def parse_item(self, response):
        # print(response.url)
        item = BtrenrenItem()
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i

        # item['name'] = response.xpath('//h1/text()').extract()[0]
        item['alias'] = response.xpath('//ul[@class="moviedteail_list"]/li[1]/a/text()').extract()
        item['tags'] = response.xpath('//ul[@class="moviedteail_list"]/li[2]/a/text()').extract()
        item['locality'] = response.xpath('//ul[@class="moviedteail_list"]/li[3]/a/text()').extract()
        item['year'] = response.xpath('//ul[@class="moviedteail_list"]/li[4]/a/text()').extract()
        item['director'] = response.xpath('//ul[@class="moviedteail_list"]/li[5]/a/text()').extract()
        item['screenwriter'] = response.xpath('//ul[@class="moviedteail_list"]/li[6]/a/text()').extract()
        item['star'] = response.xpath('//ul[@class="moviedteail_list"]/li[7]/a/text()').extract()
        item['imdb'] = response.xpath('//ul[@class="moviedteail_list"]/li[8]/a/@href').extract()
        item['info'] = response.xpath('//ul[@class="moviedteail_list"]/li[9]/a/@href').extract()
        item['bt_url'] = response.xpath('//div[@class="tinfo"]/a/@href').extract()
        item['context'] =response.xpath('//span[@property="v:summary"]/text()').extract()
        # item['img_url'] = response.xpath('')

        # print(item)
        yield item