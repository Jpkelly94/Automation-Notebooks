# coding: utf-8

# In[1]:

#The purpose of this notebook is to automatically scrape the first table that appears in the HTML of a webpage


# In[2]:

import pandas as pd
from pandas import Series, DataFrame

# In[3]:

tables = pd.read_html("URL", header=0)


# In[3]:

tables


# In[35]:

tabes = pd.DataFrame(tables)

type(tables)


# In[36]:

output = pd.ExcelWriter('output.xlsx')

tables.to_excel(output, 'Sheet1')
output.save()



