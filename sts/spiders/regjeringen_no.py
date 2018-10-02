# -*- coding: utf-8 -*
import scrapy

class RegjeringenNoSpider(scrapy.Spider):
    '''A spider to crawl the Norwegian Government's pages containing news, speeches and opinions'''
    name = "regjeringen_no"
    start_urls = [
        'https://www.regjeringen.no/no/aktuelt/taler_artikler/',
        'https://www.regjeringen.no/no/aktuelt/nyheter/',
    ]

    def parse(self, response):
        '''Parses the response downloaded for each of the requests made. Some
        contracts are mingled with this docstring.

        @url https://www.regjeringen.no/no/aktuelt/nyheter/
        @returns requests 1 
        '''

        self.logger.info('Parse function called on %s', response.url)

        for href in response.css('li.listItem h2.title a::attr(href)'):
            yield response.follow(href, callback=self.parse_article)

        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, callback=self.parse)
    
    def parse_article(self, response):
        '''Parse response for pages with a single article'''
        self.logger.info('Parse article function called on %s', response.url)

        yield {
            'article_title': self._extract_with_css("header.article-header h1::text", response),
            'article_date': self._extract_with_css("div.article-info span.date::text", response),
            'article_type': self._extract_with_css("div.article-info span.type::text", response),
            'article_lead': self._extract_with_css("div.article-ingress p::text", response),
            'article_text': self._extract_with_css("div.article-body::text", response),
        }

    def _extract_with_css(self, query, response):
        return response.css(query).extract_first().strip()
