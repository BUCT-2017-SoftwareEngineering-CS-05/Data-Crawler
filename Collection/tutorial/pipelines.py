# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class TutorialPipeline:
    def process_item(self, item, spider):
        return item


class savainDB:
    def open_spider(self, spider):
        self.connect = pymysql.connect(
            host='cdb-3lehih0k.cd.tencentcdb.com',
            port=10090,
            db='museum',
            user='CS1705museum',
            passwd='CS1705museum',
            charset='utf8',
            use_unicode=True
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                """select* from Collection where ophoto=%s""",
                item['pic'])
            repetition = self.cursor.fetchone()
            if repetition:
                pass
            else:
                self.cursor.execute(
                    """insert into Collection(midex,oname,ointro, ophoto)
                                                value (%s, %s, %s, %s)""",
                    (item['midx'],
                     item['name'],
                     item['text'],
                     item['pic'])
                )
                self.connect.commit()
        except Exception as error:
            print("error" + str(error))

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()