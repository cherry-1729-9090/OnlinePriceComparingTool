import requests
from bs4 import BeautifulSoup

def amazon_scraper(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'TE': 'Trailers',
    }   
    
    while True:
        contents = requests.get(url,headers=headers)
        if contents.status_code == 200:
            soup = BeautifulSoup(contents.text, 'lxml')
            product_name = soup.find('span', {'class': 'a-size-large product-title-word-break'})
            product_price = soup.find('span', {'class': 'a-price-whole'})
            if product_name:
                product_name = product_name.text
                product_name = product_name.strip()
            if product_price:
                product_price = product_price.text
                product_price = product_price.strip()
            print(product_name)
            print(product_price)
            break


if __name__ == "__main__":
    url = input()
    amazon_scraper(url)

