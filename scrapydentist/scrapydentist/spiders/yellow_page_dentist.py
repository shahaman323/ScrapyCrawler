import scrapy


class YellowPageDentist(scrapy.Spider):
    name = "yellow_page_dentist"
    start_urls = ["https://www.yellowpages.com/california-md/dentists"]

    def parse(self, response):
        print('Parsing: ', response.url)
        ad_urls = response.xpath('//*[@class="business-name"]/@href').getall()
        yield from response.follow_all(ad_urls, callback=self.parse_content)

        next_page = response.xpath('//*[@class="next ajax-page"]/@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_content(self, response):
        print('parsing', response.url)
        item = dict(
            adUrl=response.url,
            clinic=response.xpath('//*[@class="dockable business-name"]/text()').get(),
            videos=response.xpath('//*[@id="yp-video-container"]/@data-videosrc').get(),
            images=response.xpath('//*[@class="media-thumbnail collage-pic"]//@src').get(),
            phones=response.xpath('//*[@class="phone dockable"]/@href').get(),
            location=response.xpath('//span[@class="address"]/text()').get(),
            openingHours=response.xpath('//td[@class="day-hours"]//@datetime').getall(),
            reviewCount=response.xpath('//*[@class="yp-ratings"]/span/text()').get(),
            latestReviewer=response.xpath('//*[@class="author"]/text()').getall()
        )
        print("item", item)
        yield item




