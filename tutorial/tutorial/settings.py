# Scrapy settings for tutorial project

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'
DEFAULT_ITEM_CLASS = 'tutorial.items.Website'

ITEM_PIPELINES = {'tutorial.pipelines.FilterWordsPipeline': 1}
FEED_EXPORT_ENCODING = 'utf-8' #保证抓取的字符为utf-8格式