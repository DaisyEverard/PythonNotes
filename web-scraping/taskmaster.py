import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import re

load_dotenv()
url = os.environ.get("URL")

headers = {'User-Agent': os.environ.get("USER_AGENT")}
html_page = requests.get(url)

soup = BeautifulSoup(html_page.content, 'lxml')

table_info = soup.find_all("table", class_=["wikitable", "sortable", "jquery-tablesorter"])[0]
table_headers = table_info.find_all("th")
table_headers.pop(0)
table_headers = [header.get_text().replace("\n", "") for header in table_headers]

table_rows = table_info.find_all("tr")
contestants = []

for i in range(1, len(table_rows)):
    # clean data to remove tags
    table_row = (str(table_rows[i])
                 .replace("\n", "")
                 .replace("</tr>", "")
                 .replace("</a>", "")
                 )
    table_row = re.sub(r"<tr\b[^>]*>", "", table_row)
    table_row = re.sub(r"<td\b[^>]*>", "", table_row)
    table_row = re.sub(r"<a\b[^>]*>", "", table_row)

    # turn each cell into a list  
    table_row_list = table_row.split("</td>")

    # some rows have an extra column for the series 'header'
    SERIES_NAMES = ["Series", "NYT", "CoC"]
    if table_row_list[0].startswith(tuple(SERIES_NAMES)):
        table_row_list.pop(0)

    # this is an empty column
    table_row_list.pop(13)

    contestants.append(table_row_list)
    # name = table_row_list[0]
    # total = table_row_list[11]
    # percentage_maximum = table_row_list[12]


print(table_headers)
print(contestants)



