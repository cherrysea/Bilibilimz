import json
import random
from pymysql import connect

class SetuItem(object):
    def __init__(self):
        self.conn = connect(host='192.168.153.131', port=3306, user='cherry', password='helloworld', database="helloworld", charset='utf8')
        self.cursor = self.conn.cursor()

    def get_setus(self):
        sql = '''
            SELECT * FROM jk;
        '''
        try:
            self.cursor.execute(sql)
            items = self.cursor.fetchall()
        except Exception as e:
            print('出错了：', e)
            return -1
        else:
            result = []
            data = {}
            for item in items:
                data['title'] = item[1]
                data['links'] = item[2]
                result.append(data.copy())
            return result

    def get_setu(self):
        sql = '''
                    SELECT image_url FROM jk;
                '''
        try:
            self.cursor.execute(sql)
            items = self.cursor.fetchall()
        except Exception as e:
            print("出错了：", e)
            return -1
        else:
            # random.seed()
            item = items[random.randint(0, len(items)-1)]
            links = eval(item[0])
            # print(list(eval(item[0])))
            link = links[random.randint(0, len(links)-1)]
            return link

    def close(self):
        self.cursor.close()
        self.conn.close()
        print("执行完毕，数据库已关闭！")