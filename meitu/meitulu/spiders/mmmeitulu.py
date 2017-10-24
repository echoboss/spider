# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from meitulu.items import MeituluItem


class MmmeituluSpider(CrawlSpider):
    name = 'mmmeitulu'
    allowed_domains = ['www.meitulu.com']
    start_urls = ['https://www.meitulu.com/rihan/' ,'https://www.meitulu.com/gangtai/', 'https://www.meitulu.com/guochan/']

    rules = (
        Rule(LinkExtractor(allow=r'/(rihan|guochan|gangtai)/\d+.html'), follow=True),
        Rule(LinkExtractor(allow=r'/item/\d+.html'), follow=True),
        Rule(LinkExtractor(allow=r'/item/\d+_\d+.html'), callback='parse_item',follow=False)
    )

    def parse_item(self, response):
        # print(response.url)
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()

        item = MeituluItem()

        item['name'] = re.sub(r' \d+/\d+', '', response.xpath('//h1/text()').extract()[0])
        # print(item['name'])
        item['type'] = response.xpath('//div[@class="weizhi"]/span/a[2]/text()').extract()[0]
        # print(item['type'])
        # item['url'] = response.url
        item['img_list'] = response.xpath('//center/img/@src').extract()
        # print(item['img_list'])

        # print(item)
        yield item



        
