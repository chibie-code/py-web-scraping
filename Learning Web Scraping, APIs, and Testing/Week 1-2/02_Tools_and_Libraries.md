## File: 02_Tools_and_Libraries.md

### Tools and Libraries
- **Learn Python Basics (if needed)**
  - Familiarize yourself with Python syntax, data structures, and libraries.
  - Recommended resources: Codecademy, Python official documentation, or freeCodeCamp.

- **Introduction to Beautiful Soup**
  - Beautiful Soup is a Python library for parsing HTML and XML documents.
  - It provides simple methods for navigating, searching, and modifying the parse tree.
  - Install Beautiful Soup using pip: `pip install beautifulsoup4`.

- **Introduction to Scrapy**
  - Scrapy is an open-source web crawling framework for Python, designed to efficiently extract data from websites.
  - It provides a powerful set of tools for handling requests, responses, parsing data, and storing results.
  - Key Features:
    - **Fast and Efficient**: Built on asynchronous networking for high-speed data extraction.
    - **Built-in Item Pipeline**: Automatically handle data cleaning and storage.
    - **Support for Various Data Formats**: Easily export data in formats like JSON, CSV, and XML.
    - **Extensible**: Supports middleware and custom extensions for specific needs.
  - Installation:
    - Install Scrapy using pip: `pip install Scrapy`.
  - Creating a New Scrapy Project:
    - Use the command: `scrapy startproject project_name`.
  - Defining a Spider: 
    - A class that defines how to scrape a particular site.
  - Running the Spider:
    - Use the command: `scrapy crawl spider_name`.
  - Storing the Data:
    - Store scraped data in JSON format using: `scrapy crawl spider_name -o output.json`.

- **Introduction to MechanicalSoup**
  - MechanicalSoup is a Python library that provides a simple way to automate web interactions.
  - It combines the capabilities of Beautiful Soup and Requests, allowing for easy form submission and data extraction.
  - Key Features:
    - **Automate Browsing**: Simulate a web browser to navigate websites and fill out forms.
    - **Session Management**: Maintains sessions and cookies automatically.
    - **Easy Integration**: Works well with Beautiful Soup for parsing HTML.
  - Installation:
    - Install MechanicalSoup using pip: `pip install MechanicalSoup`.
  - Basic Usage Example:
    ```python
    import mechanicalsoup

    browser = mechanicalsoup.StatefulBrowser()
    browser.open("http://example.com/login")
    browser.select_form('form[action="/login"]')
    browser["username"] = "your_username"
    browser["password"] = "your_password"
    browser.submit_selected()
    ```
  - When to Use MechanicalSoup:
    - Ideal for websites that require user interaction, such as logging in or submitting forms.
    - Great for simple scraping tasks where session management is needed.
