import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class RegeringenDkSpider(CrawlSpider):
    '''Spider crawling the Danish Government's news pages'''
    name = 'regeringen_dk'
    allowed_domains = ['regeringen.dk']
    start_urls = ['https://www.regeringen.dk/nyheder/']

    rules = (
        # Extract links matching '*\/nyheder\/*' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=('*\/nyheder\/*', )), callback='parse_item'),
    )

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        item = scrapy.Item()
        item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        item['name'] = response.xpath('//td[@id="item_name"]/text()').extract()
        item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
        return item
