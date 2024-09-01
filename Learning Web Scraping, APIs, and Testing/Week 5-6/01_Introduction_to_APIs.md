## File: 01_Introduction_to_APIs.md

### Week 5-6: Introduction to APIs

- **Understanding APIs**
  - **What is an API?**
    - An **API (Application Programming Interface)** is a set of rules that allows different software applications to communicate with each other.
    - APIs enable developers to access and interact with the functionality or data of another application or service.
  - **Types of APIs**
    - **RESTful APIs**: 
      - Use standard HTTP methods (GET, POST, PUT, DELETE).
      - Typically return data in JSON format.
      - Stateless communication.
    - **GraphQL**:
      - A query language for APIs that allows clients to request only the data they need.
      - Provides a single endpoint for requests, making it flexible and efficient.

- **Making API Requests**
  - **Using the Requests Library in Python**
    - The `requests` library is a simple and intuitive way to make HTTP requests in Python.
    - Installation:
      ```bash
      pip install requests
      ```
    - **GET Request Example**:
      ```python
      import requests

      response = requests.get('https://api.example.com/data')
      data = response.json()  # Parse JSON response
      print(data)
      ```
    - **POST Request Example**:
      ```python
      import requests

      payload = {'key': 'value'}
      response = requests.post('https://api.example.com/data', json=payload)
      print(response.status_code)  # Check status code
      ```
    - **PUT and DELETE Requests**:
      ```python
      # PUT Request
      update_payload = {'key': 'new_value'}
      put_response = requests.put('https://api.example.com/data/1', json=update_payload)

      # DELETE Request
      delete_response = requests.delete('https://api.example.com/data/1')
      ```

- **Working with JSON and XML**
  - **Parsing JSON Responses**
    - JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy to read and write.
    - Example of parsing JSON:
      ```python
      json_data = '{"name": "Alice", "age": 30}'
      parsed_data = json.loads(json_data)  # Convert JSON to Python dictionary
      print(parsed_data['name'])  # Output: Alice
      ```
  - **Parsing XML Responses**
    - XML (eXtensible Markup Language) is a markup language that defines rules for encoding documents.
    - You can use libraries like `xml.etree.ElementTree` to parse XML in Python:
      ```python
      import xml.etree.ElementTree as ET

      xml_data = '''<person><name>Alice</name><age>30</age></person>'''
      root = ET.fromstring(xml_data)
      print(root.find('name').text)  # Output: Alice
      ```
