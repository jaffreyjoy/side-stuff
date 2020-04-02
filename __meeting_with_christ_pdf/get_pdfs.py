import urllib
from bs4 import BeautifulSoup
import requests
import os


def fetch_file(prefix, route):
    url = f"http://www.meetingwithchrist.com/{route}"
    r = requests.get(url, stream=True)
    filename = f"PDFs/{prefix}. {urllib.parse.unquote(route)[4:]}"
    print(filename)
    with open(filename, "wb") as file:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)

with open("html/Meeting With Christ.html", "r") as html:
    html_doc = html.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    nodesList = soup.find_all("a")
    all_links = list(map(lambda node: node['href'], nodesList))
    # print(all_links[0])
    req_links = list(filter(lambda link: link[0:3]=="pdf", all_links))
    nline = "\n"
    # print(nline.join(req_links))
    for index, route in enumerate(req_links):
        fetch_file(index+1, route)

