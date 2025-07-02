import requests

# Target URL
url = "https://www.moneycontrol.com/india/stockpricequote/computers-software/infosys/IT"

# Set a user-agent to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

# Send request
response = requests.get(url)

# Save to file
with open("hdfc_stock_page.html", "w", encoding="utf-8") as file:
    file.write(response.text)

print("Saved page to hdfc_stock_page.html")
