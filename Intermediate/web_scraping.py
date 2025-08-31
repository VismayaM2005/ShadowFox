import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

header={
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    'Accept-Language':"en-US,en;q=0.9,hi;q=0.8",
    "Sec-Ch-Ua-Platform": "Windows"
    }

url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
response=requests.get(url=url,headers=header)
amazon_webpage=response.text
soup=BeautifulSoup(amazon_webpage,"html.parser")
price=soup.find(name="span",class_="a-offscreen").getText()
final_price=float(price.split('$')[1])

if final_price<100.0:
    with smtplib.SMTP(SMTP_ADDRESS,587) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDRESS,password=EMAIL_PASSWORD)
        subject = "Price Drop!!"
        body = (
            "Instant Pot Duo Plus 9-in-1 Electric Pressure Cooker, Slow Cooker, Rice Cooker, "
            "Steamer, Sauté, Yogurt Maker, Warmer & Sterilizer, Includes App With Over 800 Recipes, "
            f"Stainless Steel, 3 Quart is now ${final_price}\n{url}"
        )
        msg = f"Subject:{subject}\n\n{body}"
        connection.sendmail(from_addr=EMAIL_ADDRESS, to_addrs=EMAIL_ADDRESS, msg=msg.encode("utf-8"))