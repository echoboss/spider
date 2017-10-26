# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from mm131.items import Mm131Item
import re

class MmSpider(CrawlSpider):
    name = 'mm'
    allowed_domains = ['m.mm131.com']
    start_urls = ['http://m.mm131.com/xinggan/',
                    'http://m.mm131.com/qingchun/',
                    'http://m.mm131.com/xiaohua/',
                    'http://m.mm131.com/chemo/',
                    'http://m.mm131.com/qipao/',
                    'http://m.mm131.com/mingxing/',]

    rules = (
        Rule(LinkExtractor(allow=r'list_\d_\d+.html'), follow=True),
        Rule(LinkExtractor(allow=r'http://m.mm131.com/\w+/\d+.html'), callback='parse_item',),
    )

    def parse_item(self, response):
        print(response.url)
        item = Mm131Item()
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        """
        item['name'] = response.xpath('//h2[@class="mm-title"]/text()').extract()[0]
        item['types'] = response.xpath('//span[@class="post-meta"]/a/text()').extract()[0]
        item['num'] = re.findall(r'/(\d+)',response.xpath('//span[@class="rw"]/text()').extract()[0])[0]
        item['img_url'] = self.get_num(response)

        yield item

    def get_num(self,response):
        first_url = response.xpath('//div[@class="post-content single-post-content"]//img/@src').extract()[0]
        pos = int(first_url.rindex('/')) + 1
        url = first_url[:pos]
        return url
    """