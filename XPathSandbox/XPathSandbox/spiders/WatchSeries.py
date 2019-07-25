# -*- coding: utf-8 -*-
import scrapy


class WatchseriesSpider(scrapy.Spider):
    name = 'WatchSeries'
    allowed_domains = ['watch-series']
    start_urls = ['http://https://www3.watch-series.live//']

    def parse(self, response):
        wsLister = response.css('.category-videos')
        for wsL in wsLister:
            wsHref  = wsL.css('.sdimg a::attr("href")').extract_first()
            wsTitle = wsL.css('.home_video_title::text').extract_first()
