import scrapy
from bookscrapy.items import EbookItem

class AbitelSpider(scrapy.Spider):
    name = "abitel"
    allowed_domains = ["abitel.gsm.pl"]

    patt='http://ebooki.abitel.gsm.pl/index.php?option=com_booklibrary&task=showCategory&catid=52&Itemid=509&limitstart='
    start_urls = [patt+str(start) for start in xrange(0,2701,90)]


    def parse(self, response):
        rows = response.xpath('//div[@id="list"]/table/tr')
        for tr in rows[1:91]:

            tdatexts = tr.xpath('td/a/text()')
            tdahrefs = tr.xpath('td/a/@href')
            tdtexts = tr.xpath('td/text()')
            if len(tdatexts)<1 or len(tdahrefs)<1 or len(tdtexts)<4:
                continue
            url = tdahrefs[0].extract()

            def go_inside(response):
                rows = response.xpath('//div[@id="inside3"]/table')[0].xpath('tr')
                title = rows[0].xpath('td/text()')[2].extract().strip()
                author = rows[2].xpath('td/text()')[2].extract().strip()
                relative = response.xpath('//a[@id="pobranie"]/@href').extract()[0]
                url = 'http://ebooki.abitel.gsm.pl/' + relative
                item = EbookItem()
                item['title'] = title
                item['author'] = author
                item['link'] = url
                yield item

            yield scrapy.Request(url, callback=go_inside)
