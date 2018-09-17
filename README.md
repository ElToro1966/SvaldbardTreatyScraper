# SvaldbardTreatyScraper
A Scrapy-project that finds static pages and news - in several languages - about the Svalbard Treaty

# Spiders

Usage: From folder /sts run:

regjeringen_no: scrapy crawl regjeringen_no -o output-file

regjeringen_no_search: scrapy crawl regjeringen_no_search -o output-file -a tag=tag

regjeringen_dk: scrapy crawl regjeringen_dk -o output-file

regjeringen_dk_search: scrapy crawl regjeringen_dk_search -o output-file -a tag=tag
