import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://fr.wikipedia.org/wiki/Championnat_de_France_de_rugby_%C3%A0_XV"
    ]

    def parse(self, response):
        filename = 'club.json'
        with open('/root/projects/top14/data/clubs.json', 'w') as f:
            f.write(response.body)
