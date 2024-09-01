## File: 07_Advanced_API_Usage.md

### Week 7-8: Advanced API Usage

- **Authentication and Authorization**
  - **Understanding API Keys**
    - API keys are unique identifiers used to authenticate requests made to an API.
    - Typically passed in the request header or as a query parameter.
    - Example of using an API key:
      ```python
      import requests

      api_key = 'your_api_key'
      headers = {'Authorization': f'Bearer {api_key}'}
      response = requests.get('https://api.example.com/data', headers=headers)
      ```
  - **OAuth**
    - OAuth is a protocol that allows applications to access user data without exposing passwords.
    - Commonly used for third-party applications (e.g., logging in with Google or Facebook).
    - Involves multiple steps: obtaining authorization, requesting access tokens, and making API requests.

- **Error Handling**
  - **Handling API Errors**
    - Check the response status code to determine if an error occurred:
      - **200**: Success
      - **400**: Bad Request
      - **401**: Unauthorized
      - **404**: Not Found
      - **500**: Internal Server Error
    - Example of error handling:
      ```python
      response = requests.get('https://api.example.com/data')
      if response.status_code == 200:
          data = response.json()
      else:
          print(f'Error: {response.status_code} - {response.text}')
      ```
  - **Rate Limits**
    - Most APIs have rate limits to control the number of requests made in a given time period.
    - Handle rate limits by checking the response headers for rate limit information and implementing back-off strategies:
      ```python
      if 'X-RateLimit-Remaining' in response.headers:
          remaining = int(response.headers['X-RateLimit-Remaining'])
          if remaining == 0:
              reset_time = int(response.headers['X-RateLimit-Reset'])
              print(f'Rate limit exceeded. Try again at {reset_time}.')
      ```

- **Integrating APIs into Applications**
  - **Building Small Projects that Consume APIs**
    - Start with simple projects to practice integrating APIs into your applications.
    - Project Ideas:
      - **Weather App**: Use a weather API to display current weather conditions.
      - **Todo List**: Create a todo list application that interacts with a task management API.
      - **News Aggregator**: Build an app that pulls news articles from a news API.
    - Example of a simple project structure:
      ```plaintext
      /my_api_project
      ├── app.py          # Main application file
      ├── requirements.txt # List of dependencies
      └── README.md       # Project documentation
      ```
