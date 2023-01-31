#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install bs4


# In[2]:


import bs4
from bs4 import BeautifulSoup as bs


# In[3]:


import requests


# In[4]:


page = requests.get("https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off%27")


# In[5]:


page


# In[6]:


page.content


# In[7]:


soup = bs(page.content,'html.parser')


# In[8]:


soup


# In[9]:


print(soup.prettify())


# In[10]:


soup.findAll('a',class_='_1fQZEK')


# In[11]:


for laptop in soup.findAll('a',class_= '_1fQZEK'):
    print(laptop.find('div',attrs = {'class': "_4rR01T"}).get_text())
    


# In[12]:


for laptop in soup.findAll('a',class_= '_1fQZEK'):
    print(laptop.find('div',attrs = {'class':"_30jeq3 _1_WHN1"}).get_text())
    


# In[13]:


laptop_names = []
laptop_prices = []
laptop_ratings = []
laptop_specifcations = []
for laptop in soup.findAll('a',class_="_1fQZEK"):
    laptop_name= laptop.find('div',attrs = {'class':"_4rR01T"}).get_text()
    laptop_price = laptop.find('div',attrs = {'class':"_30jeq3 _1_WHN1"}).get_text()
    laptop_rating  = laptop.find('div',attrs = {'class':"_3LWZlK"}).get_text()
    laptop_specifcation = laptop.find('div',attrs = {'class':"fMghEO"}).get_text()
    laptop_names.append(laptop_name)
    laptop_prices.append(laptop_price)
    laptop_ratings.append(laptop_rating)
    laptop_specifcations.append(laptop_specifcation)
    


# In[14]:


laptop_prices


# In[21]:


prices = []
for price in laptop_prices:
    prices.append(int(price.replace('₹','').replace(',','')))
    
    laptop_prices = prices


# In[22]:


prices


# In[23]:


import pandas as pd
laptop_data=pd.DataFrame({'Laptop Names': laptop_names, 'Price': laptop_prices,'Ratings':laptop_ratings, 'Specifations': laptop_specifcations})


# In[24]:


laptop_data


# In[25]:


laptop_data['company_Name']=laptop_data['Laptop Names'].apply(lambda x: x.split()[0])


# In[26]:


laptop_data


# In[ ]:





# In[ ]:




