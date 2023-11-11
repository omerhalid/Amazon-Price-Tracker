# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

# The URL of the Amazon product page you want to monitor
URL = "https://www.amazon.com/dp/B06XQBNFT7/ref=sbl_dpx_kitchen-electric-cookware_B007WQ9YNO_0"

# Headers to mimic a browser visit
headers = { 'Accept-Language' : "en-US,en;q=0.9",
            'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35"}

# Send a request to the URL
response = requests.get(URL, headers=headers)

# Print the response object to check if the request was successful
print(response)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, "lxml")

# Find the element that contains the price
price_data = soup.find("span", class_="a-offscreen")

# Extract the text from the price element
price = price_data.getText()

# Convert the price string to a floating-point number
split_price = float(price.split("$")[1])

# Print the extracted price
print(split_price)

# Set the threshold price for the alert
BUY_PRICE = 40

# Find the product title and clean it
title = soup.find(id="productTitle").get_text().strip()

# Check if the current price is less than the buy price
if split_price < BUY_PRICE:
    # Create a message with the product title and its price
    message = f"{title} is now {price}"

    # Set up a connection to the SMTP server
    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        # Start TLS for security
        connection.starttls()
        # Log in to your email account
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        # Send an email from your account to the same account
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
