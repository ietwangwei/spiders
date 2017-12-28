from scrapy.spiders import Spider
from scrapy.selector import Selector
from tutorial.items import Website
class DmozSpider(Spider):
    name = "jd"
    allowed_domains = ["jd.com"]
    start_urls = [
        "https://search.jd.com/Search?keyword=%E6%B4%97%E8%A1%A3%E6%9C%BA&enc=utf-8&wq=%E6%B4%97%E8%A1%A3%E6%9C%BA&pvid=38ba2cbb22c34be58a2a0976cdb6d49b"
    ]
    def parse(self, response):
        for sel in response.xpath('//div[@class="gl-i-wrap"]'):
            item = Website()#Website会生成相应的容器来装载抓取的数据
            price = sel.xpath("div[@class='p-price']//strong//i//text()")
            item["price"] = price.extract()#extract会把数据序列化
            bookName = sel.xpath("div[@class='p-name']//font//text()")
            item['description'] = bookName.extract()
            author = sel.xpath("div[@class='p-bookdetails']//a//text()")
            item['author'] = author.extract()
            yield item

