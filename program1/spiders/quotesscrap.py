import scrapy

class QuoteSpider(scrapy.Spider):
    name='quote'
    start_urls= [
        'http://www.wikicfp.com/cfp/'
    ]

    def parse(self,response):
        title = response.css('title').extract()
        yield {'titletext': title}

        """extra line"""