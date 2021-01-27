from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem, NathomeItem


class HellobearComHk(BasePortiaSpider):
    name = "www.hellobear.com.hk"
    allowed_domains = ['www.hellobear.com.hk']
    start_urls = ['https://www.hellobear.com.hk/']
    rules = [
        Rule(
            LinkExtractor(
                allow=('.*'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [
        [
            Item(
                NathomeItem,
                None,
                '.pd-box',
                [
                    Field(
                        'name',
                        'div:nth-child(2) > .ProductDetail-product > .ProductDetail-product-info > .box-default > .Product-title *::text',
                        []),
                    Field(
                        'price',
                        'div:nth-child(2) > .ProductDetail-product > .ProductDetail-product-info > .box-default > .product-detail-actions > .not-same-price > .price-box > .global-primary *::text',
                        []),
                    Field(
                        'desc',
                        '.ProductDetail-additionalInfo > .col-xs-12 > .Tabset > .active > .ProductDetail-description *::text',
                        [])])]]
