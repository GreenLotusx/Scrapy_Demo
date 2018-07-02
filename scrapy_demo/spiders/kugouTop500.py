from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scary_demo.items import kugouTop500Item
from scrapy.http import Request

class kugouTop500(CrawlSpider):
	name = 'kugou'			##定义爬虫名称
	start_urls = ['http://www.kugou.com/yy/rank/home/1-8888.html?from=rank']

	def parse(self,response):
		item = ScaryDemoItem()
		selector = Selector(response)
		infos = selector.xpath('//*[@class="pc_temp_songlist "]/ul/li')
		for info in infos:
			try:												##异常处理
				try:
					index = info.xpath('span[3]/strong/text()').extract()[0].strip()
				except Exception as e:
					index = info.xpath('span[3]/text()').extract()[0].strip()			##取指定数据
				songname = info.xpath('a/text()').extract()[0]
				time = info.xpath('span[4]/span/text()').extract()[0].strip()
				url = info.xpath('a/@href').extract()[0].strip()
				item['index'] = index
				item['songname'] = songname
				item['time'] = time
				item['url'] = url

				yield item
			except Exception as e:
				pass
																						##构建页面url
		urls = ['http://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(str(x)) 
			for x in range(2,24)]
		for url in urls:
			yield Request(url,callback=self.parse)