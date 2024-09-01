import mechanicalsoup as ms
"""
(Docstring) This script uses MechanicalSoup to scrape and interact with a web page that lists NHL team stats. It performs the following tasks:

1. **Set Items Per Page**: Dynamically sets the number of items listed per page by modifying the 'per_page' query parameter in the URL.
2. **Scrape Team Data**: Scrapes team data from the page, extracting information from table rows with the class 'team'.
3. **Search for Teams**: Uses the search feature in the form element to search for a specific team name and prints the first few results.

Functions:
- `reconstruct_url_with_params(parsed_url, new_query_params)`: Reconstructs the URL with updated query parameters.
- `set_per_page(sb, new_per_page_value)`: Sets the 'per_page' query parameter value and returns the updated page result.
- `scrape_items(soup)`: Scrapes list items (team data) from the page.

Usage:
- The script initializes a StatefulBrowser instance, opens the target URL, and performs the tasks mentioned above.
- It prints the updated URLs and scraped data for verification.
"""
# used to interact with urls and their query params
from urllib.parse import urlparse, parse_qs, urlencode
import json

# statefulbrowser (sb) instance
sb = ms.StatefulBrowser(
    soup_config = {'features':'lxml'},
    raise_on_404=True
)
url = "https://www.scrapethissite.com/pages/forms/"
scraped_page = sb.open(url)

# sb.launch_browser(scraped_page.soup)
ssoup = scraped_page.soup # this scraped page's soup

# Tasks
# 1. get the soup for when per page is set to 50, 25 and/or 100
# 2. create modular helper functions that scrape information from specified parts of the page.
# e.g. get all list items displayed on the page as a list of objects
# 3. use search feature in the "form" element to search for specific team name and print first few results
# 4. navigate to certain page number that pagination allows

# 1. id="per_page" for the select box to assign how many items listed per page

# Function to reconstruct the URL with updated query parameters
def reconstruct_url_with_params(parsed_url, new_query_params):
    # ? Could create a separate function to handle reconstructing the url, that gets all the external variables it needs passed to it through its params
    # Reconstruct the URL with updated query parameters
    # The scheme (protocol) of the URL, e.g., 'https'
    scheme = parsed_url.scheme
    # The network location (domain) of the URL, e.g., 'www.scrapethissite.com'
    netloc = parsed_url.netloc
    # The path of the URL, e.g., '/pages/forms/'
    path = parsed_url.path
    new_query_string = urlencode(new_query_params, doseq=True)

    new_url = f"{scheme}://{netloc}{path}?{new_query_string}"
    return new_url

# function to dynamically set the per_page query param value and return new page result
def set_per_page(sb, new_per_page_vlue):
    # get the current page's url and parse its query params
    current_url = sb.get_url()
    parsed_url = urlparse(current_url)
    query_params = parse_qs(parsed_url.query)
    # get the per_page query param's value
    # here, the code is supposed to return whatever the 'per_page' query param's value is
    # but if the 'per_page' query param doesn't exist in the url, it returns a default value of None
    default_ret = None
    per_page_value = query_params.get("per_page", [default_ret])[0]
    # check if current page already has the specified per_page value
    if per_page_value == str(new_per_page_vlue):
        # make no changes to the current page
        return browser.get_current_page()

    # else update the per_page value and maintain any other existing query param values
    query_params['per_page'] = [str(new_per_page_vlue)]

    new_url = reconstruct_url_with_params(parsed_url, query_params)

    print(f"new per_page url: {new_url}")

    # open the new url
    sb.open(new_url)

    updated_page = sb.get_current_page()
    return updated_page

# Get the soup for per_page = 50
soup_50 = set_per_page(sb, 50)
print(f"new url [50]: {sb.get_url()}")
# Get the soup for per_page = 15
soup_2 = set_per_page(sb, 2)
print(f"new url [2]: {sb.get_url()}")

soup_25 = set_per_page(sb, 25)
print(f"new url [25]: {sb.get_url()}")


# 2. Scrape list items. in the case of the given page,
# the items of interest are each in '<tr>' tag with the same class 'team'

def scrape_items(soup):
    items = []
    column_headings = [
        th.get_text(strip=True)
        .lower()
        .replace(' ', '_')
        .replace('(', '')
        .replace(')', '')
        for th in soup.select("table.table th")]
    for item in soup.select("tr.team"):
        data = {}
        for i, td in enumerate(item.find_all("td")):
            key = column_headings[i]
            data[key] = td.get_text(strip=True)
        if data:
            items.append(data)
    return items

# Scrape <tr> tags with class 'team'
team_rows_25 = scrape_items(soup_25)
print(json.dumps(team_rows_25, indent=2))


# 3. use search feature in the "form" element to search for specific team name and print first few results
scraped_page = sb.open(url)
# Select the specific form by its action attribute
form = sb.select_form("form[action='/pages/forms/']")
# Set the value of the input field with the name 'q'
print(form.set("q", "chicago"))
# Submit the selected form
res = sb.submit_selected()
# Get the updated page
updated_page = sb.get_current_page()
# Print the updated URL
print(sb.get_url())
sb.launch_browser(updated_page.soup)

sb.close()
