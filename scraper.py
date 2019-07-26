import os
import re
import csv
import time
import requests
import pandas as pd

from tqdm import tqdm
from pprint import pprint
from bs4 import BeautifulSoup


from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait

class Scraper():
    def __init__(self):
        self.companies = []
        self.gender = []
        self.paths = []
        self.category = []
        self.dump = []
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
                self.companies.append(row[0])
                self.gender.append(row[1])
                self.category.append(row[2])
                self.paths.append(row[3])

    def scrape_uniqlo(self, gender, category, path):
        # for i in tqdm(range(len(self.paths))):
        # self.driver.get(self.paths[i])
        self.driver.get(path)
        for _ in range(10):
            self.driver.implicitly_wait(2)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
        elements = self.driver.find_elements_by_tag_name("img")
        for j in range(len(elements)):
            elements_src = elements[j].get_attribute("data-original")
            if elements_src != None and '.jpg' in elements_src:
                item_id = elements_src[-10:-4]
                title = elements[j].get_attribute("alt")
                path = self.parse_uniqlo_url(elements_src)
                # data = [self.companies[i], item_id, title, path]
                # data = ['Uniqlo', item_id, title, path]
                data = ['Uniqlo', gender, category, title, path]
                self.dump.append(data)
                # self.image_paths.append(temp)
        return 0

    def parse_uniqlo_url(self, string):
        replaced_string = 'https:' + string
        replaced_string = replaced_string.replace("medium1", "large")
        return replaced_string

    def scrape_nike(self, gender, category, path):
        self.driver.get(path)
        for _ in range(10):
            self.driver.implicitly_wait(2)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
        elements = self.driver.find_elements_by_tag_name("picture")
        for i in range(len(elements)):
            image = elements[i].find_element_by_tag_name("img")
            path = image.get_attribute('src')
            title = image.get_attribute('alt')
            data = ['Nike', gender, category, title, path]
            self.dump.append(data)
        return 0

    def parse_html(self):
        text = "Test"
        soup = BeautifulSoup(text, 'html.parser')
        print(soup.prettify())
        return 0

    # use dump_csv after scrape_all() 
    def scrape_all(self):
        assert(len(self.companies) == len(self.paths))
        for i in tqdm(range(len(self.companies))):
            if self.companies[i] == 'Uniqlo':
                self.scrape_uniqlo(self.gender[i], self.category[i], self.paths[i])
            elif self.companies[i] == 'Nike':
                self.scrape_nike(self.gender[i], self.category[i], self.paths[i])
        return 0

    def dump_csv(self):
        assert(len(self.dump) > 0)
        with open('paths.csv', 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            csvwriter.writerow(['company', 'gender', 'category', 'title', 'path', 'itemid'])
            ids = [i for i in range(len(self.dump))]
            for i in range(len(self.dump)):
                self.dump[i].append(ids)
            for row in self.dump:
                csvwriter.writerow(row)
        return 0

    def add_item_id(self):
        assert(os.path.isfile('./paths.csv'))
            # csvwriter = csv.writer(csvfile, delimiter=' ',
            #                         quotechar='|', quoting=csv.QUOTE_MINIMAL)
        df = pd.read_csv('./paths.csv', delimiter=' ', quotechar='|')
        df.drop(['itemid'], axis=1)
        # df.assign('itemid' = [i for i in range(len(df))])
        df['itemid'] = [i for i in range(len(df))]
        df.to_csv('paths.csv', index=False, encoding='utf-8')
        return 0

if __name__ == "__main__":
    # scraper = Scraper()
    # scraper.add_paths()
    # scraper.scrape_all()
    # scraper.dump_csv()

    # scraper.add_item_id()
