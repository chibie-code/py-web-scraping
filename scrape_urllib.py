# Simple web scraping using urllib.request's urlopen func
# import urllib.request's urlopen function
from urllib.request import urlopen

# write the webpage url u want to scrape
url = "http://olympus.realpython.org/profiles/aphrodite"

# open the webpage that url points to, using the urlopen() function call
# with the designated url as the parameter
wbpage = urlopen(url)

# wbpage is now an object that has the whole html data for that page/url in it
print(wbpage)

# now we extract the whole html from the response object in bytes
# using .read() on the page object as bytes
# then decoding with .decode("utf-8") as "utf-8" text
page_bytes = wbpage.read()
page_html = page_bytes.decode("utf-8")

print(page_html)
