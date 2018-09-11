# -*- coding: utf-8 -*
import scrapy

class RegjeringenNoSpider(scrapy.Spider):
    '''A spider to crawl the Norwegian Government's pages covering the Treaty of Svalbard'''
    name = "regjeringen_no"
    count = 0
    #rules = (
    #    Rule(LinkExtractor(allow='regjeringen\.no\/no\/[a-z_/]+$'),
    #        'parse_category', follow=True,
    #    ),
    #)

    def start_requests(self):
        '''Returns an iterable of Requests which the Spider will begin to crawl from'''
        urls = [
            'https://www.regjeringen.no/no/aktuelt/taler_artikler/',
            'https://www.regjeringen.no/no/aktuelt/nyheter/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        '''Parses the response downloaded for each of the requests made'''
        for article in response.css("ul.listing"):
            yield {
                'article_title': article.css("h2.title a::text").extract_first(),
                'article_date': article.css("div.info span.date::text").extract_first(),
                'article_type': article.css("div.info span.type::text").extract_first(),
                'article_text': article.css("p.excerpts::text").extract_first(),
            }

