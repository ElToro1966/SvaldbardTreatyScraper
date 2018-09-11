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
            'https://www.regjeringen.no/no/sok/id86008/?sortby=1&term=Svalbardtraktaten',
            'https://www.regjeringen.no/no/sok/id86008/?sortby=1&term=Svalbardtraktaten&page=2',
            'https://www.regjeringen.no/no/sok/id86008/?sortby=1&term=Svalbardtraktaten&page=3',
            'https://www.regjeringen.no/no/sok/id86008/?sortby=1&term=Svalbardtraktaten&page=4',
            'https://www.regjeringen.no/no/sok/id86008/?sortby=1&term=Svalbardtraktaten&page=5',
            'https://www.regjeringen.no/no/sok/id86008/?sortby=1&term=Svalbardtraktaten&page=6',
            'https://www.regjeringen.no/no/dokumentarkiv/id115322/?sortby=1&isfilteropen=True&term=Svalbardtraktaten',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        '''Handles the response downloaded for each of the requests made'''
        self._save_response_to_html(response)
        for article in response.css("ul.listing"):
            title = article.css("h2.title a::text").extract_first()


    def _save_response_to_html(self, response):        
        self.count = self.count + 1
        filename = 'response/regjeringen_no-%s.html' % str(self.count)
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


