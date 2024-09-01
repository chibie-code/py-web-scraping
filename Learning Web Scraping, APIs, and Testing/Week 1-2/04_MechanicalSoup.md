## File: 04_MechanicalSoup.md

### MechanicalSoup
- **What is MechanicalSoup?**
  - MechanicalSoup is a Python library that provides a simple way to automate web browsing and scraping tasks.
  - It combines the functionality of `requests` and `Beautiful Soup` into a convenient API.

- **Key Features**
  - **Form Handling**: Easily fill out and submit forms on web pages.
  - **Session Management**: Maintain session information (cookies) across requests.
  - **Navigation**: Navigate between pages and handle page redirections.

- **Installation**
  - Install MechanicalSoup using pip:
    ```bash
    pip install MechanicalSoup
    ```

- **Basic Usage Example**
  - Here’s a simple example of using MechanicalSoup to scrape a webpage:
    ```python
    import mechanicalsoup

    # Create a browser instance
    browser = mechanicalsoup.StatefulBrowser()

    # Open a page
    browser.open('http://example.com')

    # Select a form and fill it
    browser.select_form('form')
    browser["input_name"] = "example_value"  # Replace with actual input name and value

    # Submit the form
    response = browser.submit_selected()

    # Parse the response with Beautiful Soup
    soup = response.soup
    print(soup.title.text)  # Print the title of the page
    ```

- **StatefulBrowser Functions and Attributes**
  - **Functions**
    - `__init__`: Initializes the browser with optional parameters like `user_agent`, `soup_config`, and `requests_session`.
    - `open(url, *args, **kwargs)`: Opens a URL and returns the response.
    - `get(url, *args, **kwargs)`: Sends a GET request to the specified URL.
    - `post(url, *args, **kwargs)`: Sends a POST request to the specified URL.
    - `select_form(selector)`: Selects a form on the current page using a CSS selector.
    - `submit_selected(*args, **kwargs)`: Submits the currently selected form.
    - `follow_link(link)`: Follows a link on the current page.
    - `download_link(link, file)`: Downloads a file from a link on the current page.
    - `get_current_page()`: Returns the current page as a BeautifulSoup object.
    - `get_url()`: Returns the current URL.
    - `get_response()`: Returns the current response object.
    - `set_user_agent(user_agent)`: Sets the user agent for the browser.
    - `launch_browser()`: Launches a real browser for debugging purposes.

  - **Attributes**
    - `session`: The requests session used by the browser.
    - `soup`: The BeautifulSoup object representing the current page.
    - `url`: The current URL.
    - `user_agent`: The user agent string used by the browser.
    - `history`: A list of URLs visited by the browser.

- **When to Use MechanicalSoup**
  - MechanicalSoup is particularly useful when:
    - You need to log in to a site before scraping.
    - You want to interact with forms (e.g., search forms).
    - You prefer a more high-level API compared to raw `requests` and `Beautiful Soup`.

### Conclusion
MechanicalSoup is a powerful tool for automating web browsing tasks and can simplify the process of scraping websites that require form submission or session management. It's a great addition to your toolkit alongside `Beautiful Soup` and `Scrapy`.
