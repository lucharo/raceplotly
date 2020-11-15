#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bar_chart_race as bcr
import pandas as pd
from raceplotly.plots import barplot


# ## Original data

# In[2]:


data = bcr.load_dataset('covid19_tutorial')
data


# ## Tidy data (one row, one entry)

# In[3]:


data.reset_index(inplace=True)
data = pd.melt(data, id_vars = 'date', var_name = 'Country', value_name = 'COVID cases')
data


# In[4]:


## date format
print(data['date'])


# In[5]:


my_raceplot = barplot(data,  item_column='Country', value_column='COVID cases', time_column='date')
my_raceplot.plot(item_label = 'Country',
                 value_label = 'COVID cases',
                 frame_duration = 800,
                 date_format = '%Y-%m-%d')


# In[ ]:




