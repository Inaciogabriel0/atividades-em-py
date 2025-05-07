from bs4 import BeautifulSoup
import requests

html = requests.get("https://example.com").text
soup = BeautifulSoup(html, "html.parser")
for link in soup.find_all("a"):
    print(link.get("href"))
