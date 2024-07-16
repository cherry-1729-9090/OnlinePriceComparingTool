import requests
from bs4 import BeautifulSoup

def get_product_price_flipkart(product_name):
    # Flipkart URL with the product name as a search query
    flipkart_url = f"https://www.flipkart.com/search?q={product_name}"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    }

    while True:
        response = requests.get(flipkart_url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')

            product_name_tag = soup.find('a', {'class': 's1Q9rs'})
            product_price_tag = soup.find('div', {'class': '_30jeq3'})

            # Check if the tags are found
            if product_name_tag:
                product_name_tag = product_name_tag.string

            if product_price_tag:
                product_price_tag = product_price_tag.string

            return f"{product_name_tag} \n{product_price_tag}"

        else:
            print(f"Failed to fetch data from Flipkart. Status Code: {response.status_code}")

if __name__ == "__main__":
    user_input = input("Enter the product name: ")
    flipkart_price = get_product_price_flipkart(user_input)
    print(f"{flipkart_price}")
