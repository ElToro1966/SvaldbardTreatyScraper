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
        Rule(LinkExtractor(allow=('[a-z]+\/nyheder\/[a-z]+', )), callback='parse_item'),
    )

    def parse_item(self, response):
        self.logger.info('This is a Danish Government news page! %s', response.url)
        item = scrapy.Item()
        item['title'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        item['date'] = response.xpath('//td[@id="item_name"]/text()').extract()
        item['category'] = response.xpath('//td[@id="item_description"]/text()').extract()
        # Add item-text, second to last sections of article-tag
        return item
