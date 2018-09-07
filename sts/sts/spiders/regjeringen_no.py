# -*- coding: utf-8 -*
import scrapy


class RegjeringenNoSpider(scrapy.Spider):
    name = "regjeringen_no"
    count = 0

    def start_requests(self):
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
        self.count = self.count + 1
        filename = 'response/regjeringen_no-%s.html' % str(self.count)
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
