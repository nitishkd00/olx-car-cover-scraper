import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.olx.in/items/q-car-cover"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(URL, headers=HEADERS)

if response.status_code != 200:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

items = soup.find_all("li", class_="EIR5N")

results = []
for item in items:
    title_tag = item.find("span")
    title = title_tag.text.strip() if title_tag else "N/A"

    price_tag = item.find("span", class_="_89yzn")
    price = price_tag.text.strip() if price_tag else "N/A"

    location_tag = item.find("span", class_="_2tW1I")
    location = location_tag.text.strip() if location_tag else "N/A"

    link_tag = item.find("a", href=True)
    link = "https://www.olx.in" + link_tag['href'] if link_tag else "N/A"

    results.append([title, price, location, link])

with open("olx_car_covers.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Location", "Link"])
    writer.writerows(results)

print("Scraping complete. Data saved to olx_car_covers.csv.")
