#### 1. 爬虫部分

bilibilicrawl 实现利用接口爬取妹子图片链接通过管道储存到数据库，接口见 `bilibilicrawl/spiders/bilibili.py`中`start_url`

运行：`cd bilibilicrawl`注意是含有`scrapy.cfg`文件的那一层

`scrapy crawl bilibili`

#### 2. 接口部分

框架：flask

详情见`main.py`即可