import scrapy
import json
import re
from TwitterSpider.items import TwitterspiderItem
from lxml import etree

class TwitterSpider(scrapy.Spider):

    twitterName = raw_input("Please input the twitter id:")
    print twitterName
    name = "twitter"
    allowed_domains = ["twitter.com"]
    start_urls = [
        "https://twitter.com/{name}/media".format(name = twitterName)
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

        newUrl = "https://twitter.com/i/profiles/show/{name}/media_timeline?include_available_features=1&include_entities=1&last_note_ts=26&max_position={maxId}&oldest_unread_id=0&reset_error_state=false".format(name = twitterName, maxId=itemIdArray[-1])

        # print newUrl

        yield scrapy.Request(newUrl, callback=self.parseJson)


    def parseJson(self, response):
        self.counter += 1
        print self.counter
        currentList = []
        itemIdArray = []
        jsonresponse = json.loads(response.body_as_unicode())
        if jsonresponse["min_position"] is not None:
                         
            for url in re.findall(r'src=\"https:\/\/pbs.twimg.com\/media\/[A-Za-z0-9_]+.jpg', jsonresponse["items_html"]):
                currentList.append([unicode(url[5:])])
                # print url[5:]

            for itemId in re.findall(r'data-item-id=\"[0-9]+', jsonresponse["items_html"]):
                itemIdArray.append(itemId[14:])
                # print itemId[14:]
            newUrl = "https://twitter.com/i/profiles/show/{name}/media_timeline?include_available_features=1&include_entities=1&last_note_ts=26&max_position={maxId}&oldest_unread_id=0&reset_error_state=false".format(name = twitterName, maxId=itemIdArray[-1])

            for url in currentList:
                # print url
                item = TwitterspiderItem()
                item['image_urls'] = url
                yield item

            yield scrapy.Request(newUrl, callback=self.parseJson)
            # print newUrl
            

            
    







