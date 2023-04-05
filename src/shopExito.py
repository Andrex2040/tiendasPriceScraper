from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import Spider

class Producto(Item):
    nombre = Field()
    descripcion = Field()
    precio = Field()

class Exito(Spider):
    name = "Productos"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
    }

    start_urls = ['https://www.exito.com/licores?_q=licores&map=ft']

    # download_delay = 2

    #rules = (
    #   Rule(
    #        LinkExtractor(
    #            allow=r'/licores'
    #        ), follow=True
    #    )
    #)

    def parse(self, response):
        selector = Selector(response)
        productos = selector.xpath('//div[@id="gallery-layout-container"]//div[@class="pointer pt3 pb4 flex flex-column h-100"]')

        for producto in productos:
            item = ItemLoader(Producto(), producto)
            item.add_xpath('descripcion', 'hola')
            item.add_xpath('precio', 'hola')
            item.add_xpath('nombre', './/div[@ class ="vtex-flex-layout-0-x-flexRow vtex-flex-layout-0-x-flexRow--product-info-container"]//div//div[@ class ="vtex-flex-layout-0-x-flexColChild vtex-flex-layout-0-x-flexColChild--product-info pb0"]//div//div//div[@ class ="pr0 items-stretch vtex-flex-layout-0-x-stretchChildrenWidth   flex"]//div[@ class ="vtex-product-summary-2-x-productBrandContainer"]//span[@class="vtex-product-summary-2-x-productBrandName"]//text()')
            #item.add_xpath('nombre', './/div[@class="vtex-product-summary-2-x-productBrandContainer"]//text()')
            #item.add_xpath('nombre',
                          # './/div[@class="vtex-flex-layout-0-x-flexRow vtex-flex-layout-0-x-flexRow--product-info-container"]//div//div//div//div//div//div//div[@class="vtex-product-summary-2-x-productBrandContainer"]//text()')
            yield item.load_item()