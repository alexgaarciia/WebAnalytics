import scrapy


class WebSpiderSpider(scrapy.Spider):
    name = "web_spider"
    allowed_domains = ["www.uc3m.es"]
    start_urls = ["https://www.uc3m.es/bachelor-degree/data-science"]

    def parse(self, response):
        pass
