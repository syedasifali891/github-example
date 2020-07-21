#!/usr/bin/env python
# coding: utf-8

# In[2]:


url="https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"


# In[7]:


import numpy as np


# In[60]:


import pandas as pd
import requests


# In[61]:


#Assigning
list_df=pd.read_html(url,header=0)
df=list_df[0]


# In[62]:


#Printing
df


# In[63]:


#preprocessing
df = df[(df.Borough != 'Not assigned')]

df.groupby(['Post Code','Borough'])['Neighborhood'].transform(lambda x: ', '.join(x))
df = df.drop_duplicates()
df.reset_index(drop = True, inplace=True)
df.head()


# In[64]:


df.rename(index=str, columns={"Post Code": "PostalCode", "Neighborhood":"Neighborhood"}, inplace = True)


# In[65]:


#printing final output
print(df.shape)
df.head(10)

