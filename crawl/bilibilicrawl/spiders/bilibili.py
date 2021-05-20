import scrapy
import json
from bilibilicrawl.items import BilibilicrawlItem

class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['api.vc.bilibili.com']
    start_urls = ['http://api.vc.bilibili.com/']
    # start_urls = [
    #     'https://api.vc.bilibili.com/link_draw/v2/Photo/list?category=sifu&type=new&page_num={}&page_size=20'.format(i)
    #     for i in range(600)]
    # start_urls = ['https://api.vc.bilibili.com/link_draw/v2/Photo/list?category=sifu&type=new&page_num=1&page_size=20']
    start_urls = [
        'https://api.vc.bilibili.com/link_draw/v2/Photo/list?category=sifu&type=new&page_num={}&page_size=20'.format(i)
        for i in range(15)]

    def parse(self, response):
        for item in json.loads(response.text)['data']['items']:
            yield response.follow(
                'https://api.vc.bilibili.com/link_draw/v1/doc/detail?doc_id=' + str(item['item']['doc_id']),
                meta={'image_urls': [picture['img_src'] for picture in item['item']['pictures']]},
                callback=self.parse_jk,
            )

    def parse_jk(self, response):
        item = json.loads(response.text)['data']['item']
        title = item['title']
        tags = [tag['tag'] for tag in item['tags']]
        description = item['description']
        if any('jk' in i.lower() for i in (title, *tags, description)):
            jk = BilibilicrawlItem()
            jk['title'] = title
            jk['image_urls'] = response.meta['image_urls']
            yield jk
