import scrapy
from crawler.items import CrawlerItem


class Spider(scrapy.Spider):


    name = "mark1spider2"


    def start_requests(self):
        for number in range(1, 4382):
            url = 'http://markinfo.co.kr/front/phtml/c1200_r.php?p={}&trademark_name=&classsification=&asign_product=&application_number=&register_number=&publication_number=&international_register_number=&application_date=&register_date=&publication_date=&priority_date=&international_register_date=&applicant_name=&agent_name=&vienna_cd=&reg_privilege_name=&similarity_code=G5206%2BN16004&application_date1=&application_date2=&abandonment=true&application=true&cancel=true&expiration=true&publication=true&refused=true&registration=true&withdrawal=true&trademark=true&service_mark=true&business_emblem=true&collective_mark=true&geo_org_mark=true&trademark_service_mark=true&cert_mark=true&geo_cert_mark=true&international_mark=true&character=true&figure=true&composition_character=true&figure_composition=true&fragrance=true&sound=true&color=true&color_mixed=true&dimension=true&hologram=true&invisible=true&motion=true&visual=true&act=search&expiration_all=&mark_upclass_cd=8&mark_subclass_cd=143&sort_spec=AD&desc_sort=true'\
            .format(number)
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        f = open("./books.csv", mode='a', encoding='utf-8')
        trademarks = response.xpath('//*[@id="container"]/ul')
        for trademark in trademarks:
            items_row = trademark.xpath('./li')
            for each in items_row:
                f.write(each.xpath('./a/p[1]/text()').extract()[0].replace('\n','').replace('\t','') + ',')
                f.write(each.xpath('./a/span/img/@src').extract()[0] + ',')
                f.write(each.xpath('./a/p[1]/span/text()')[0].extract().replace('\n','').replace('\t','') + ',')
                f.write(each.xpath('./a/p[3]/text()')[0].extract().replace('\n','').replace('\t','') + ',\n')
        f.close()
