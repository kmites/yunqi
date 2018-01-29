# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class BookInfoItem(scrapy.Item):
    # id
    id = Field()
    #  书名
    name = Field()
    # 链接
    link = Field()
    # 作者
    author = Field()
    #  分类
    type = Field()
    # 状态
    status = Field()
    # 更新时间
    update_time =Field()
    # 字数
    words = Field()
    # 简介
    summary = Field()

class BookHotItem(scrapy.Item):
    # id
    id = Field()
    # 名字
    name = Field()
    # 类型
    type = Field()
    # 总点击
    all_click = Field()
    # 月点击
    month_click = Field()
    # 周点击
    week_click = Field()
    # 总人气
    all_popular = Field()
    # 月人气
    month_popular = Field()
    # 周人气
    week_popular = Field()
    # 总推荐
    all_commend = Field()
    # 月推荐
    month_commend = Field()
    # 周推荐
    week_commend = Field()
    # 总字数
    all_words = Field()
    # 评论
    comment = Field()
    # 状态
    status = Field()