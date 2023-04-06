import os
import scrapy
import math
import random


class SupermercadoSpider(scrapy.Spider):
    name = "supermercado"
    base_url = "https://www.olimpica.com/supermercado/licores?map=category-1,categoria"
    # Inicializa page_number leyendo el archivo "last_page.txt" o asignando 1 si el archivo no existe.
    page_number = int(open("last_page.txt", "r").read().strip()) if os.path.exists("last_page.txt") else 1
    start_urls = [f"{base_url}&page={page_number}"]
    products_per_page = 8

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, headers={'User-Agent': self.get_random_user_agent()})

    def parse(self, response):
        elementos = response.css("div.vtex-search-result-3-x-galleryItem.vtex-search-result-3-x-galleryItem--normal.vtex-search-result-3-x-galleryItem--grid-3.pa4")
        
        if not elementos:
            return

        for elemento in elementos:
            nombre = elemento.css("span.vtex-product-summary-2-x-productBrand.vtex-product-summary-2-x-brandName.t-body::text").get().strip()
            precio_container = elemento.css("div.false.olimpica-dinamic-flags-0-x-listPrices")
            precio = precio_container.xpath(".//span[contains(@class, 'olimpica-dinamic-flags-0-x-currency')]/text()").getall()
            precio = "".join([x.strip() for x in precio])

            yield {
                "Nombre": nombre,
                "Precio": precio
            }

        total_products = int(response.css("div.vtex-search-result-3-x-totalProducts--layout span::text").get().strip())
        print(total_products)
        total_pages = math.ceil(total_products / self.products_per_page)
        
        if self.page_number < total_pages:
            self.page_number += 1
            next_page = f"{self.base_url}&page={self.page_number}"
            yield scrapy.Request(next_page, callback=self.parse, headers={'User-Agent': self.get_random_user_agent()})
            with open("last_page.txt", "w") as f:
                f.write(str(self.page_number))

    def get_random_user_agent(self):
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15"
        ]
        return random.choice(user_agents)
