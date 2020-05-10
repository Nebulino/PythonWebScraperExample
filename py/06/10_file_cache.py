import scrapy
from scrapy.crawler import CrawlerProcess


class Spider(scrapy.spiders.SitemapSpider):
    name = 'spider'
    sitemap_urls = ['https://www.nasa.gov/sitemap.xml']

    def parse(self, response):
        print(response)


if __name__ == "__main__":
    process = CrawlerProcess({
        'LOG_LEVEL': 'CRITICAL',
        'CLOSESPIDER_PAGECOUNT': 500,
        'HTTPCACHE_ENABLED': True,
        'HTTPCACHE_DIR': "."
    })
    process.crawl(Spider)
    process.start()
