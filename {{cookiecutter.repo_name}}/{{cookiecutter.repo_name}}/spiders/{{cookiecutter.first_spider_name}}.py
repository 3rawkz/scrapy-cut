_author_ = 'Erick'
# -*- coding: utf-8 -*-
import scrapy


class VidspiSpider(scrapy.Spider):
    name = "{{cookiecutter.first_spider_name}}"
    allowed_domains = ["pyvideo.org"]
    start_urls = ['http://pyvideo.org/tags.html']

    def parse(self, response):
        for href in response.css('#element-list a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(href),
                                 callback=self.parse_mainsrc)

    def parse_mainsrc(self, response):
        for href in response.css('.entry-title a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(href),
                                 callback=self.parse_main)
    def parse_main(self, response):
        yield {
            'name': "{{cookiecutter.item_name_selector}}",
            'event': "{{cookiecutter.item_event_selector}}",
            'vidurl': "{{cookiecutter.item_vidurl_selector}}",
            'tags': "{{cookiecutter.item_tags_selector}}",
            }
