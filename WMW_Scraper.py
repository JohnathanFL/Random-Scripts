#!/usr/bin/python3

# If you want to change the chapters that get downloaded, just change startChap and endChap.
# If you want to change to a different story, just change the URL 
#   in "chapterData = requests.get("...")" to whatever the book uses.


from optparse import OptionParser
from bs4 import BeautifulSoup
from time import sleep
import requests

startChap = 551
endChap = 850

for i in range(startChap,endChap + 1):
    sleep(1)
    chapterData = requests.get("http://www.wuxiaworld.com/wmw-index/wmw-chapter-" + str(i))
    chapter = chapterData.text
    chapter = BeautifulSoup(chapter, 'lxml')
    chapContent = chapter.find("div", {"itemprop": "articleBody"})
    with open("Chapter " + str(i) + ".html", "w") as file:
        file.write(str(chapContent))
    
