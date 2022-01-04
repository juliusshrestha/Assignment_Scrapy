import scrapy
from ..items import AssignmentWebcrawlerItem

class DataScrap (scrapy.Spider):
    name = 'data_scrap'
    start_urls = ['https://www.sastodeal.com/books/genre.html']
    
    #initializing page number varaiable for pagination
    page_number =2

    def parse(self, response):

        items = AssignmentWebcrawlerItem()

       #serach for class name where the data that are need to scrap are located
        product = response.css('.product-item-details')
        for p in product:
            item_name = p.css('.product-item-link::text').extract()
            price  = p.css('.price::text').extract()
            

            items['item_name']=item_name
            items['price']=price
            
            yield items
        
        #to goto next page

        next_page = "https://www.sastodeal.com/books/genre.html?p="+ str(DataScrap.page_number)
        
        # 50 pages are crawled 
        if DataScrap.page_number <=50:
            DataScrap.page_number +=1
            yield response.follow(next_page, callback = self.parse)
        
        
        


 