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
        
        yield {
            'article_title': response.xpath('//section[@class="article-top"]/div/h1/text()').extract_first(),
            'article_date': response.xpath('//section[@class="article-top"]/div/div/time/text()').extract_first(),
            'article_type': response.xpath('//section[@class="article-top"]/div/div/span/text()').extract_first(),
            'article_lead': response.xpath('//article/p/text()').extract_first(),
            'article_text': ''.join(response.xpath('//article/p/text()').extract()),
        }
