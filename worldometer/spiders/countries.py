# -*- coding: utf-8 -*-
import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/']

    def parse(self, response):
        countries_list = response.xpath("//td")
        for country in countries_list:
            name = country.xpath(".//a/text()").get()
            link = country.xpath(".//a/@href").get()
            absoute_url = response.urljoin(link)

            # yield {
            #     "name": name,
            #     "link": absoute_url,
            # }
            yield response.follow(url=link, callback=self.parse_country, meta={"name":name})

    def parse_country(self, response):
        name = response.request.meta['name']
        flag = response.xpath("//td//img/@src").get()
        flag_link = response.urljoin(flag)
        area = response.xpath("//tr[@id='places_area__row']//td/text()").get()
        yield {
            "name": name,
            "flag": flag_link,
            "area": area,
            }

