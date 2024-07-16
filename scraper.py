import requests
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from bs4 import BeautifulSoup

def scrape_flipkart_product(url, max_retries=3):
    retries = 0
    
    while retries < max_retries:
        # Add headers to mimic a browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }
        
        try:
            # Make an HTTP request to the Flipkart product page
            response = requests.get(url, headers=headers)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the HTML content of the page
                soup = BeautifulSoup(response.content, 'html.parser')

                # Extract product details using class names
                product_name = soup.find('span', {'class': '_35KyD6'})
                product_price = soup.find('div', {'class': '_1vC4OE _3qQ9m1'})

                # Check if the elements are found
                if product_name and product_price:
                    # Get the text content if the elements are found
                    product_name = product_name.get_text(strip=True)
                    product_price = product_price.get_text(strip=True)

                    # Print the extracted details
                    print(f"Product Name: {product_name}")
                    print(f"Product Price: {product_price}")
                    return  # Exit the function if successful
                else:
                    print("Error: Unable to find product details on the page.")
            elif response.status_code == 503:
                # If 503 (Service Unavailable) is encountered, wait and retry
                print(f"Service Unavailable. Retrying ({retries + 1}/{max_retries})...")
                time.sleep(2)  # Wait for 2 seconds before retrying
                retries += 1
            else:
                print(f"Error: Unable to fetch data. Status code: {response.status_code}")
                return  # Exit the function on other errors
        except Exception as e:
            print(f"Error: {e}")
            return  # Exit the function on exception

    print("Error: Maximum retries reached. Unable to fetch data.")

# Example usage
if __name__ == "__main__":
    # Example Flipkart product URL
    flipkart_url = "https://www.flipkart.com/10club-screen-cleaning-microfibre-towel-set-3-protection-laptops-mobiles-computers/p/itm38865dd833841?pid=CLKGTMJTENDVZWBG&lid=LSTCLKGTMJTENDVZWBGS5RQY9&marketplace=FLIPKART&store=6bo%2Fai3%2Fzy6&srno=b_1_2&otracker=browse&iid=en_k2OtErp_rtk9jCvY260qyN6x7lTzMzUfkPSQKymF7Zmhs7I9V2AgKFps3rkiXCqr8hCWywIKVHnhO3GLMtnvww%3D%3D&ssid=o1nh57r4lc0000001700556121712"
    
    # Call the scraper function
    scrape_flipkart_product(flipkart_url)
