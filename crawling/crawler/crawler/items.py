import scrapy


class CrawlerItem(scrapy.Item):
    # data : 출원일
    # mark_status : 출원, 거절, 등록 등의 현재 상표 상태
    # mark_class : 상품 분류
    date = scrapy.Field()
    mark_status = scrapy.Field()
    mark_class = scrapy.Field()
