# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class SvalbardtreatySpider(scrapy.Spider):
    name = 'svalbardtreaty'
    allowed_domains = ['thebarentsobserver.com',
            'https://www.uio.no',
            'https://www.unis.no',
            'https://www.arctic-council.org',
            'https://www.arctictoday.com',
            'http://www.npolar.no',
            ]
    start_urls = ['https://thebarentsobserver.com/en',
            'https://www.uio.no/english/research/interfaculty-research-areas/high-north/research/',
            'https://www.unis.no/news/',
            'https://www.arctic-council.org/index.php/en/',
            'https://www.arctictoday.com',
            'http://www.npolar.no/en/',
            ]

    def parse(self, response):
        pass
