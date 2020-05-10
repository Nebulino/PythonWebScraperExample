from scrapy.crawler import CrawlerProcess
from wikipedia.spiders import WikipediaSpider

if __name__ == "__main__":
    process = CrawlerProcess({
        'LOG_LEVEL': 'ERROR',
        'DEPTH_LIMIT': 1
    })

    process.crawl(WikipediaSpider)
    spider = next(iter(process.crawlers)).spider
    process.start()

    print("-" * 60)

    for pm in spider.linked_pages:
        print(pm.depth, pm.title, pm.child_title)
