# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# from scrapy.pipelines.images import ImagesPipeline

from scrapy.pipelines.images import ImagesPipeline

class TwitterspiderPipeline(ImagesPipeline):
    def process_item(self, item, spider):
    	# item = TwitterspiderItem()
		
        return item
