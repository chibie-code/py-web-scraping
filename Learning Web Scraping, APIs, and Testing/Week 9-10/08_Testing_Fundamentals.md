## File: 08_Testing_Fundamentals.md

### Week 9-10: Testing Fundamentals

- **Introduction to Testing**
  - **Importance of Testing in Software Development**
    - Ensures software reliability and functionality.
    - Helps identify and fix bugs before deployment.
    - Facilitates code maintenance and refactoring.

- **Unit Testing**
  - **Writing Unit Tests with `unittest` or `pytest`**
    - **`unittest`**: A built-in Python module for creating and running tests.
      - Example of a simple unit test:
        ```python
        import unittest

        def add(a, b):
            return a + b

        class TestMathFunctions(unittest.TestCase):
            def test_add(self):
                self.assertEqual(add(2, 3), 5)

        if __name__ == '__main__':
            unittest.main()
        ```
    - **`pytest`**: A more flexible testing framework that simplifies test writing.
      - Example of a simple unit test using `pytest`:
        ```python
        def add(a, b):
            return a + b

        def test_add():
            assert add(2, 3) == 5
        ```

- **Mocking and Stubbing**
  - **Using Mock Objects to Simulate API Responses**
    - Mocking allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.
    - Example using `unittest.mock`:
      ```python
      from unittest.mock import Mock

      mock_api = Mock()
      mock_api.get_data.return_value = {'key': 'value'}
      response = mock_api.get_data()
      assert response['key'] == 'value'
      ```