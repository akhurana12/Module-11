#!/usr/bin/env python
# coding: utf-8

# # Module 12 Challenge
# ## Deliverable 1: Scrape Titles and Preview Text from Mars News

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup


# In[2]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service = Service(executable_path=r"C:\Users\USER\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe")
browser=Browser('chrome',service=service)


# In[3]:


browser = Browser('chrome')


# In[4]:


get_ipython().system('pip install requests beautifulsoup4')


# ### Step 1: Visit the Website
# 
# 1. Use automated browsing to visit the [Mars news site](https://static.bc-edx.com/data/web/mars_news/index.html). Inspect the page to identify which elements to scrape.
# 
#       > **Hint** To identify which elements to scrape, you might want to inspect the page by using Chrome DevTools.

# In[5]:


import requests
from bs4 import BeautifulSoup


# In[6]:


# Visit the Mars news site
url = 'https://static.bc-edx.com/data/web/mars_news/index.html'


# ### Step 2: Scrape the Website
# 
# Create a Beautiful Soup object and use it to extract text elements from the website.

# In[7]:


# Create a Beautiful Soup object
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')


# In[8]:


# Extract all the text elements
all_text = soup.get_text()
print(all_text)


# ### Step 3: Store the Results
# 
# Extract the titles and preview text of the news articles that you scraped. Store the scraping results in Python data structures as follows:
# 
# * Store each title-and-preview pair in a Python dictionary. And, give each dictionary two keys: `title` and `preview`. An example is the following:
# 
#   ```python
#   {'title': "NASA's MAVEN Observes Martian Light Show Caused by Major Solar Storm", 
#    'preview': "For the first time in its eight years orbiting Mars, NASA’s MAVEN mission witnessed two different types of ultraviolet aurorae simultaneously, the result of solar storms that began on Aug. 27."
#   }
#   ```
# 
# * Store all the dictionaries in a Python list.
# 
# * Print the list in your notebook.

# In[9]:


# Create an empty list to store the dictionaries
all_divs=soup.find_all('div')
all_divs[0]


# In[10]:


pandas_info_dict={}


# In[11]:


for div in all_divs:
    des= div.find('h2').text
    urls=[ link['href'] for link in div.find_all('a') ]
    print(des)
    print(urls)
    pandas_info_dict[des] = urls
    break


# In[12]:


all_urls=[ link['href'] for link in soup.find_all('a')]
all_urls


# In[13]:


# Print the list to confirm success
pandas_info_dict


# In[14]:


browser.quit()

