#!/usr/bin/python3

from optparse import OptionParser
from bs4 import BeautifulSoup
from time import sleep
import requests


for i in range(551,851):
    sleep(1)
    chapterData = requests.get("http://www.wuxiaworld.com/wmw-index/wmw-chapter-" + str(i))
    chapter = chapterData.text
    chapter = BeautifulSoup(chapter, 'lxml')
    chapContent = chapter.find("div", {"itemprop": "articleBody"})
    with open("Chapter " + str(i) + ".html", "w") as file:
        file.write(str(chapContent))
    
