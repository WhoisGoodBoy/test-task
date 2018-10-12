# -*- coding: utf-8 -*-
import scrapy
import csv
import random

def dataimp():
    testdata = []
    with open('result.csv', newline='') as File:  
        reader = csv.reader(File)
        for row in reader:
            testdata.extend(row) 
    t = random.sample(testdata, 250)
    t = [a + "?json" for a in t]
    #print (t)
    return t

class ExampleSpider(scrapy.Spider):
    name = "exampledownload"
    allowed_domains = ['e27.co']
    start_urls = dataimp()

    def parse(self, response):
        for item in response.xpath('//div[@class="container"]'):
            yield {
                'description_short': item.xpath('.//div[@class="portlet-body"]/p//text()').extract_first(),
                'location': item.xpath('.//div[@class="mbt"]/span[3]/a/text()').extract_first(),
                'tags': item.xpath('.//div[@style="word-wrap: break-word;"]/span//a/text()').extract_first(),
                'founding_date': item.xpath('.//p[contains(text(), "Founded:")]/following-sibling::span/text()').extract_first(),
                'request_company_url': item.xpath('.//div[@class="row"]//div[@class="mbt"]/span[1]/a/@href').extract_first(),
                #'description': item.xpath('.//div[@class="portlet-body"]/p/text()').extract_first(),
                'company_name': item.xpath('.//h1[@class="profile-startup"]/text()').extract_first()
            }



