# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScaryDemoPipeline(object):
	def process_item(self, item, spider):
		try:
			fp = open('C:/Users/Administrator/Desktop/ScrapyData.txt','a+')
			fp.write(item['index']+'\t')
			fp.write(item['songname']+'\t')
			fp.write(item['time']+'\t')
			fp.write(item['url']+'\t')
		except Exception as e:
			fp.write('\n')
			fp.write(item['fans']+'\t')
			fp.write(item['name']+'\t')
			fp.write(item['content']+'\t')
			fp.write(item['article']+'\t')
			fp.write('\n')
		return item
