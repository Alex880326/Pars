import scrapy


class SteamdbSpider(scrapy.Spider):
    name = "steamdb"
    allowed_domains = ["steamdb.info"]
    start_urls = ["https://steamdb.info/sales/"]

    def parse(self, response):
        rows = response.xpath('//*[@id="DataTables_Table_0"]/tbody/tr')
        for row in rows:
            game_name = row.xpath('.//td[3]//a/text()').get()
            price = row.xpath('.//td[5]//text()').get()
            rating = row.xpath('.//td[6]//text()').get()
            release = row.xpath('.//td[7]//text()').get()
            link = row.xpath('.//b/a//@href()').get()
            yield response.follow(url=link if link else 'shok', callback=self.parse_game, 
                                  meta={'game_name': game_name,
                                        'price': price,
                                        'rating': rating,
                                        'release': release
                                       })
    
    def parse_game(self, response):
        rows = response.xpath('//*[@id,"DataTables_Table_0"]/tbody')
        for row in rows:
            system = response.xpath('.//td[contains@id,"DataTables_Table_0")]/a/text()').get()
            name = response.request.meta['game_name']
            price = response.request.meta['price']
            rating = response.request.meta['rating']
            release =response.request.meta['release']
            yield {
                'system': system,
                'name': name,
                'price': price,
                'rating': rating,
                'release': release
            }
