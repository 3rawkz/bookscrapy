import scrapy

class EbookItem(scrapy.Item):
    author = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
