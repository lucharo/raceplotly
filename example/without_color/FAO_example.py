#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from raceplotly.plots import barplot


# In[5]:


data = pd.read_csv(
    "https://raw.githubusercontent.com/lc5415/raceplotly/main/example/dataset/FAOSTAT_data.csv"
)

my_raceplot = barplot(
    data, item_column="Item", value_column="Value", time_column="Year"
)

my_raceplot.plot(
    item_label="Top 10 crops",
    value_label="Production quantity (tonnes)",
    time_label="Year: ",  ## overwrites default `Date: `
    frame_duration=800,
)


# In[ ]:
