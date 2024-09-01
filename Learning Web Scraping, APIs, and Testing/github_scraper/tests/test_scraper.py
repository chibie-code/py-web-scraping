import unittest
from unittest.mock import patch, MagicMock
import mechanicalsoup
from github_scraper.scraper import load_env_variables, create_browser, login_to_github, scrape_nickname

class TestGitHubScraper(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # print("Test cases begin [class setUpClass]")
        pass

    @classmethod
    def tearDownClass(cls):
        # print("Test cases end [class tearDownClass]")
        pass

    def setUp(self):
        self.username = 'test_user'
        self.password = 'test_pass'
            # print(f"Setting up for {self._testMethodName}")

    def tearDown(self):
        # print(f"Tearing down for {self._testMethodName}")
        pass

    @patch('github_scraper.scraper.load_dotenv')
    @patch('github_scraper.scraper.os.getenv')
    def test_load_env_variables(self, mock_getenv, mock_load_dotenv):
        # preset the mock/test env values because "load_env_variables" would run the "load_dotenv()" and then retrieve the values using "getenv"
        mock_getenv.side_effect = ['test_user', 'test_pass']
        # would run the mock versions of "load_dotenv()" and then retrieve the values using "getenv"
        username, password = load_env_variables()
        self.assertEqual(username, 'test_user')
        self.assertEqual(password, 'test_pass')

    def test_create_browser(self):
        sb = create_browser()
        self.assertIsInstance(sb, mechanicalsoup.StatefulBrowser)

    @patch('mechanicalsoup.StatefulBrowser')
    def test_login_to_github_success(self, mock_sb): # mock_sb mocks "sb" which is an instance of StatefulBrowser
        # Arrange
        mock_sb.open = MagicMock()
        mock_sb.select_form = MagicMock()
        mock_sb.submit_selected = MagicMock(return_value='mock_response')
        # call the method being tested
        response = login_to_github(mock_sb, self.username, self.password)

        # assert to ensure that "mock_sb.open()"  is called on the url parameter ("https://github.com/login") exactly once
        mock_sb.open.assert_called_once_with("https://github.com/login")

        # assert to ensure that "mock_sb.select_form()" on the css-selector string parameter/form selector ('form[action="/session"]') exactly once
        mock_sb.select_form.assert_called_once_with('form[action="/session"]')

        # assert to ensure, for the mock_sb, the key whose value is being assigned is "login" and the value is "self.username"
        mock_sb.__setitem__.assert_any_call("login", self.username)

        # assert to ensure, for the mock_sb, the key whose value is being assigned is "password" and the value is "self.password"
        mock_sb.__setitem__.assert_any_call("password", self.password)

        # assert to ensure that "mock_sb.submit_selected()" is called exactly once
        mock_sb.submit_selected.assert_called_once()

        # finally test the final response of the function to makes sure the expected outcome "mock_response" is returned
        self.assertEqual(response, 'mock_response')

    @patch('mechanicalsoup.StatefulBrowser')
    def test_login_to_github_failure(self, MockBrowser):
        @patch('mechanicalsoup.StatefulBrowser')
        def test_login_to_github_success(self, mock_sb): # mock_sb mocks "sb" which is an instance of StatefulBrowser
            # Arrange
            mock_sb.open = MagicMock()
            mock_sb.select_form = MagicMock()
            mock_sb.submit_selected = MagicMock(return_value='mock_response')
            # call the method being tested
            response = login_to_github(mock_sb, self.username, self.password)

            # assert to ensure that "mock_sb.open()"  is called on the url parameter ("https://github.com/login") exactly once
            mock_sb.open.assert_called_once_with("https://github.com/login")

            # assert to ensure that "mock_sb.select_form()" on the css-selector string parameter/form selector ('form[action="/session"]') exactly once
            mock_sb.select_form.assert_called_once_with('form[action="/session"]')

            # assert to ensure, for the mock_sb, the key whose value is being assigned is "login" and the value is "self.username"
            mock_sb.__setitem__.assert_any_call("login", self.username)

            # assert to ensure, for the mock_sb, the key whose value is being assigned is "password" and the value is "self.password"
            mock_sb.__setitem__.assert_any_call("password", self.password)

            # assert to ensure that "mock_sb.submit_selected()" is called exactly once
            mock_sb.submit_selected.assert_called_once()

            # finally test the final response of the function to makes sure the expected outcome "mock_response" is returned
            self.assertEqual(response, 'mock_response')

    @patch('mechanicalsoup.StatefulBrowser')
    def test_login_to_github_invalid_credentials(self, MockBrowser):
        # Arrange
        mock_sb = MockBrowser.return_value
        mock_sb.open = MagicMock()
        mock_sb.select_form = MagicMock()
        mock_sb.submit_selected = MagicMock(return_value='invalid_response')  # Simulated invalid response

        # Act
        response = login_to_github(mock_sb, "invalid_username", "invalid_password")

        # Assert
        mock_sb.open.assert_called_once_with("https://github.com/login")
        mock_sb.select_form.assert_called_once_with('form[action="/session"]')
        mock_sb.__setitem__.assert_any_call("login", "invalid_username")
        mock_sb.__setitem__.assert_any_call("password", "invalid_password")
        mock_sb.submit_selected.assert_called_once()
        self.assertEqual(response, 'invalid_response')

    @patch('mechanicalsoup.StatefulBrowser')
    def test_login_to_github_form_selection_failure(self, MockBrowser):
        # Arrange
        mock_sb = MockBrowser.return_value
        mock_sb.open = MagicMock()
        mock_sb.select_form.side_effect = Exception("Form not found")  # Simulate an exception

        # Act
        response = login_to_github(mock_sb, self.username, self.password)

        # Assert
        mock_sb.open.assert_called_once_with("https://github.com/login")
        mock_sb.select_form.assert_called_once_with('form[action="/session"]')
        self.assertIsNone(response)  # Expect None due to form selection failure

    @patch('mechanicalsoup.StatefulBrowser')
    def test_login_to_github_empty_credentials(self, MockBrowser):
        # Arrange
        mock_sb = MockBrowser.return_value
        mock_sb.open = MagicMock()
        mock_sb.select_form = MagicMock()
        mock_sb.submit_selected = MagicMock(return_value='mock_response')

        # Act
        response = login_to_github(mock_sb, "", "")  # Testing with empty credentials

        # Assert
        mock_sb.open.assert_called_once_with("https://github.com/login")
        mock_sb.select_form.assert_called_once_with('form[action="/session"]')
        mock_sb.__setitem__.assert_any_call("login", "")
        mock_sb.__setitem__.assert_any_call("password", "")
        mock_sb.submit_selected.assert_called_once()
        self.assertEqual(response, 'mock_response')  # Assuming the function still returns a response

    @patch('mechanicalsoup.StatefulBrowser')
    def test_scrape_nickname_success(self, MockBrowser):
        # Arrange
        mock_sb = MockBrowser.return_value
        mock_sb.open = MagicMock()

        # Mocking the page object returned by the browser
        mock_sb.page = MagicMock()
        mock_sb.page.find.return_value = MagicMock(get_text=MagicMock(return_value='chibie-code'))

        # Act
        nickname = scrape_nickname(mock_sb)

        # Assert
        mock_sb.open.assert_called_once_with("https://github.com/chibie-code")
        self.assertEqual(nickname, 'chibie-code')

    @patch('mechanicalsoup.StatefulBrowser')
    def test_scrape_nickname_page_load_failure(self, MockBrowser):
        # Arrange
        mock_sb = MockBrowser.return_value
        mock_sb.open = MagicMock()
        mock_sb.page = None  # Simulating page load failure

        # Act
        nickname = scrape_nickname(mock_sb)

        # Assert
        mock_sb.open.assert_called_once_with("https://github.com/chibie-code")
        self.assertIsNone(nickname)  # Expect None due to page load failure

    @patch('mechanicalsoup.StatefulBrowser')
    def test_scrape_nickname_element_not_found(self, MockBrowser):
        # Arrange
        mock_sb = MockBrowser.return_value
        mock_sb.open = MagicMock()
        mock_sb.page = MagicMock()
        mock_sb.page.find.return_value = None  # Simulating nickname element not found

        # Act
        nickname = scrape_nickname(mock_sb)

        # Assert
        mock_sb.open.assert_called_once_with("https://github.com/chibie-code")
        self.assertIsNone(nickname)  # Expect None since nickname element is not found

    @patch('mechanicalsoup.StatefulBrowser')
    def test_scrape_nickname_unexpected_structure(self, MockBrowser):
        # Arrange
        mock_sb = MockBrowser.return_value
        mock_sb.open = MagicMock()
        mock_sb.page = MagicMock()
        mock_sb.page.find.return_value = MagicMock(get_text=MagicMock(return_value=''))  # Empty nickname

        # Act
        nickname = scrape_nickname(mock_sb)

        # Assert
        mock_sb.open.assert_called_once_with("https://github.com/chibie-code")
        self.assertEqual(nickname, '')  # Expect empty string since nickname is empty




if __name__ == '__main__':
    unittest.main()


"""
Explanation
test_load_env_variables: Tests the load_env_variables function to ensure it correctly loads the environment variables.
test_create_browser: Tests the create_browser function to ensure it returns an instance of StatefulBrowser.
test_login_to_github: Tests the login_to_github function to ensure it correctly logs in and returns the expected response URL.
test_scrape_nickname: Tests the scrape_nickname function to ensure it correctly scrapes the nickname from the overview page.
"""
