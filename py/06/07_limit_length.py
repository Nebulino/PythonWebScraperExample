import scrapy
from scrapy.crawler import CrawlerProcess


class Spider(scrapy.spiders.SitemapSpider):
    name = 'spider'
    sitemap_urls = ['https://www.nasa.gov/sitemap.xml']

    def parse(self, response):
        print(response)


if __name__ == "__main__":
    process = CrawlerProcess({
        'LOG_LEVEL': 'INFO',
        'CLOSESPIDER_PAGECOUNT': 5
    })
    process.crawl(Spider)
    process.start()
