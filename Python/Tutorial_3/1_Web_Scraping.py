"""
1_Web_Scraping.py

Author: Justin Petluk
Date: July 31, 2020

A Very brief introduction to webscraping.
Version 1.0 (will be added to)
"""


from bs4 import BeautifulSoup
import requests

# Handling local zipped files
from zipfile import ZipFile
import os

#global variable of local path to python documentation
WEB_PATH = "https://docs.python.org/3/tutorial/index.html"
LOCAL_PATH = "./Pages/python-3.8.5-docs-html/tutorial/index.html"

class Web_Scraper():
    #remember, init is like a constructor in other languages. This is where things should be 'initialized'
    def __init__(self):
        #self objects can be accessed anywhere publically from the object which the class creates
        self.data_dictionary = dict()

        # We will leave this empty for now to assign it later with the global variable.
        self.web_path = ""

        #Let's initialize an empty variable labeled with a '_' prefix to assume a hidden (private) variable.
        #This is to just make the WebScraper interface easier for later.
        self._soup = None


    def preprocess(self, string):
        """
        """
        pass

    
    def open_website(self, url):
        """
        """
        response = requests.get(url)
        #check if response is empty, passing it into "if" without any conditions returns true if not empty.
        if response:
            print("Request Successful.")
            print(response.text[:20] + "...")
        else:
            print("Request Failed.")
        
        self.soup = BeautifulSoup(response.text, 'html.parser')


    def open_local(self, path):
        """
        """
        with open(path, 'rb') as html:
            self.soup = BeautifulSoup (html, features = "html.parser") #create a new BS object

    def get_all(self, html_tag):
        """
        An HTML tag can be anything like <a> <b> <br> <p> <h1> .. <h5>, <li>.
        You can use these tags to help define what you are scraping.

        For example, any header texts (h1...h5) often are titles, while <p> are paragraph texts.
        For data analyists, this can be important based on what the author deems important, or to use this to parse a website structure

        this is basically a wrapper for beautiful soup
        """
        return self.soup.find_all(html_tag)


if __name__ == "__main__":
    scraper = Web_Scraper()

    Pages = os.listdir("./Pages") #check if any folders exist in pages, the zipped docs should be here but do not exist
    
    #only zip file exists, then extract it
    if len(Pages)  == 1:
        print("Unzipping")
        with ZipFile("./Pages/"+Pages[0], 'r') as zipObj:
            # Extract all the contents of zip file in current directory
            zipObj.extractall("./Pages/")

    scraper.open_local(LOCAL_PATH)

    print("Get all link titles!")
    a = scraper.get_all("a")
    for tag in a:
        print(tag.get_text())

    print("Get all link urls!")
    for tag in a:
        print(tag['href'])

    p = scraper.get_all("p")
    for tag in p:
        print(tag.get_text())

    ## The same code but for online website
    scraper.open_website(WEB_PATH)

    print("Get all link titles!")
    a = scraper.get_all("a")
    for tag in a:
        print(tag.get_text())

    print("Get all link urls!")
    for tag in a:
        print(tag['href'])

    p = scraper.get_all("p")
    for tag in p:
        print(tag.get_text())



