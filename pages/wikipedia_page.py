from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class WikipediaPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_input = (By.NAME, "search")
        self.search_button = (By.CLASS_NAME, "pure-button-primary-progressive")
        self.article_title = (By.ID, "firstHeading")

    def open(self):
        self.driver.get("https://es.wikipedia.org")

    def search(self, term):
        search_box = self.driver.find_element(*self.search_input)
        search_box.send_keys(term)
        search_box.send_keys(Keys.RETURN)  # Presionar Enter


    def get_article_title(self):
        return self.driver.find_element(*self.article_title).text
