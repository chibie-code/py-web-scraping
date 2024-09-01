# scrape live updating webpage
import mechanicalsoup as ms
"""
This script scrapes a live updating webpage to retrieve the result of a dice roll.
It performs the following tasks:
1. Opens the webpage containing the live updating dice roll result.
2. Extracts the result from the HTML element with the id 'result'.
3. Prints the extracted dice roll result.

Libraries used:
- MechanicalSoup: For navigating and interacting with the web page.

Usage:
- The script initializes a StatefulBrowser instance, opens the target URL, and retrieves the live updated result.
- It prints the result of the dice roll for verification.
"""

statefulbrowser = ms.StatefulBrowser(
    soup_config={'features':'lxml'}, # Set parser to the lxml HTML parser,
    raise_on_404=True # raise "LinkNotFoundError" exception whenever page at link/url not found
)

url = "http://olympus.realpython.org/dice"
page = statefulbrowser.open(url)

# You can open url in your actual browser using the ff:
# statefulbrowser.launch_browser(page.soup)

# get the new result from the live updated page
page_soup = page.soup # get the html/soup of the current page
# get the tag that the live updated result is displayed in
result_tag = page_soup.select("#result")[0] # the result tag has the id "result"
result_text = result_tag.text

print(f"dice: {result_text}")

# close browser
statefulbrowser.close()
