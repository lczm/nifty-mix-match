import os
import re
import csv
import requests

from tqdm import tqdm
from pprint import pprint
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait

class Scraper():
    def __init__(self):
        self.company = []
        self.paths = []
        self.image_paths = []
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Firefox(options=self.options)

    def add_paths(self):
        # ensure that the file exists
        assert(os.path.isfile('./links.csv'))
        with open('./links.csv') as file:
            reader = csv.reader(file, delimiter=',', quotechar='|')
            next(reader, None)
            for row in reader:
                self.company.append(row[0])
                self.paths.append(row[1])

    def test_selenium(self):
        for i in tqdm(range(len(self.paths))):
            self.driver.get(self.paths[i])
            self.driver.implicitly_wait(2)
            elements = self.driver.find_elements_by_tag_name("img")
            for j in range(len(elements)):
                elements_src = elements[j].get_attribute("data-original")
                if elements_src != None and '.jpg' in elements_src:
                    item_id = elements_src[-10:-4]
                    title = elements[j].get_attribute("alt")
                    path = self.parse_uniqlo_url(elements_src)
                    temp = [self.company[i], item_id, title, path]
                    self.image_paths.append(temp)
        return 0

    def parse_uniqlo_url(self, string):
        replaced_string = 'https:' + string
        replaced_string = replaced_string.replace("medium1", "large")
        return replaced_string

    def parse_html(self):
        text = "Test"
        soup = BeautifulSoup(text, 'html.parser')
        print(soup.prettify())
        return 0

    def dump_csv(self):
        assert(len(self.image_paths) > 0)
        with open('paths.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['company', 'itemid', 'title', 'path'])
            for row in self.image_paths:
                spamwriter.writerow(row)
        return 0


def test():
    scraper = Scraper()
    scraper.add_paths()
    scraper.test_selenium()
    scraper.dump_csv()
    # scraper.scrape()
    return 0

if __name__ == "__main__":
    test()
