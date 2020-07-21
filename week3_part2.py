#!/usr/bin/env python
# coding: utf-8

# In[38]:


url="https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"


# In[39]:


import numpy as np
import pandas as pd
import requests


# In[40]:


list_df=pd.read_html(url,header=0)
df=list_df[0]


# In[41]:


df.head()


# In[42]:


df=df[(df.Borough != 'Not assigned')]
df.head()


# In[44]:


df.groupby(['Postal Code','Borough'])['Neighborhood'].transform(lambda x: ', '.join(x))
df = df.drop_duplicates()
df.reset_index(drop = True, inplace=True)
df.head()


# In[50]:


df.rename(index=str,columns={'Postal Code':'PostalCode'},inplace=True)


# In[51]:


print(df.shape)
df.head(10)


# # part2

# In[48]:


df2=pd.read_csv("https://cocl.us/Geospatial_data")
df2.head()


# In[49]:


df2.rename(index=str, columns={"Postal Code": "PostalCode"}, inplace = True)
df2.head()


# In[53]:


toronto_df=df.join(df2.set_index('PostalCode'),on='PostalCode')
toronto_df.head(10)


# In[ ]:




