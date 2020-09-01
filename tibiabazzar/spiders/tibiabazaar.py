import scrapy
from ..items import TibiabazzarItem

class TibiabazaarSpider(scrapy.Spider):
    name = 'tibiabazaar'
    allowed_domains = ['www.tibia.com/charactertrade/?subtopic=pastcharactertrades']
    start_urls = ['http://www.tibia.com/charactertrade/?subtopic=pastcharactertrades/']
    next_page = 'http://www.tibia.com/charactertrade/?subtopic=pastcharactertrades&currentpage='

    def parse(self, response):

        pages = response.css(".PageLink a::text")[-1].get()

        current_page = response.css(".CurrentPageLink::text").get()

        if current_page == 'First Page':
            current_page = 1               

        chars = response.css(".Auction")

        for char in chars:
            name = char.css("a::text").get()
            server =  char.css("a::text")[1].get()
            descricao = char.css(".AuctionHeader::text").get()
            arrDesc = descricao.split("|")
            lvl = arrDesc[0].replace("Level: ", "").strip()
            vocation = arrDesc[1].replace("Vocation:", "").strip()
            sex = arrDesc[2].strip()

            item1 = char.css(".CVIconObject::attr(title)")[0].get().replace('""', "").strip()
            item2 = char.css(".CVIconObject::attr(title)")[1].get().replace('""', "").strip()
            item3 = char.css(".CVIconObject::attr(title)")[2].get().replace('""', "").strip()
            item4 = char.css(".CVIconObject::attr(title)")[3].get().replace('""', "").strip()

            start = char.css(".ShortAuctionDataValue::text")[0].get()
            end = char.css(".ShortAuctionDataValue::text")[1].get()

            status_auction = char.css(".ShortAuctionDataLabel::text")[2].get()
            if status_auction == "Minimum Bid:" :
                status_auction = "Not Sold"
            else:
                status_auction = "Sold"

            b_tag = char.css(".ShortAuctionDataValue")[2]
            tc = b_tag.css("b::text").get().replace(',', "").replace('.', "")

            items = TibiabazzarItem()

            items['name'] = name
            items['server'] =  server
            items['lvl'] = lvl
            items['vocation'] = vocation
            items['sex'] = sex
            items['item1'] = item1
            items['item2'] = item2
            items['item3'] = item3
            items['item4'] = item4
            items['start'] = start
            items['end'] = end
            items['status_auction'] = status_auction
            items['tc'] = tc

            special_features = char.css(".SpecialCharacterFeatures").extract_first()

            if special_features:
                entries = char.css(".Entry")

                for num, entry in enumerate(entries,start=1):
                    items['special_features'+str(num)] = entry.css("div ::text").get()

            yield items

        if current_page != 'Last Page':

            next_page = self.next_page + str(int(current_page) +1)           

            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse,
                dont_filter=True
            )
