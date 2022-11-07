import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL = "https://www.amazon.com/dp/B06XQBNFT7/ref=sbl_dpx_kitchen-electric-cookware_B007WQ9YNO_0"

headers = { 'Accept-Language' : "en-US,en;q=0.9",
            'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35"}

response = requests.get(URL, headers=headers)

print(response)

soup = BeautifulSoup(response.content, "lxml")

price_data = soup.find("span", class_="a-offscreen")

price = price_data.getText()

split_price = float(price.split("$")[1])

print(split_price)

BUY_PRICE = 40

title = soup.find(id="productTitle").get_text().strip()

if split_price < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
