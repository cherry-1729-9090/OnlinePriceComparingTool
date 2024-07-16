from flipkart_scraper import get_product_price_flipkart
from amazon_scraper import get_product_price_amazon
from urllib.parse import urlparse
from myntra_scraper import myntra_scrapper                                                                  
search_method = int(input("Please specify the method you want to search ([1] url [2]product_name) : "))

if search_method == 1:
    url_link = input("Enter the url of the product: ")
    domain_name = urlparse(url_link).netloc
    if domain_name == "www.flipkart.com":
        flipkart_scrapper(url_link)
    elif domain_name == "www.amazon.in":
        amazon_scraper(url_link)
    else:
        print("Unsupported domain.")

elif search_method == 2:
    product_name = input("Please enter the product name :")
    
    print("*****___Amazon_Price____*****")
    print(get_product_price_amazon(product_name))
    print()
    print()
    
    # Flipkart scrapper is currently not working
    # print("*****___Flipkart_Price___*****")
    # print(get_product_price_flipkart(product_name))
    
else:
    print("Invalid option.Please select the correct option.")