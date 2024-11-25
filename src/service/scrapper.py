import scrapy
from bs4 import BeautifulSoup


class StockScraper(scrapy.Spider):
    name: str = "stocks"
    allowed_domains = ["marketwatch.com"]

    def start_requests(self):
        headers = {
            'Accept': ['text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'],
            "Accept-Language": "en-US,en;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        }

        stock_url: str = "https://www.marketwatch.com/investing/stock/aapl"
        yield scrapy.Request(url=stock_url, headers=headers, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.body)

        print(soup)
