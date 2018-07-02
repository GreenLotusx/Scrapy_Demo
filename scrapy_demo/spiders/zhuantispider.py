from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scary_demo.items import zhuantiItem
from scrapy.http import Request

class jianshuZhuanti(CrawlSpider):
	name = 'zhuanti'			##定义爬虫名称
	start_urls = ['http://www.jianshu.com/recommendations/collections?page=1&order_by=hot']

	def parse(self,response):
		item = zhuantiItem()
		selector = Selector(response)
		infos = selector.xpath('//*[@class="col-xs-8"]')
		for info in infos:
			try:							##异常处理包裹取指定数据
				name = info.xpath('div/a/h4/text()').extract()[0]
				content = info.xpath('div/a/p/text()').extract()[0]
				article = info.xpath('div/div/a/text()').extract()[0]
				fans = info.xpath('div/div/text()').extract()[0]
			except Exception as e:
				pass
			item['name'] = name
			item['content'] = content
			item['article'] = article
			item['fans'] = fans

			yield item
		urls = ['http://www.jianshu.com/recommendations/collections?page={}&order_by=hot'.format(str(x))			##构建页面url
			for x in range(2,39)]
		for url in urls:
			yield Request(url,callback=self.parse)