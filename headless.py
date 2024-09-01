# headless browser with MechanicalSoup to interact with webpage
import mechanicalsoup
"""
This script uses MechanicalSoup to interact with a login webpage and scrape data after logging in.
It performs the following tasks:
1. Opens the login webpage using a headless browser.
2. Parses the webpage using BeautifulSoup.
3. Fills in the login form with the correct username and password.
4. Submits the login form and navigates to the profile page.
5. Scrapes all links from the profile page and prints their text and addresses.

Libraries used:
- MechanicalSoup: For navigating and interacting with web pages.
- BeautifulSoup: For parsing HTML content.

Usage:
- The script initializes a headless browser instance, opens the login page, fills in the login credentials, and submits the form.
- After a successful login, it scrapes the profile page for links and prints the results.
"""

# headless browser instance
browser = mechanicalsoup.Browser()

url = "http://olympus.realpython.org/login"
page = browser.get(url)

# mechanicalsoup uses beutiful soup to parse the webpage
print(page.soup)

# program to login to the webpage using mechanicalsoup
# 2. After getting the page using the headless browser instance
# obtain the .soup of it and perform mouse select actions on the field elements
pg_html = page.soup
# get the form object
form = pg_html.select("form")[0]
# to the form object, perform mouse select on the first input field
# and set its value attribute to a correct username
form.select("input")[0]["value"] = "zeus"
# to the form object, perform mouse select on the second input field
# and set its value attribute to the correct respective password
form.select("input")[1]["value"] = "ThunderDude"

# 3. perform submit action on the form
profile_pg = browser.submit(form, page.url)

print(profile_pg.url)

# Now, after login is successfull
if (profile_pg.url != page.url):
    # You can then scrape the profiles page

    # You can get all links in the page
    profile_pg_html = profile_pg.soup
    # to select just the first link, u can do profile_pg_html.a
    links_arr = profile_pg_html.select("a")

    print(links_arr)

    for link in links_arr:
        address = link["href"]
        text = link.text
        print(f"{text}: {address}")

browser.close()
