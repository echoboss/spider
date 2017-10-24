# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from meitulu.items import MeituluItem

class MeituSpider(CrawlSpider):
    name = 'meitu'
    allowed_domains = ['www.meitulu.com']
    start_urls = ['https://www.meitulu.com/rihan/','https://www.meitulu.com/gangtai/','https://www.meitulu.com/guochan/',]

    rules = (
        #Rule(LinkExtractor(allow=r'href="/\w+/|/\w+/\d+.html"'), callback='parse_item',),
        Rule(LinkExtractor(allow=r'[.*]',restrict_xpaths=('//div[@id="pages"]')), follow=True),
        Rule(LinkExtractor(allow=r'/item/\d+.html'), callback='parse_item', follow=False),
        #Rule(LinkExtractor(allow=r'[.*]',restrict_xpaths=('//div[@id="pages"]')), callback='parse_item', follow=False),
		
    )

    def parse_item(self, response):
        item = MeituluItem()
        #print(response.url)
        #i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        #return i
        item['name'] = response.xpath('//h1/text()').extract()[0]
        item['types'] = response.xpath('//div[@class="weizhi"]/span/a[2]/text()').extract()[0]
        item['url'] = response.xpath('//center/img/@src').extract()[0]
        item['num'] = re.search(r'\d+ 张',response.text).group().split()[0]
        #print(response.url,item['num'])
        #item['name'] = response.xpath('//h1/text()').extract()[0]
        #item['types'] = response.xpath('//div[@class="weizhi"]/span/a[2]/text()').extract()[0]
        #item['url'] = response.xpath('//center/img/@src').extract()[0]
        #item['num'] = response.xpath('//div[@class="c_l"]/p[3]/text()').extract()[0].split()
        #print(response.text)
        #print(item['num'])
        yield item
