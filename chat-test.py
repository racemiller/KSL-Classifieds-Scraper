import csv
from bs4 import BeautifulSoup

html = "/home/race/ksl/truck-large.html"

soup = BeautifulSoup(open(html), "html.parser")

rows = []

# Each listing card is an <a role="listitem" ...>
cards = soup.select('a[role="listitem"][href]')

for card in cards:
    # Title (usually in aria-label)
    title = card.get("aria-label", "").strip()

    # URL
    url = card.get("href", "").strip()

    # Miles + Location live in the first div.text-sm with two spans
    miles = ""
    location = ""
    info_div = card.select_one("div.text-sm")
    if info_div:
        spans = info_div.select("span")
        if len(spans) >= 1:
            miles = spans[0].get_text(strip=True)
        if len(spans) >= 2:
            location = spans[1].get_text(strip=True)

    # Price
    price = ""
    price_div = card.select_one('div[aria-label="Price"]')
    if price_div:
        price = price_div.get_text(strip=True)

    rows.append({
        "title": title,
        "miles": miles,
        "location": location,
        "price": price,
        "url": url,
    })

# Write CSV
output_file = "ksl_listings.csv"
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "miles", "location", "price", "url"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Saved {len(rows)} listings to {output_file}")
