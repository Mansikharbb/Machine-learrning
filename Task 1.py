#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import requests
import re
from bs4 import BeautifulSoup
import sys

def get_page(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup

def clean(text):
    rep = {"<br>": "\n", "<br/>": "\n", "<li>":  "\n"}
    rep = dict((re.escape(k), v) for k, v in rep.items()) 
    pattern = re.compile("|".join(rep.keys()))
    text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)
    text = re.sub(r'\<(.*?)\>', '', text)  # Corrected line
    return text

def collect_text(soup):
    text = ''
    para_text = soup.find_all('p')
    for para in para_text:
        text += f"{para.text}\n\n"
    return text

def save_file(text, url):
    if not os.path.exists('./scraped_articles'):
        os.mkdir('./scraped_articles')
    name = url.split("/")[-1]
    fname = f'scraped_articles/{name}.txt'
    with open(fname, 'w') as f:
        f.write(text)

url = "https://medium.com/@johnDoe/how-to-scrape-medium-articles-using-python-123456"
soup = get_page(url)
text = collect_text(soup)
text = clean(text)
save_file(text, url)


# In[ ]:





# In[ ]:




