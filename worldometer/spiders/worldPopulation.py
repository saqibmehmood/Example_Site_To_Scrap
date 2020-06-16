# -*- coding: utf-8 -*-
import scrapy


class WorldpopulationSpider(scrapy.Spider):
    name = 'worldPopulation'
    allowed_domains = ['www.worldometers.info/world-population/']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country']

    def parse(self, response):
        countries = response.xpath("//tbody//tr")
        for country in countries:
            name = country.xpath(".//a/text()").get()
            population = country.xpath("(.//td/text())[2]").get()
            area = country.xpath("(.//td/text())[6]").get()

            yield {
                "name": name,
                "population": population,
                "area": area,
            }

