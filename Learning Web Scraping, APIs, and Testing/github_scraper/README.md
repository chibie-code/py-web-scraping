# GitHub Scraper Script

This script uses MechanicalSoup and other libraries to automate the process of logging into a GitHub account and scraping the nickname from the overview page. The script performs the following tasks:

1. Spoofs the user agent header to mimic a real browser.
2. Logs into a GitHub account using credentials stored in environment variables.
3. Handles hidden input fields on the login page.
4. Uses the same session to navigate to the overview page and scrape the nickname.

## Modules

- **mechanicalsoup**: For automating web browsing and form submission.
- **os**: For accessing environment variables.
- **csv**: For handling CSV files (if needed for future extensions).
- **dotenv**: For loading environment variables from a .env file.

## Installation

Ensure you have the required libraries installed:
```bash
pip install mechanicalsoup python-dotenv
```
## Usage

###
Create a `.env` file in the root directory with the following content:

    ```
    GITHUB_USERNAME=your_username
    GITHUB_PASSWORD=your_password
    ```

### Run the script:

From base directory, run the ff command
    ```bash
    python -m github_scraper.scraper
    ```


## Running Tests

To run the tests, you can use the `unittest` framework or `pytest`.

### Using `unittest`

1. Navigate to the root directory of the project:

    ```bash
    cd path/to/github_scraper
    ```

2. Run the tests:

    ```bash
    python -m unittest discover -s tests
    ```


### Using `pytest`

1. Ensure `pytest` is installed:

    ```bash
    pip install pytest
    ```

2. Run the tests:

    ```bash
    pytest
    ```
### Note
This script is for educational purposes only. Use it responsibly and ensure you comply with GitHub’s terms of service.

### Author
D. Okpala
### Date
28/08/2024
