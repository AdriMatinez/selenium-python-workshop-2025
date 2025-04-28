from selenium.webdriver.common.by import By

class WikipediaPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_input = (By.NAME, "search")
        self.search_button = (By.CLASS_NAME, "pure-button-primary-progressive")
        self.article_title = (By.ID, "firstHeading")

    def open(self):
        self.driver.get("https://es.wikipedia.org")

    def search(self, term):
        self.driver.find_element(*self.search_input).send_keys(term)
        self.driver.find_element(*self.search_button).click()

    def get_article_title(self):
        return self.driver.find_element(*self.article_title).text
