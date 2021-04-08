import scrapy

class bookScraper(scrapy.Spider):
    name = 'books2scrape'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']
    base_url = 'http://books.toscrape.com/'

    custom_settings = {

    'AUTOTHROTTLE_ENABLED': True,
    'HTTPCACHE_ENABLED': True,
    }

    def parse(self, response):

        #Fetching class to get all the book details
        all_books = response.css('.col-lg-3')
    
        for book in all_books:

            #Used to fetch books URL
            url = book.css('h3 a::attr(href)').extract_first()

            #Used to fetch image link for the books
            img_link = book.css('a img::attr(src)').extract_first()

            #Used to fetch title of the books
            title = book.css('h3 a::attr(title)').extract()

            #Used to fetch the price details in text format
            price = book.css('div.product_price p.price_color::text').extract()
            
            #This fucntion is used to add catalogue to the path since some links does not have this mentioned
            if 'catalogue/' not in url:
                url = 'catalogue/' + url

            #Combining the fetched URL with base URL to form full path
            page_url = self.base_url + url

            #This function to make some alteration in the output and to get full path
            image_url = self.base_url + img_link.replace('../','')

            #Yield is used to map the values for output
            yield {
                'Book Title' : title,
                'Product Price' : price,
                'Image URL' : image_url,
                'Book URL': page_url,
                }

        #This function is to navigate to the next page        
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)