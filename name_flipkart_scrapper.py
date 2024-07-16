import requests
from bs4 import BeautifulSoup

def flipkart_scrapper(url):
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
            
            product_name = soup.find('span', {'class': 'B_NuCI'})
            
            product_price = soup.find('div', {'class': '_30jeq3 _16Jk6d'})
            
            if product_name:
                product_name = product_name.text
            
            if product_price:
                product_price = product_price.text
            
            print(product_name)
            
            print(product_price)
            
            break



if __name__ == "__main__":
    url = input()
    flipkart_scrapper(url)
