import pandas as pd
from raceplotly.plots import barplot

data = pd.read_csv('https://raw.githubusercontent.com/lc5415/raceplotly/main/example/FAOSTAT_data.csv')

# To add specific color to the categories, a new dictionary with rgb values for each category has to be created.
# Assigning colors to the categories.
colors = {'Sugar cane': 'rgba(0, 76, 109, 1)',
          'Potatoes': 'rgb(208, 210, 211)',
          'Wheat': 'rgb(208, 210, 211)',
          'Rice, paddy':'rgba(66, 114, 146, 1)',
          'Maize':'rgba(40, 95, 127, 1)',
          'Sugar beet':'rgb(208, 210, 211)',
          'Rice, paddy (rice milled equivalent)':'rgb(208, 210, 211)',
          'Sweet potatoes':'rgb(208, 210, 211)'}
# Default color for category will be assigned randomly if not specified explicitly

my_raceplot = barplot(data,  item_column='Item', value_column='Value', time_column='Year', item_color=colors)

# In this case color for 'Rice, paddy (rice milled equivalent)', 'Sugar beet' and 'Sweet potatoes' will be randomly assingned
# Default color for cateogry is black when color is not specifed explicitly

# Mapping the items with the color for the whole dataset.
data['color'] = data['Item'].map(colors)

my_raceplot = barplot(data,  item_column='Item', value_column='Value', time_column='Year', item_color='color')

my_raceplot.plot(item_label = 'Top 10 crops',
                 value_label = 'Production quantity (tonnes)',
                 time_label = 'Year: ', ## overwrites default `Date: `
                 frame_duration = 800)
