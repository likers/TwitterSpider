import scrapy

class TwitterSpider(scrapy.Spider):
    name = "twitter"
    allowed_domains = ["twiter.com"]
    start_urls = [
        "https://twitter.com/safekorea_____/media"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="AdaptiveMedia-photoContainer js-adaptive-photo "]'):
        # for sel in response.xpath('//div[@id="page-outer"]'):

            imgurl = sel.xpath('img/@src').extract()
            print imgurl
            # print sel.extract()