import scrapy


class YellowPageDentist(scrapy.Spider):
    name = "yellow_page_dentist"
    start_urls = ["https://www.yellowpages.com/search?search_terms=dentist&geo_location_terms=California%2C+MD"]

    def parse(self, response):
        print('Parsing: ', response.url)
        item=dict(
            text=response.text
        )
        print("item",item)
        yield item
