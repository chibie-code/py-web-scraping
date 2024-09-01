# Importing the main WebDriver (bridge) class to control the browser
from selenium import webdriver

# Importing By to locate elements in the DOM
from selenium.webdriver.common.by import By

# Importing Service to manage the ChromeDriver service
from selenium.webdriver.chrome.service import Service

# Importing expected_conditions for waiting for specific conditions
from selenium.webdriver.support import expected_conditions as EC

# Importing WebDriverWait to implement explicit waits
from selenium.webdriver.support.ui import WebDriverWait

# Import Options for headless mode
from selenium.webdriver.chrome.options import Options

# Importing ChromeDriverManager to automatically manage ChromeDriver binaries
from webdriver_manager.chrome import ChromeDriverManager

# Importing os module to interact with the operating system's or specifically .env file variables
import os

# Importing csv module to handle CSV file operations like saving/exporting your scraped data to a local file
import csv

import time

from dotenv import load_dotenv

import traceback

"""
This script automates the process of logging into GitHub, extracting profile data, and saving it to a CSV file using Selenium.

The script performs the following steps:
1. Loads environment variables from a .env file, including GitHub login credentials.
2. Defines functions to:
   - Extract profile data from the GitHub profile page.
   - Save the extracted data to a CSV file.
   - Automate the GitHub login process using Selenium.
3. Sets up a headless Chrome browser using Selenium WebDriver.
4. Automates the login process to GitHub.
5. Navigates to the user's GitHub profile page and extracts profile data (name, bio, followers).
6. Saves the extracted profile data to a CSV file.
7. Handles exceptions and captures error screenshots if login fails.
8. Closes the browser session after completing the tasks.

Dependencies:
- selenium: For browser automation.
- webdriver_manager: For managing browser drivers.
- BeautifulSoup: For parsing HTML content.
- requests: For making HTTP requests.
- dotenv: For loading environment variables.
- csv: For handling CSV file operations.
- os: For interacting with the operating system.
- time: For adding delays.
- traceback: For capturing and printing error tracebacks.

Usage:
1. Ensure you have a .env file with your GitHub credentials:
   GITHUB_USERNAME=your_username
   GITHUB_PASSWORD=your_password
2. Run the script to automate the login process and extract profile data.

Note:
- This script is based on the article "Automate Website Login with Python and Selenium" by Sunil Kumawat.
  Link: https://medium.com/@Sunil_Kumawat/automate-website-login-with-python-and-selenium-a-step-by-step-guide-a4d3871f22ca
"""

# *Load environment variables from .env file
load_dotenv()

def simple_extracted_profile_data(webdriver):
    # Extract profile data
    nickname_element = WebDriverWait(webdriver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'p-nickname'))
    ).text
    name_element = WebDriverWait(webdriver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'p-name'))
    ).text
    name = name_element if name_element else nickname_element
    bio = webdriver.find_element(By.CLASS_NAME, 'p-note').text
    followers = None #webdriver.find_element(By.XPATH, "//a[contains(@href, 'followers')]/span").text
    return {
        'name': name,
        'bio': bio,
        'followers': followers
    }

def simple_save_data_to_csv(data={}, filename='github_profile_data.csv'):
    # Check if the file already exists
    file_exists = os.path.isfile(filename)

    # Save data to a CSV file
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write the header only if the file is new
        if not file_exists:
            writer.writerow(['name', 'bio', 'followers'])

        # Validate and clean data
        name = data.get('name', 'N/A')
        bio = data.get('bio', 'N/A') or 'No bio available'
        followers = "None" # data.get('followers', '0')  # Default to 0 if not provided

        writer.writerow([name, bio, followers])

    print("Data saved to", filename)

def github_login(chrome_web_driver):
    # make selenium open the GitHub login page using the chrome_web_driver we instantiated
    chrome_web_driver.get("https://github.com/login")

    # for visual confirmation, print to console that the login page is opened in your headless chrome Browser
    print("Opened GitHub login page")

    # make the chrome driver find the login form's fields and buttons to automate inputting the login credentials
    # Explicit Wait for the username field to be present
    github_username_field = WebDriverWait(chrome_web_driver, 5).until(
        EC.presence_of_element_located((By.ID, 'login_field'))
    )

    # Explicit Wait for the password field to be present
    github_password_field = WebDriverWait(chrome_web_driver, 5).until(
        EC.presence_of_element_located((By.ID, 'password'))
    )

    # Explicit Wait for the login button to be clickable
    github_login_button = WebDriverWait(chrome_web_driver, 5).until(
        EC.element_to_be_clickable((By.NAME, 'commit'))
    )

    # enter the username and password, directly from the .env file, into the fields using 'field_variable.send_keys()'
    github_username_field.send_keys(os.getenv('GITHUB_USERNAME'))
    github_password_field.send_keys(os.getenv('GITHUB_PASSWORD'))

    # click the login button
    github_login_button.click()

    # wait for page to load after login and verify that login was successful
    WebDriverWait(chrome_web_driver, 10).until(
        EC.url_changes('https://github.com/login')
    )

    # the current url after login either failed or was successful
    current_url = chrome_web_driver.current_url
    if 'login' in current_url: # if you are still on the login page, it means the login wasn't successful
        print("login failed: still on login page")
        return None
    else:
        print("login successful")
        return chrome_web_driver

def selenium_automate():
    # specify which browser the webdriver service is for
    webdriver_service = Service( ChromeDriverManager().install() )
    # I would like to run the browser being automated in headless mode, so the ff options are going to ensure that
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless") # make the browser headless
    chrome_options.add_argument("--no-sandbox") # Optional: for certian environments
    chrome_options.add_argument("--disable-dev-shm-usage") # Optional: overcome limited resources problems

    # create an instance of the chrome Webdriver you'll use to breidge the connection between the automation tool (selenium) and the chrome web Browser
    chrome_web_driver = webdriver.Chrome(
        service=webdriver_service,
        options=chrome_options
    )

    try:
        chrome_web_driver = github_login(chrome_web_driver)

        # Navigate to the user's profile page
        chrome_web_driver.get(f'https://github.com/{os.getenv("GITHUB_USERNAME")}')
        print("Navigated to user profile page")

        extracted_data = simple_extracted_profile_data(chrome_web_driver)

        name = extracted_data['name']
        bio = extracted_data['bio']
        followers = extracted_data['followers']

        # Print extracted data
        print(f"Name: {name}, Bio: {bio}, Followers: {followers}")
        simple_save_data_to_csv(extracted_data)

    # if an error occured while attempting to login with automated selenium,
    # an exception is thrown and you print to the console the error message
    # and save the screenshot of the actual chrome web browser in that error state to the current directory
    except Exception as e:
        # Capture the traceback and print it
        tb_str = traceback.format_exception(type(e), e, e.__traceback__)
        print(f"When trying to login, an error occurred: {''.join(tb_str)}")
        # driver.save_screenshot("error_screenshot.png")
    finally:
        # close/end the instance of this chrome webdriver
        chrome_web_driver.quit()

if __name__ == "__main__":
    selenium_automate()  # Calls the main function if the script is run directly
