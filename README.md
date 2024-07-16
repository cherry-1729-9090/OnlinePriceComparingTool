# Product Price Scraper

This Python script allows you to fetch product prices from various e-commerce websites.

## Current Features

- Fetches product prices from Amazon India.
- Supports both URL input and product name input for searching.

## Usage

### Requirements

- Python 3.x
- BeautifulSoup (`pip install beautifulsoup4`)
- Requests (`pip install requests`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/cherry-1729-9090/product-price-scraper.git
   cd product-price-scraper
   ```

2. Install dependencies:

   ```bash
   pip install requests beautifulsoup4 chromium
   ```

### Usage

Run the script `scraper.py`:

```bash
python scraper.py
```

Follow the prompts to specify the search method and input the necessary details.

### Example

```bash
Please specify the method you want to search ([1] url [2]product_name) : 2
Please enter the product name :water bottle

*****___Amazon_Price____*****
Boldfit Water Bottles Stainless Steel Water Bottle 1 Litre Steel Water Bottles for School, Office, Home, Gym 1 Litre Water Bottle for Men Leakproof, Rust free Steel Bottle -1000 ml Water Bottle Black
₹932

```

## Future Improvements

- Expand support for additional e-commerce websites (e.g., Flipkart, Myntra).
- Enhance error handling and retry mechanisms for robustness.

Feel free to contribute to this project by adding more features or improving existing ones!

