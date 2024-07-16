import requests
from bs4 import BeautifulSoup

def get_product_price_amazon(product_name):
    # Amazon URL with the product name as a search query
    amazon_url = f"https://www.amazon.in/s?k={product_name.replace(' ', '-')}&crid=L2JFQOIWU7YY&sprefix={product_name.replace(' ', '-')}%2Caps%2C247&ref=nb_sb_noss_2"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

    while True:
        response = requests.get(amazon_url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')

            product_name_tag = soup.find('span', {'class': 'a-size-base-plus a-color-base a-text-normal'})
            product_price_tag = soup.find('span', {'class': 'a-price-whole'})

                # Check if the tags are found
            if product_name_tag:
                product_name_tag = product_name_tag.string

            if product_price_tag :
                product_price_tag = product_price_tag.string

            return f"{product_name_tag} \n₹{product_price_tag}"


if __name__ == "__main__":
    user_input = input("Enter the product name: ")
    amazon_price = get_product_price_amazon(user_input)
    print(f"{amazon_price}")
