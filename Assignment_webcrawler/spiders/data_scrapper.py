
import scrapy
from ..items import AssignmentWebcrawlerItem

class DataScrap (scrapy.Spider):
    name = 'data_scrap'
    start_urls = ['https://www.sastodeal.com/books/genre.html']
    
    #initializing page number varaiable for pagination
   
    def parse(self, response):

       

       #serach for class name where the data that are need to scrap are located
        product = response.css('.product-item-details')
        for p in product:
            
            item_url = p.css('.product-item-link::attr(href)').extract()
            
            for i in item_url:
                yield response.follow(i,callback =self.parse_product_details)
            
            
        next_page = response.css(".next::attr(href)").get()
        
    #to goto next page
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback = self.parse)    
    
    def parse_product_details(self, response):
        items = AssignmentWebcrawlerItem()
        item=response.css(".base::text").extract()
        

        item_name=item[0].split("-")[0]
        author = item[0].split("-")[1]
        
        t_price=response.css(".price::text")[0].extract()
        price=""
        for c in t_price:
            if c.isdigit():
                price = price + c

        
        product_genre = response.css(".items a::text")[3].get() 
        items['item_name']=item_name
        items['price']= price   
        items['author']= author
        items['product_genre']= product_genre
        yield items
    

    
        
        
        


 