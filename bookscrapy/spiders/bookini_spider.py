import scrapy
from bookscrapy.items import EbookItem

HOST = 'http://www.bookini.pl/'

class BookiniSpider(scrapy.Spider):
    name = "bookini"
    allowed_domains = ["bookini.pl"]
    start_urls = [HOST + 'index.php?t=authors&p=a']

    def parse(self, response):
        others = response.xpath('//a[contains(@href, "index.php?t=authors&")]/@href').extract()
        for other in others:
            yield scrapy.Request(HOST + other.encode('iso-8859-2', 'xmlcharrefreplace'), callback=self.do_authors)

    def do_authors(self, response):
        authors = set(response.xpath('//a[contains(@href, "index.php?t=ebooks&author=")]/@href').extract())
        for author in authors:
            author = author.encode('iso-8859-2', 'xmlcharrefreplace')
            yield scrapy.Request(HOST + author, callback=self.do_author)

    def do_author(self, response):
        entries = response.xpath('//center/table[@id="AutoNumber4"]/tr')
        if len(entries) < 1:
            pass

        for entry in entries:
            author, title, _, _ = entry.xpath('td/p/text()').extract()
            url = HOST + entry.xpath('td/p/a/@href').extract()[0]
            item = EbookItem()
            item['title'] = title
            item['author'] = author
            item['link'] = url
            yield item
