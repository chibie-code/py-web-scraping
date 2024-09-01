"""
GitHub Scraper Script

This script uses MechanicalSoup and other libraries to automate the process of logging into a GitHub account and scraping the nickname from the overview page. The script performs the following tasks:

1. Spoofs the user agent header to mimic a real browser.
2. Logs into a GitHub account using credentials stored in environment variables.
3. Handles hidden input fields on the login page.
4. Uses the same session to navigate to the overview page and scrape the nickname.

Modules:
- mechanicalsoup: For automating web browsing and form submission.
- os: For accessing environment variables.
- csv: For handling CSV files (if needed for future extensions).
- dotenv: For loading environment variables from a .env file.

Usage:
1. Ensure you have the required libraries installed:
    ```bash
    pip install mechanicalsoup python-dotenv
    ```

2. Create a .env file in the same directory as this script with the following content:
    ```
    GITHUB_USERNAME=your_username
    GITHUB_PASSWORD=your_password
    ```

3. Run the script:
    ```bash
    python github_scraper.py
    ```

Note: This script is for educational purposes only. Use it responsibly and ensure you comply with GitHub's terms of service.

Author: D. Okpala
Date: 28/08/2024
"""

import mechanicalsoup as ms
from dotenv import load_dotenv
import os

def load_env_variables():
    """Load environment variables from .env file."""
    load_dotenv()
    username = os.getenv('GITHUB_USERNAME')
    password = os.getenv('GITHUB_PASSWORD')
    return username, password

def create_browser():
    """Create and configure a MechanicalSoup StatefulBrowser instance."""
    soup_c = {"features": "lxml"}
    user_a = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    sb = ms.StatefulBrowser(
        soup_config=soup_c,
        user_agent=user_a,
        raise_on_404=True
    )
    return sb

def login_to_github(sb, username, password):
    """Log in to GitHub using the provided credentials."""
    response = None
    sb.open("https://github.com/login")
    try:
        sb.select_form('form[action="/session"]')
        sb["login"] = username
        sb["password"] = password
        response = sb.submit_selected()
    except Exception as e:
        print(f"Error selecting form: {e}")
        return response  # Handle this case appropriately in your tests
    return response

def scrape_nickname(sb):
    """Scrape the nickname from the GitHub overview page."""
    sb.open("https://github.com/chibie-code")
    if sb.page is None:
        print("Failed to load the page.")
        return None
    psoup = sb.page
    nickname_ele = psoup.find("span", attrs={"class": "p-nickname"})
    return nickname_ele.get_text(strip=True) if nickname_ele else None

def main():
    """Main function to run the GitHub scraper."""
    username, password = load_env_variables()
    sb = create_browser()
    try:
        response = login_to_github(sb, username, password)
        if response is not None:
            if '/login' in response.url:
                print("Login failed")
            else:
                print("Login successful")
                nickname = scrape_nickname(sb)
                print(f"Scraped nickname: {nickname}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        sb.close()

if __name__ == "__main__":
    main()


"""
github_scraper/
├── .env
├── README.md
├── requirements.txt
├── setup.py
├── github_scraper/
│   ├── __init__.py
│   ├── scraper.py
│   └── utils.py
└── tests/
    ├── __init__.py
    └── test_scraper.py

Explanation
Root Directory:
.env: Contains environment variables.
README.md: Provides an overview of the project, usage instructions, and other relevant information.
requirements.txt: Lists the dependencies required for the project.
setup.py: Used for packaging and distribution.
github_scraper/:
__init__.py: Makes the directory a package.
scraper.py: Contains the main scraping logic.
utils.py: Contains utility functions that support the main scraping logic.
tests/:
__init__.py: Makes the directory a package.
test_scraper.py: Contains unit tests for the scraper.

load_env_variables: Loads environment variables from the .env file.
create_browser: Creates and configures a StatefulBrowser instance.
login_to_github: Logs into GitHub using the provided credentials.
scrape_nickname: Scrapes the nickname from the GitHub overview page.
main: The main function that orchestrates the entire process.
This modular structure makes it easier to write unit tests for each function. If you have any more questions or need further assistance, feel free to ask!

Functions
__init__: Initializes the browser with optional parameters like user_agent, soup_config, and requests_session.
open(url, *args, **kwargs): Opens a URL and returns the response.
get(url, *args, **kwargs): Sends a GET request to the specified URL.
post(url, *args, **kwargs): Sends a POST request to the specified URL.
select_form(selector): Selects a form on the current page using a CSS selector.
submit_selected(*args, **kwargs): Submits the currently selected form.
follow_link(link): Follows a link on the current page.
download_link(link, file): Downloads a file from a link on the current page.
get_current_page(): Returns the current page as a BeautifulSoup object.
get_url(): Returns the current URL.
get_response(): Returns the current response object.
set_user_agent(user_agent): Sets the user agent for the browser.
launch_browser(): Launches a real browser for debugging purposes.

Attributes
session: The requests session used by the browser.
soup: The BeautifulSoup object representing the current page.
url: The current URL.
user_agent: The user agent string used by the browser.
history: A list of URLs visited by the browser.
"""
