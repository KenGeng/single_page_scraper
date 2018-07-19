# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import os
import csv
from scrapy.exporters import JsonItemExporter

#
# class JsonExporterPipeline:
#     # 调用 scrapy 提供的 json exporter 导出 json 文件
#     def __init__(self):
#         base_dir = os.getcwd()
#         filename = base_dir + '/news2.json'
#         self.file = open(filename, 'wb+')
#         # 初始化 exporter 实例，执行输出的文件和编码
#         self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
#         # 开启倒数
#         self.exporter.start_exporting()
#
#     def close_spider(self, spider):
#         self.exporter.finish_exporting()
#         self.file.close()
#
#     # 将 Item 实例导出到 json 文件
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item


class SinglePageScraperPipeline(object):
    def process_item(self, item, spider):
        base_dir = os.getcwd()
        filename = base_dir + '/result.json'
        # 打开json文件，向里面以dumps的方式吸入数据
        # 注意需要有一个参数ensure_ascii=False ，不然数据会直接为utf编码的方式存入比如
        # :“/xe15”
        with codecs.open(filename, 'a') as f:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            f.write(line)
        return item


class PipelineToCSV(object):

    def __init__(self):
        # csv文件的位置
        store_file = os.path.dirname(__file__) + '/spiders/result.csv'
        flag=0
        if not os.path.isfile(store_file):
            flag = 1
        # 打开(创建)文件

        self.file = open(store_file, 'a+')
        # csv写法
        self.writer = csv.writer(self.file)
        if flag == 1:
            self.writer.writerow(('id','claim', 'rating', 'image_url', 'permalink', 'publish_date'))

    def process_item(self, item, spider):
        # 判断字段值不为空再写入文件
        self.writer.writerow(
            (item['id'], item['claim'], item['rating'], item['image_url'], item['permalink'], item['publish_date']))
        return item
