# -*- coding: utf-8 -*-
import scrapy


class Covid19Spider(scrapy.Spider):
    name = 'covid19'
    allowed_domains = ['www.worldometers.info/coronavirus']
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def parse(self, response):
        heading = response.xpath("//h1/text()").get()
        yield {
            "heading": heading,
        }
