## File: 01_Handling_Dynamic_Content.md

### Handling Dynamic Content
- **Introduction to Selenium for Scraping Dynamic Pages**
  - Selenium is a powerful tool that automates browsers, ideal for scraping websites that use JavaScript to load content dynamically.
  - Key Features:
    - Simulates real user interactions (clicks, scrolling, etc.).
    - Can handle pop-ups and alerts.
    - Works with multiple browsers (Chrome, Firefox, etc.).
  - Installation:
    - Install Selenium using pip: `pip install selenium`.
    - Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome).
  - Basic Usage Example:
    ```python
    from selenium import webdriver

    driver = webdriver.Chrome()  # or webdriver.Firefox() for Firefox
    driver.get("http://example.com")
    # Interact with the page
    content = driver.page_source
    driver.quit()
    ```
