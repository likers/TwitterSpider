import scrapy
import json

from scrapy.selector import XmlXPathSelector
import lxml.etree as etree

class TwitterSpider(scrapy.Spider):
    name = "twitter"
    allowed_domains = ["twitter.com"]
    start_urls = [
        "https://twitter.com/taylorswift13/media"
    ]

    

    def parse(self, response):
        imgList = []

        for sel in response.xpath('//div[@class="AdaptiveMedia-photoContainer js-adaptive-photo "]'):
            imgurl = sel.xpath('img/@src').extract()
            imgList.append(imgurl)
        print len(imgList)  

        for sel in response.xpath('//ol[@class="stream-items js-navigable-stream"]'):
            itemIdArray = sel.xpath('li/@data-item-id').extract()

        print itemIdArray[-1]

        newUrl = "https://twitter.com/i/profiles/show/taylorswift13/media_timeline?include_available_features=1&include_entities=1&last_note_ts=26&max_position={maxId}&oldest_unread_id=0&reset_error_state=false".format(maxId=itemIdArray[-1])

        print newUrl

        yield scrapy.Request(newUrl, callback=self.parseJson)


    def parseJson(self, response):
        jsonresponse = json.loads(response.body_as_unicode())             

        # xml = dicttoxml.dicttoxml(json_dict)
        # xml = etree.fromstring(jsonresponse["items_html"])
        # #Apply scrapy's XmlXPathSelector module,and start using xpaths
        # xml = XmlXPathSelector(text=xml)
        # data = xml.select('.//div[@class="AdaptiveMedia-photoContainer js-adaptive-photo "]').extract()
        # print data
        print jsonresponse["items_html"]






