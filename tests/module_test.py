#!/usr/bin/env python

import pandas as pd
from raceplotly.plots import barplot

# load data
data = pd.read_csv('https://github.com/lc5415/raceplotly/blob/main/example/FAOSTAT_data.csv')

# instantiate barplot
bar_race = barplot(data, item_column='Item', value_column='Value', time_column='Year')

# plot horizontal version
bar_race.plot(title = 'Top 10 Crops from 1961 to 2018',
              item_label = 'Top 10 crops',
              value_label = 'Production quantity (tonnes)', frame_duration = 800)

# plot vertically
bar_race.plot(title = 'Top 10 Crops from 1961 to 2018',
              orientation='vertical',
              item_label='Crops')

