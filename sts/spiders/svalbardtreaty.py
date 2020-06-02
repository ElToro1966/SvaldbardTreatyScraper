# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class SvalbardtreatySpider(CrawlSpider):
    name = 'svalbardtreaty'
    allowed_domains = ['thebarentsobserver.com',
            'uio.no',
            'unis.no',
            'arctic-council.org',
            'arctictoday.com',
            'npolar.no',
            'sysselmannen.no',
            ]
    start_urls = ['https://thebarentsobserver.com/en',
            'https://www.uio.no/english/research/interfaculty-research-areas/high-north/research/',
            'https://www.unis.no/news/',
            'https://www.arctic-council.org/index.php/en/',
            'https://www.arctictoday.com',
            'http://www.npolar.no/en/',
            'https://www.sysselmannen.no/en/',
            ]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        print('Processing..' + response.url)
