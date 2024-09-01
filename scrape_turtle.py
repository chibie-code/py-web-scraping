import mechanicalsoup as ms
import json
# used to interact with urls and their query params
from urllib.parse import urlparse, parse_qs, urlencode

"""
(Docstring) This script scrapes turtle family data from the 'Scrape This Site' website.
It performs the following tasks:
1. Opens the webpage containing a list of turtle families.
2. Extracts the names of all turtle families listed on the page.
3. For each turtle family, constructs a URL to access detailed information.
4. Scrapes the description and image link for each turtle family.
5. Stores the scraped data in a JSON format and prints it.

Libraries used:
- MechanicalSoup: For navigating and interacting with web pages.
- urllib.parse: For handling URL query parameters.
- json: For formatting the scraped data as JSON.
"""

sb = ms.StatefulBrowser(
    soup_config={'features': 'lxml'},  # Set parser to the lxml HTML parser
    raise_on_404=True  # Raise "LinkNotFoundError" exception if page not found
)

url = "https://www.scrapethissite.com/pages/frames/?frame=i"
page = sb.open(url)

psoup = page.soup

turtle_families = [nm.text for nm in psoup.select("h3.family-name")]
print(turtle_families)

# Function to reconstruct the URL with updated query parameters
def build_url_with_params(parsed_url, new_query_params):
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

# Function to get the description of a turtle family
def get_description(family_name):
    # get the current page's url and parse its query params
    current_url = sb.get_url()
    parsed_url = urlparse(current_url)
    query_params = parse_qs(parsed_url.query)
    # check if family url query param already exists and if it's for the current family, don't change the page
    default_return_value = None
    family_value = query_params.get("family", [default_return_value])[0]
    # check if current page already has the specified per_page value
    if family_value == str(family_name):
        # make no changes to the current page
        return browser.get_current_page()

    # else change the page to the one showing the description for that turtle family
    query_params['family'] = [str(family_name)]

    new_url = build_url_with_params(parsed_url, query_params)

    print(f"{family_name} turtles' description url: {new_url}")

    # open this description url in the headless stateful browser
    # get the description page's bs4 object
    description_page = sb.open(new_url)
    desc_soup = description_page.soup

    try:
        description = str(desc_soup.select("p.lead")[0].get_text(strip=True))
        img_link = str(desc_soup.select("img.turtle-image")[0]["src"])
    except IndexError:
        description = "Description not found"
        img_link = "Image not found"

    return [description, img_link]


turtles = []
for name in turtle_families:
    [desc, img] = get_description(name)
    turtle = {
        "family":name,
        "description":str(desc),
        "img_link": str(img)
    }
    turtles.append(turtle)

print(json.dumps(turtles, indent=2))
# close browser
sb.close()
