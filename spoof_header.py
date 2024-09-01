import requests
"""
This script sends an HTTP GET request to a specified URL with spoofed headers to make the request appear as if it's coming from a browser.

It performs the following tasks:
1. Defines the URL of the page to be scraped.
2. Sets up the headers to mimic a browser request, including the essential 'User-Agent' header.
3. Sends the GET request with the spoofed headers.
4. Checks if the request was successful and prints the appropriate message.

Key Points:
- The 'User-Agent' header is crucial for making the request appear as if it's coming from a browser. This helps bypass some basic anti-scraping measures.
- Other headers like 'accept', 'accept-language', and 'referrer' are included to further mimic a genuine browser request, although they may not be strictly necessary for this specific site.
"""
# URL of the page you want to scrape
url = "https://www.scrapethissite.com/pages/advanced/?gotcha=headers"

# Essential headers to make the request appear as if it's coming from a browser
headers = {
    # The "User-Agent" is the main header string that spoofs the request to make the server think the request is coming from a browser and not form a script
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    # the rest aren't all needed
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "referrer": "https://www.scrapethissite.com/pages/advanced/"
}

# Make the request with the spoofed headers
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print(f"Headers properly spoofed, request appears to be coming from a browser :). Status code: {response.status_code}")
else:
    print(f"Failed to spoof headers. Status code: {response.status_code}\nContent: {response.content}")
