import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.olx.in/items/q-car-cover"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

r = requests.get(url, headers=headers)
if r.status_code != 200:
    exit()

soup = BeautifulSoup(r.text, "html.parser")
data = soup.find_all("li", class_="EIR5N")
output = []

for i in data:
    t = i.find("span")
    p = i.find("span", class_="_89yzn")
    l = i.find("span", class_="_2tW1I")
    a = i.find("a", href=True)
    row = [
        t.text.strip() if t else "",
        p.text.strip() if p else "",
        l.text.strip() if l else "",
        "https://www.olx.in" + a['href'] if a else ""
    ]
    output.append(row)

with open("olx_car_covers.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Title", "Price", "Location", "Link"])
    w.writerows(output)
