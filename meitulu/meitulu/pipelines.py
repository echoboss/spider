# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests


class MeituluPipeline(object):
    def __init__(self):
        self.storge_path = os.path.join('/data','meitulu')
        self.headers = {}

    def process_item(self, item, spider):
        if not os.path.isdir(self.storge_path):
            os.mkdir(self.storge_path)
        # type = item['type']
        # name = item['name']
        for ln in item['img_list']:
            pos = ln.rindex('/') + 1
            img_name = ln[pos:]
            if not os.path.isdir(os.path.join(self.storge_path, item['type'], item['name'])):
                os.makedirs(os.path.join(self.storge_path, item['type'], item['name']))
            local_path = os.path.join(self.storge_path, item['type'], item['name'], img_name)
            # print(local_path)
            if not os.path.isfile(local_path):
                response = requests.get(ln,).content
                print('\033[1;33mDown Loading ...... \033[0m\n\033[1;31m{}\n\033[0m'.format(ln))
                with open(local_path, 'wb') as img:
                    img.write(response)
                print('\033[1;35mWrite local success ......\033[0m\n\033[1;34m{}\n\n\033[0m'.format(local_path))
            else:
                print("\033[1;35mIt's already been downloaded ......\033[0m\n\033[1;32m{}\n\n\033[0m".format(local_path))




        # print(item['name'])
        # print(item['type'])
        # print(item['img_list'])


        return item
