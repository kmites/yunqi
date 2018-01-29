# -*- coding: utf-8 -*-
import scrapy
from ..items import BookInfoItem,BookHotItem
from scrapy_redis.spiders import RedisSpider

class YunqiSpider(RedisSpider):
    name = 'book'
    allowed_domains = ['yunqi.qq.com']

    # start_urls = ['http://yunqi.qq.com/bk/so2/n10p1880']

    def parse(self, response):
        book_infos = response.xpath("//div[@class='book']/div[@class='book_info']")

        for book_info in book_infos:

            item = BookInfoItem()

            item['id'] = book_info.xpath("./h3/a/@id").extract_first()
            item['link'] = book_info.xpath("./h3/a/@href").extract_first()
            item['name'] = book_info.xpath("./h3/a/text()").extract_first()
            item['author']= book_info.xpath("./dl[1]/dd[1]/a/text()").extract_first()
            item['type'] = book_info.xpath("./dl[1]/dd[2]/a/text()").extract_first()
            item['status'] = book_info.xpath("./dl[1]/dd[3]/text()").extract_first()
            item['update_time'] = book_info.xpath("./dl[2]/dd[1]/text()").extract_first()
            item['words'] = book_info.xpath("./dl[2]/dd[2]/text()").extract_first()
            item['summary'] = book_info.xpath("./dl[3]/dd[@id='introCut']//text()").extract_first()
            print(item)
            yield item

            book_hot_request = scrapy.Request(item['link'],callback=self.book_hot_parse)
            book_hot_request.meta['id'] = item['id']

            yield  book_hot_request

        next_page_url = response.xpath("//div[@id='pageHtml2']/a[last()]/@href").extract_first()

        if next_page_url:
            print(next_page_url)
            yield scrapy.Request(url= next_page_url, callback=self.parse)

    def book_hot_parse(self,response):

        item = BookHotItem()

        item['id'] = response.meta['id']

        item['name'] = response.xpath("//div[@class='main1']/div[@class ='title']/a/@title").extract_first()
        item['type'] = response.xpath("//div[@class='main2']//div[@class='title']/a[3]/text()").extract_first()

        item['all_click'] = response.xpath("//div[@id='novelInfo']//tr[2]//td[1]/text()").extract_first()
        item['all_popular'] = response.xpath("//div[@id='novelInfo']//tr[2]//td[2]/text()").extract_first()
        item['all_commend'] = response.xpath("//div[@id='novelInfo']//tr[2]//td[3]/text()").extract_first()

        item['month_click'] = response.xpath("//div[@id='novelInfo']//tr[3]/td[1]/text()").extract_first()
        item['month_popular'] = response.xpath("//div[@id='novelInfo']//tr[3]//td[2]/text()").extract_first()
        item['month_commend'] = response.xpath("//div[@id='novelInfo']//tr[3]//td[3]/text()").extract_first()

        item['week_click'] = response.xpath("//div[@id='novelInfo']//tr[4]//td[1]/text()").extract_first()
        item['week_popular'] = response.xpath("//div[@id='novelInfo']//tr[4]//td[2]/text()").extract_first()
        item['week_commend'] = response.xpath("//div[@id='novelInfo']//tr[4]//td[3]/text()").extract_first()

        item['all_words'] = response.xpath("//div[@id='novelInfo']//tr[5]//td[1]/text()").extract_first()
        item['comment'] = response.xpath("//div[@id='novelInfo']//tr[5]//td[2]/text()").extract_first()
        item['status'] = response.xpath("//div[@id='novelInfo']//tr[5]//td[3]/text()").extract_first()

        yield item