#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pytrends')


# In[2]:


import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends=TrendReq()


# In[10]:


trends.build_payload(kw_list=['Data Science'])
data=trends.interest_by_region()
data=data.sort_values(by='Data Science',ascending=False)
data=data.head(15)
print(data)


# In[11]:


data.reset_index().plot(x='geoName',y='Data Science',figsize=(10,6),kind='bar')
plt.style.use('fivethirtyeight')
plt.show()


# In[14]:


data=TrendReq(hl='en-US',tz=360)
data.build_payload(kw_list=['Data Science'])
data =data.interest_over_time()
fig,ax=plt.subplots(figsize=(10,6))
data['Data Science'].plot()
plt.style.use('fivethirtyeight')
plt.title('total google search for data science')
plt.xlabel('year')
plt.ylabel('total count')
plt.show()


# In[ ]:




