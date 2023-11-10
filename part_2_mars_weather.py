#!/usr/bin/env python
# coding: utf-8

# # Module 12 Challenge
# ## Deliverable 2: Scrape and Analyze Mars Weather Data

# In[1]:


# Import relevant libraries
from splinter import Browser
from bs4 import BeautifulSoup as soup
import matplotlib.pyplot as plt
import pandas as pd


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
# Use automated browsing to visit the [Mars Temperature Data Site](https://static.bc-edx.com/data/web/mars_facts/temperature.html). Inspect the page to identify which elements to scrape.
# 
#    > **Hint** To identify which elements to scrape, you might want to inspect the page by using Chrome DevTools to discover whether the table contains usable classes.
# 

# In[5]:


import requests
from bs4 import BeautifulSoup


# In[6]:


# Visit the website
# https://static.bc-edx.com/data/web/mars_facts/temperature.html
url = "https://static.bc-edx.com/data/web/mars_facts/temperature.html"


# ### Step 2: Scrape the Table
# 
# Create a Beautiful Soup object and use it to scrape the data in the HTML table.
# 
# Note that this can also be achieved by using the Pandas `read_html` function. However, use Beautiful Soup here to continue sharpening your web scraping skills.

# In[7]:


# Create a Beautiful Soup Object
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')


# In[8]:


# Extract all rows of data
data_rows = soup.find_all('tr')
all_text = soup.get_text()
print(all_text)


# In[9]:


print(data_rows)


# ### Step 3: Store the Data
# 
# Assemble the scraped data into a Pandas DataFrame. The columns should have the same headings as the table on the website. Here’s an explanation of the column headings:
# 
# * `id`: the identification number of a single transmission from the Curiosity rover
# * `terrestrial_date`: the date on Earth
# * `sol`: the number of elapsed sols (Martian days) since Curiosity landed on Mars
# * `ls`: the solar longitude
# * `month`: the Martian month
# * `min_temp`: the minimum temperature, in Celsius, of a single Martian day (sol)
# * `pressure`: The atmospheric pressure at Curiosity's location

# In[10]:


# Create an empty list
extracted_data = []


# In[11]:


# Loop through the scraped data to create a list of rows
for row in data_rows:
    columns = row.find_all()
    row_data = [column.text.strip() for column in columns]
    extracted_data.append(row_data)


# In[12]:


# Create a Pandas DataFrame by using the list of rows and a list of the column names
df = pd.DataFrame(extracted_data, columns=['id','terrestrial_date','sol','ls','month','min_temp', 'pressure'])


# In[13]:


# Confirm DataFrame was created successfully
print(df)


# ### Step 4: Prepare Data for Analysis
# 
# Examine the data types that are currently associated with each column. If necessary, cast (or convert) the data to the appropriate `datetime`, `int`, or `float` data types.
# 
#   > **Hint** You can use the Pandas `astype` and `to_datetime` methods to accomplish this task.
# 

# In[14]:


# Examine data type of each column
print(df.dtypes)


# In[15]:


df['terrestrial_date'] = pd.to_datetime(df['terrestrial_date'], errors='coerce', format='%Y-%m-%d %H:%M:%S')


# In[16]:


df['min_temp'] = pd.to_numeric(df['min_temp'], errors='coerce')


# In[17]:


df['pressure'] = pd.to_numeric(df['pressure'], errors='coerce')


# In[18]:


# Confirm type changes were successful by examining data types again
print(df.dtypes)


# ### Step 5: Analyze the Data
# 
# Analyze your dataset by using Pandas functions to answer the following questions:
# 
# 1. How many months exist on Mars?
# 2. How many Martian (and not Earth) days worth of data exist in the scraped dataset?
# 3. What are the coldest and the warmest months on Mars (at the location of Curiosity)? To answer this question:
#     * Find the average the minimum daily temperature for all of the months.
#     * Plot the results as a bar chart.
# 4. Which months have the lowest and the highest atmospheric pressure on Mars? To answer this question:
#     * Find the average the daily atmospheric pressure of all the months.
#     * Plot the results as a bar chart.
# 5. About how many terrestrial (Earth) days exist in a Martian year? To answer this question:
#     * Consider how many days elapse on Earth in the time that Mars circles the Sun once.
#     * Visually estimate the result by plotting the daily minimum temperature.
# 

# In[19]:


# 1. How many months are there on Mars?

unique_months = df['terrestrial_date'].dt.month_name().unique()
print(f"Number of months on Mars: {len(unique_months)}")


# In[20]:


# 2. How many Martian days' worth of data are there?
unique_sols = df['sol'].nunique()
print(f"Number of Martian days in the dataset: {unique_sols}")


# In[21]:


# 3. What is the average low temperature by month?
df['month'] = df['terrestrial_date'].dt.month_name()
monthly_avg_min_temp = df.groupby('month')['min_temp'].mean()


# In[22]:


# Plot the average temperature by month
monthly_avg_min_temp.plot(kind='bar', xlabel='Month', ylabel='Average Low Temperature (Celsius)', title='Average Low Temperature for Each Month')
plt.show()


# In[23]:


# Identify the coldest and hottest months in Curiosity's location


# In[24]:


# 4. Average pressure by Martian month
monthly_avg_pressure = df.groupby('month')['pressure'].mean()


# In[25]:


# Plot the average pressure by month
monthly_avg_pressure.plot(kind='bar', xlabel='Month', ylabel='Average Atmospheric Pressure', title='Average Pressure by Month')
plt.show()


# In[26]:


# 5. How many terrestrial (earth) days are there in a Martian year?
terrestrial_days_in_martian_year = df['terrestrial_date'].nunique() / df['sol'].nunique()
print(f"Average terrestrial days in a Martian year: {terrestrial_days_in_martian_year}")


# On average, the third month has the coldest minimum temperature on Mars, and the eighth month is the warmest. But it is always very cold there in human terms!
# 
# 

# Atmospheric pressure is, on average, lowest in the sixth month and highest in the ninth.

# The distance from peak to peak is roughly 1425-750, or 675 days. A year on Mars appears to be about 675 days from the plot. Internet search confirms that a Mars year is equivalent to 687 earth days.

# ### Step 6: Save the Data
# 
# Export the DataFrame to a CSV file.

# In[27]:


# Write the data to a CSV
df.to_csv('output_file.csv', index=False)


# In[28]:


browser.quit()


# In[ ]:




