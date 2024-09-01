import requests
from bs4 import BeautifulSoup
import os
import csv
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def simple_extracted_profile_data(session, profile_url):
    # Extract profile data
    response = session.get(profile_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    nickname_element = soup.find(class_='p-nickname').text
    name_element = soup.find(class_='p-name').text
    name = name_element if name_element else nickname_element
    bio = soup.find(class_='p-note').text
    followers = None  # Followers extraction can be added if needed
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
        followers = "None"  # Default to None if not provided

        writer.writerow([name, bio, followers])

    print("Data saved to", filename)

def github_login(session):
    # Open GitHub login page
    login_url = "https://github.com/login"
    response = session.get(login_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print("Opened GitHub login page")

    # Extract authenticity token
    authenticity_token = soup.find('input', {'name': 'authenticity_token'})['value']

    # Prepare login data
    login_data = {
        'login': os.getenv('GITHUB_USERNAME'),
        'password': os.getenv('GITHUB_PASSWORD'),
        'authenticity_token': authenticity_token # the hidden input
    }

    # Submit the login form
    response = session.post('https://github.com/session', data=login_data)
    print("Submitted login form")

    # Check if login was successful
    if 'login' in response.url:
        print("Login failed: still on login page")
        return None
    else:
        print("Login successful")
        return session

def requests_automate():
    # Create a session object
    session = requests.Session()

    try:
        session = github_login(session)

        # Navigate to the user's profile page
        profile_url = f'https://github.com/{os.getenv("GITHUB_USERNAME")}'
        response = session.get(profile_url)
        print("Navigated to user profile page")

        extracted_data = simple_extracted_profile_data(session, profile_url)

        name = extracted_data['name']
        bio = extracted_data['bio']
        followers = extracted_data['followers']

        # Print extracted data
        print(f"Name: {name}, Bio: {bio}, Followers: {followers}")
        simple_save_data_to_csv(extracted_data)

    except Exception as e:
        print(f"When trying to login, an error occurred: {str(e)}")

if __name__ == "__main__":
    requests_automate()
