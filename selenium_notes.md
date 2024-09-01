# Clarification of Selenium Automation Components

## 3 Components of Selenium Automation 

1. **Automation Tool**
   - **Selenium (itself)**: The primary tool used for browser automation.

2. **WebDriver (bridge)**
   - **Specific WebDriver**: The intermediary that enables Selenium to control a specific browser (e.g., ChromeDriver for Chrome, GeckoDriver for Firefox).

3. **Web Browser**
   - **Desired Browser**: The actual web browser to be automated, which must be installed separately on the machine like normal (e.g., Google Chrome, Mozilla Firefox).

## Installation Command

The command: 
```
pip install selenium webdriver-manager python-dotenv
```
installs:
- **Selenium**: The automation tool.
- **WebDriver Manager**: The utility to manage WebDrivers automatically.
- **Python-Dotenv**: The package for handling sensitive information securely.

## Note
The **actual web browser** must be installed through its normal installation process (e.g., downloading it from the official website) before it can be automated using Selenium, as modern web browsers typically come with their normal GUI mode but also their headless or non-GUI mode.
