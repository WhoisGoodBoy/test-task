# -*- coding: utf-8 -*-
import scrapy

class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ['e27.co']
    start_urls = ['https://e27.co/search/startups/?json&page=1']

    def parse(self, response):
        for item in response.xpath('//div[@class="pos-rel"]'):
            yield {
                'url': item.xpath('./a/@href').extract_first()
            }
        next_page = response.xpath('//div[@class="pagination"]/div[@class="btn-group"][a/button[text()="Next "]]/a/@href').extract_first().replace("https://e27.co/search/startups/?all&amp;per_page=", "https://e27.co/search/startups/?json&page=")
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

