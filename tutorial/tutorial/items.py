from scrapy.item import Item, Field
class Website(Item):
    description = Field()
    price = Field()
    author = Field()

#生成相应的容器