# -------------- Ekster Price Checker
#
# Check the price of the Ekster GRID Backpack.  Normal price is 349$
# Will send a SMS if price drops below 275$
#-------------------------------------------------------------------

# Librairies
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os

from twilio.rest import Client

# - Setting environment variables

load_dotenv()

account_sid = os.environ["MESS_SID"]
auth_token = os.environ["TOKEN"]
client = Client(account_sid, auth_token)

WEB_LINK = "https://www.ekster.com/en-ca/products/grid-backpack"
TARGET_PRICE = 300


# Request to web page to scrape

response = requests.get(WEB_LINK)

ekster_webpage = response.text
soup = BeautifulSoup(ekster_webpage, "html.parser")

# Scraping the page

price_container = soup.find(name='span', class_="current-price text-gray-950")
price = int(price_container.find("span", attrs={"data-current-price": ""}).get_text(strip=True).strip('$'))

if price <= TARGET_PRICE:
  client = Client(account_sid, auth_token)
  message = client.messages.create(
    from_='+12183221929',
    body=f'The price of the Esket GRID backpack is ${price}.  It is time to buy!',
    to='+18198181719'
  )
