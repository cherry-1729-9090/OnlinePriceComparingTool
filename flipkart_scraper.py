import requests
from bs4 import BeautifulSoup
import time

def get_product_price_flipkart(product_name):
    flipkart_url = f"https://www.flipkart.com/search?q={product_name}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    max_retries = 3
    retries = 0

    while retries < max_retries:
        try:
            response = requests.get(flipkart_url, headers=headers)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

            soup = BeautifulSoup(response.text, 'html.parser')

            product_name_tag = soup.find('a', {'class': 's1Q9rs'})
            product_price_tag = soup.find('div', {'class': '_30jeq3'})

            if product_name_tag:
                product_name = product_name_tag.text.strip()

            if product_price_tag:
                product_price = product_price_tag.text.strip()

            return f"{product_name}\n{product_price}"

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            retries += 1
            time.sleep(2)  # Wait for 2 seconds before retrying

        except Exception as err:
            print(f"Other error occurred: {err}")
            retries += 1
            time.sleep(2)  # Wait for 2 seconds before retrying

    return "Failed to fetch data from Flipkart"

if __name__ == "__main__":
    user_input = input("Enter the product name: ")
    flipkart_price = get_product_price_flipkart(user_input)
    print(f"{flipkart_price}")
