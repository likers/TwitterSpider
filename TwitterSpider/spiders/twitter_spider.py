import scrapy
import json
import re
from TwitterSpider.items import TwitterspiderItem
from lxml import etree

class TwitterSpider(scrapy.Spider):
    name = "twitter"
    allowed_domains = ["twitter.com"]
    start_urls = [
        "https://twitter.com/taylorswift13/media"
    ]
    counter = 0
    imgList = []

    def parse(self, response):
        

        for sel in response.xpath('//div[@class="AdaptiveMedia-photoContainer js-adaptive-photo "]'):
            imgurl = sel.xpath('img/@src').extract()
            self.imgList.append(imgurl)
        print len(self.imgList) 
        # print self.imgList  

        for sel in response.xpath('//ol[@class="stream-items js-navigable-stream"]'):
            itemIdArray = sel.xpath('li/@data-item-id').extract()

        print itemIdArray[-1]

        newUrl = "https://twitter.com/i/profiles/show/taylorswift13/media_timeline?include_available_features=1&include_entities=1&last_note_ts=26&max_position={maxId}&oldest_unread_id=0&reset_error_state=false".format(maxId=itemIdArray[-1])

        print newUrl

        yield scrapy.Request(newUrl, callback=self.parseJson)


    def parseJson(self, response):
        self.counter += 1
        if self.counter < 5:
            jsonresponse = json.loads(response.body_as_unicode())             
        
            for url in re.findall(r'https:\/\/pbs.twimg.com\/media\/[A-Za-z0-9_]+.jpg', jsonresponse["items_html"]):
                self.imgList.append([unicode(url)])


            # print self.imgList
            print len(self.imgList)

            for url in self.imgList:
                # print url
                item = TwitterspiderItem()
                item['image_urls'] = url
                yield item
    







