import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os


load_dotenv()
url = os.environ.get("URL")

headers = {'User-Agent': os.environ.get("USER_AGENT")}
html_page = requests.get(url)

soup = BeautifulSoup(html_page.content, 'lxml') # content, parser

title = soup.title # can access title and some others directory
title = soup.find("title")
# return first instance of a title tag <class 'bs4.element.Tag'>
title = soup.find("title").get_text()
# removes the <title> tags from around the title text

paragraphs = soup.find_all("p")
# returns list of all paragraphs <class 'bs4.element.ResultSet'>

page_header = soup.find_all("div", id="page-header")
# all of the raw html in the #page_header div wrapped in [square brackets]
# you can also search via class
page_header = page_header[0].find("h1").get_text()
# this could have been chained to the find all line.


