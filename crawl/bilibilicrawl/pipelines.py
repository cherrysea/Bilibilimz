# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymysql import connect

class BilibilicrawlPipeline:
    def __init__(self):
        # 连接
        self. conn = connect(host='192.168.153.131', port=3306, user='cherry', password='helloworld', database='helloworld', charset='utf8')
       # 添加游标
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # links=''
        # for link in item['image_urls']:
        #     links = links+link+','
        # if links[-1]==',':

        # 执行 sql
        self.cursor.execute('insert into jk(title, image_url) VALUES ("{}","{}")'.format(item['title'],item['image_urls']))
        # 提交 不然无法保存到数据库
        self.conn.commit()
        return item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()
        print("保存完毕！")
