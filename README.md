# Amazon Price Alert

## Project Overview
The Amazon Price Alert project is a Python script designed to monitor the price of a specific product on Amazon. When the price falls below a predetermined threshold, the script automatically sends an email alert to the user. This utility is particularly useful for tracking price drops on desired products, enabling users to make timely purchases at the best possible price.

## Goal
The primary goal of this project is to automate the process of tracking a product's price on Amazon and to notify the user promptly when the product is available at a lower price.

## Reasoning
Regularly checking the price of a product can be tedious and time-consuming. This project simplifies the process by automating the price tracking and notification procedure, ensuring that users don't miss out on potential savings.

## How It Works
1. **URL and Price Threshold Setup**: The user specifies the URL of the Amazon product and the desired buy price threshold in the script.
2. **Web Scraping**: The script uses `requests` and `BeautifulSoup` to scrape the product's current price from the Amazon webpage.
3. **Price Comparison**: The scraped price is compared with the user-defined threshold.
4. **Email Alert**: If the current price is lower than or equal to the threshold, the script sends an email alert to the user.

## Code Explanation
- **Libraries Used**:
  - `requests`: For sending HTTP requests to the Amazon product page.
  - `BeautifulSoup` from `bs4`: For parsing HTML and extracting the necessary data (product price and title).
  - `lxml`: Used as a parser for BeautifulSoup.
  - `smtplib`: For sending the email alert.
- **Script Flow**:
  1. **Setting Up the URL and Headers**: The script starts by defining the URL of the product and headers to mimic a browser request.
  2. **HTTP Request**: It sends a GET request to the Amazon product page.
  3. **HTML Parsing**: The response is parsed to extract the product price and title using BeautifulSoup.
  4. **Price Processing**: The price is processed and converted into a floating-point number for comparison.
  5. **Email Notification**: If the product's price falls below the threshold, an email is composed and sent using SMTP protocol.

## How to Use
1. Replace `URL`, `BUY_PRICE`, `YOUR_SMTP_ADDRESS`, `YOUR_EMAIL`, and `YOUR_PASSWORD` with your desired product URL, price threshold, SMTP server address, and email credentials.
2. Run the script periodically (e.g., using a cron job) to check for price updates.

## Future Enhancements
- Integrate with a scheduling tool for regular checks.
- Extend functionality to monitor multiple products.
- Include error handling for web requests and email sending process.
- Implement a user-friendly interface for non-technical users.

## Disclaimer
This project is intended for educational purposes. Be aware of Amazon's terms of service regarding web scraping.

---

*Happy Savings!*
