import pandas as pd
from raceplotly.plots import barplot


data = pd.read_csv('https://raw.githubusercontent.com/lc5415/raceplotly/main/example/FAOSTAT_data.csv')

# To add specific color to the categories, a new coloumn with rgb values for each category has to be created.
# Assigning colors to the categories.
colors = {'Sugar cane': 'rgba(0, 76, 109, 1)',
          'Potatoes': 'rgba(40, 95, 127, 1)',
          'Wheat': 'rgba(66, 114, 146, 1)',
          'Rice, paddy':'rgb(208, 210, 211)',
          'Maize':'rgb(208, 210, 211)',
          'Sugar beet':'rgb(208, 210, 211)',
          'Rice, paddy (rice milled equivalent)':'rgb(208, 210, 211)',
          'Sweet potatoes':'rgb(208, 210, 211)',
          'Barley':'rgb(208, 210, 211)',
          'Cassava':'rgb(208, 210, 211)'}

# Mapping the items with the color for the whole dataset.
data['color'] = data['Item'].map(colors)

my_raceplot = barplot(data,  item_column='Item', value_column='Value', time_column='Year', item_color='color')

my_raceplot.plot(item_label = 'Top 10 crops',
                 value_label = 'Production quantity (tonnes)',
                 time_label = 'Year: ', ## overwrites default `Date: `
                 frame_duration = 800)