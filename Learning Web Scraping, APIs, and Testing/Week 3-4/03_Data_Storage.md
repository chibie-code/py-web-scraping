## File: 03_Data_Storage.md

### Data Storage
- **Saving Scraped Data to CSV, JSON, or Databases**
  - **CSV**: Use Python's built-in `csv` module to write data to CSV files.
    ```python
    import csv

    with open('data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Column1', 'Column2'])  # Header
        writer.writerow(['Value1', 'Value2'])      # Data
    ```
  - **JSON**: Use Python's built-in `json` module to save data in JSON format.
    ```python
    import json

    data = {'key': 'value'}
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)
    ```
  - **Databases**: Use libraries like `sqlite3` for local databases or `SQLAlchemy` for more complex database interactions.
    ```python
    import sqlite3

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS data (column1 TEXT, column2 TEXT)')
    c.execute('INSERT INTO data (column1, column2) VALUES (?, ?)', ('Value1', 'Value2'))
    conn.commit()
    conn.close()
    ```
