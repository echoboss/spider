# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests


class MeituluPipeline(object):
    def __init__(self):
        self.storge_path = os.path.join('/data','meitu')
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

    def process_item(self, item, spider):
        if not os.path.isdir(self.storge_path):
            os.mkdir(self.storge_path)

        pos = item['url'].rindex('/') + 1
        url_name = item['url'][:pos]

        if not os.path.isdir(os.path.join(self.storge_path,item['types'],item['name'])):
            os.makedirs(os.path.join(self.storge_path,item['types'],item['name']))
        
        for nn in range(0,int(item['num']) + 1):
            fullurlname = url_name + str(nn) + '.jpg'
            local_path = os.path.join(self.storge_path,item['types'],item['name'],str(nn) + '.jpg')
            if not os.path.isfile(local_path):
                try:
                    response = requests.get(fullurlname,headers=self.headers).content
                    print('\033[1;33mDown Loading ...... \033[0m\n\033[1;31m{}\n\033[0m'.format(fullurlname))
                    with open(local_path,'wb') as img:
                        img.write(response)
                    print('\033[1;35mWrite local success ......\033[0m\n\033[1;34m{}\n\n\033[0m'.format(local_path))
                except Exception as ee:
                    print(ee)
            else:
                print("\033[1;35mIt's already been downloaded ......\033[0m\n\033[1;32m{}\n\n\033[0m".format(local_path))




        return item
