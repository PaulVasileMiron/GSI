import scrapy
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from Covid.items import CovidItem

class CovidSpider(Spider):
    name = "CoviSpider"
    start_urls=["https://elpais.com/sociedad/2020/03/30/actualidad/1585589827_546714.html"]
    def parse(self,response):
        sel = Selector(response)
        preguntas= sel.xpath('//*[@id="tableEurope"]/div')
        for i, elem in enumerate(preguntas):
            item = ItemLoader(CovidItem(),elem)
            item.add_xpath('pregunta','.//div[2]/div[1]/div/textContent()')
            item.add_value('id',i)
            yield item.load_item()

