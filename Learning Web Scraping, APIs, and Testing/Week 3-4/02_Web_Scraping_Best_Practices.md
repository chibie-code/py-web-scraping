## File: 02_Web_Scraping_Best_Practices.md

### Web Scraping Best Practices
- **Respecting `robots.txt`**
  - Always check the `robots.txt` file of a website before scraping to understand which pages are allowed or disallowed to be scraped.
  - Example of checking `robots.txt`:
    - Access `http://example.com/robots.txt` to view the rules.
- **Rate Limiting and Throttling Requests**
  - Implement delays between requests to avoid overwhelming the server (e.g., using `time.sleep()`).
  - Use libraries like `scrapy` that handle this automatically.
  - Consider using `random` delays to mimic human behavior:
    ```python
    import time
    import random

    time.sleep(random.uniform(1, 3))  # Wait between 1 to 3 seconds
    ```
