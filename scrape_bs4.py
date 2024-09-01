# Scraping using BeautifulSoup4
from bs4 import BeautifulSoup
from urllib.request import urlopen

# the url being scraped
url = "http://olympus.realpython.org/profiles/dionysus"
page_obj = urlopen(url)
html_bytes = page_obj.read()
html = html_bytes.decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

print(soup.get_text())
