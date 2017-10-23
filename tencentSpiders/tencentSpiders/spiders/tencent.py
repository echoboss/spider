# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tencentSpiders.items import TencentspidersItem


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # i = {}
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        for each in response.xpath('(//tr[@class="even"]| //tr[@class="odd"])'):
            item = TencentspidersItem()

            item['name'] = each.xpath('./td/a/text()').extract()[0]
            item['type'] = each.xpath('./td[2]/text()').extract()[0]
            item['numbers'] = each.xpath('./td[3]/text()').extract()[0]
            item['place'] = each.xpath('./td[4]/text()').extract()[0]
            item['publish_time'] = each.xpath('./td[5]/text()').extract()[0]
            item['info_url'] = each.xpath('./td/a/@href').extract()[0]

            yield item
