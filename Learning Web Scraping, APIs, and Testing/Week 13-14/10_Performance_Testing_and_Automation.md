## File: 10_Performance_Testing_and_Automation.md

### Week 13-14: Performance Testing and Automation

- **Performance Testing**
  - **Assessing the Performance of Scraping Scripts and API Calls**
    - Measure response times and resource usage.
    - Tools: `time`, `cProfile`, or third-party libraries like `locust`.

- **Test Automation**
  - **Automating Tests with CI/CD Tools**
    - Integrate testing into your Continuous Integration/Continuous Deployment pipeline.
    - Example tools: Jenkins, GitHub Actions, Travis CI.

- **Exploring Selenium for Testing**
  - **Using Selenium for End-to-End Testing of Web Applications**
    - Automate browser interactions to test web applications.
    - Example of a basic Selenium test:
      ```python
      from selenium import webdriver

      driver = webdriver.Chrome()
      driver.get('https://example.com')
      assert 'Example Domain' in driver.title
      driver.quit()
      ```

---
