## File: 03_Basic_Scraping_Techniques.md

### Basic Scraping Techniques
- **Parsing HTML and XML**
  - Use Beautiful Soup to parse HTML content:
    ```python
    from bs4 import BeautifulSoup
    import requests

    response = requests.get('http://example.com')
    soup = BeautifulSoup(response.text, 'html.parser')
    ```

- **Navigating the DOM**
  - Use methods like `.find()`, `.find_all()`, and CSS selectors to navigate the DOM.
  - Example: 
    ```python
    title = soup.find('title').text
    ```

- **Extracting Data from Static Websites**
  - Identify the HTML elements containing the data you need.
  - Extract text, links, images, etc., using Beautiful Soup methods.
  - Example:
    ```python
    all_links = [a['href'] for a in soup.find_all('a', href=True)]
    ```
