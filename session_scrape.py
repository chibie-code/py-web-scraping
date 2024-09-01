import requests

"""
This script logs into a website, retrieves a session cookie, and uses that cookie for subsequent requests to stay logged in.

It performs the following tasks:
1. Defines the login URL and the URL of the page to be accessed after login.
2. Sets up the headers to mimic a browser request, including the essential 'User-Agent' header.
3. Submits the login credentials to the login URL.
4. Retrieves the session cookie from the login response.
5. Uses the session cookie to make subsequent requests while staying logged in.
"""

# URL of the login page
login_url = "https://www.scrapethissite.com/pages/advanced/?gotcha=login"

# URL of the page to be accessed after login
target_url = "https://www.scrapethissite.com/pages/advanced/?gotcha=login"

# Login credentials (replace with actual credentials)
login_data = {
    "username": "your_username",
    "password": "your_password"
}

# Headers to make the request appear as if it's coming from a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "referrer": "https://www.scrapethissite.com/pages/advanced/"
}

# Create a session object to persist cookies
session = requests.Session()

# Make the login request
login_response = session.post(login_url, data=login_data, headers=headers)

# Check if the login was successful
if login_response.status_code == 200:
    print("Login successful. Status code: 200")

    # Use the session object to make subsequent requests
    response = session.get(target_url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        print("Accessed target page successfully. Status code: 200")
        print(response.text)  # Print the content of the page
    else:
        print(f"Failed to access target page. Status code: {response.status_code}")
else:
    print(f"Login failed. Status code: {login_response.status_code}")
