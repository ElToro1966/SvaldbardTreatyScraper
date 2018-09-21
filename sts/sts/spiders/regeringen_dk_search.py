# -*- coding: utf-8 -*
import scrapy
import scrapy_splash


class RegeringenDkSearchSpider(scrapy.Spider):
    '''A spider to crawl the Danish Government's search pages.'''
    name = "regeringen_dk_search"

    def start_requests(self):
        url = 'https://www.regeringen.dk/soeg/?q='
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + tag
        yield scrapy_splash.SplashRequest(
            url=url, callback=self.parse, endpoint='render.html'
        )

    def parse(self, response):
        '''Parses the response downloaded for each of the requests made'''
        self.logger.info('Parse function called on %s', response.url)

        from scrapy.shell import inspect_response
        inspect_response(response, self)

        for href in response.css('li.ng-scope h4 a::attr(href)'):
            yield response.follow(href, callback=self.parse_article)

        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, callback=self.parse)

    def parse_article(self, response):
        '''Parse response for pages with a single article'''
        self.logger.info('Parse article function called on %s', response.url)

        yield {
            'article_title': self._extract_with_xpath('//ul/li[@class="ng-scope"]/h4/a/text()', response),
            #'article_date': self._extract_with_css("div.article-info span.date::text", response),
            #'article_type': self._extract_with_css("div.article-info span.type::text", response),
            #'article_lead': self._extract_with_css("div.article-ingress p::text", response),
            #'article_text': self._extract_with_css("div.article-body::text", response),
        }

    def _extract_with_xpath(self, query, response):
        return response.css(query).extract_first().strip()

