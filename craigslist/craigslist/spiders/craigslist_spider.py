from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

import scrapy

# item models
from craigslist.items import CraigslistItem

class CraigslistSpider(CrawlSpider):

	name = "craigslist"
	allowed_domains = ["craigslist.org"]
	start_urls = [
	    "https://sfbay.craigslist.org/search/sss?query=rv",
	    "http://houston.craigslist.org/search/sss?sort=rel&query=rv"
	]

	rules = (
		Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@class="button next"]',)), callback = "parse_search", follow = True),
	)


	def parse_search(self, response):

		for sel in response.xpath("//p[@class='row']"):

			item = CraigslistItem()
			item['title'] = sel.xpath("span[@class='txt']/span[@class='pl']/a[@class='hdrlnk']/text()").extract()
			item['price'] = sel.xpath("span[@class='txt']/span[@class='l2']/span[@class='price']/text()").extract()
			yield item