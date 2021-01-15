![Test Python package](https://github.com/lc5415/raceplotly/workflows/Test%20Python%20package/badge.svg)
[![PyPI version](https://badge.fury.io/py/raceplotly.svg)](https://badge.fury.io/py/raceplotly)
# Making race plots with Plotly!

## Motivation 

Bar race plots, barchart race plots or simply race plots are very common when evaluating rankings over time. Python plotting is not the most user friendly and whenever I've wanted to make race plots I have ended up with tonnes of code for what is a simple plot in the end. I wish to remove that headache for many users that simply want to make quick plot and then move on.

## Usage

### Installation

`raceplotly` can be installed from pip.The only dependencies are `pandas` and `plotly`.
```sh
pip install raceplotly
```

### Basic documentation

The package only contains one module called `barplot`. This module takes the following arguments at initialisation:

* `df`: (type: pandas.DataFrame) dataframe from which to query data
* `item_column`: (type: string) Name of column describing the items to be ranked (e.g. countries, corporations, names of people...)
* `value_column`: (type: string) Name of column describing the value to be used for ranking (e.g. GDP, population, volume of sales...)
* `time_column`: (type: string) Name of column describing the time variable. This must be a sequence (e.g. years, days). Support of Date format has not been tested yet.
* `item_color`: (type: string) [OPTIONAL ATTRIBUTE] Name of column describing the color for different categories (e.g. colors = {'Category 1': 'rgba(0, 76, 109, 1)', 'Category 2': 'rgb(208, 210, 211)'}...) [DEFAULT = Random Color]
* `top_entries`: (type: numeric) [OPTIONAL ATTRIBUTE] Number of top entries to display (e.g. 5 for top 5 for any given time period...) [DEFAULT = 10]

The `barplot` object contains one main method:
* `plot(title, orientation, item_label, value_label, time_label, frame_duration, date_format)`: 
	* `title`: (type: string) Main title of the plot (static by default)
	* `orientation`: (type: string -> 'horizontal' or 'vertical') whether bars grow upwards ('vertical') or rightwards ('horizontal')
	* `initial_frame`: (type: numeric or string) Should either match one of the values from the `time_column` or be provided as `min` or `max`, in which case the initial frame would correspond to the minimum or maximum value of the `time_column`.
	* `item_label`: (type: string) Title of the axis corresponding to the item values
	* `value_label`: (type: string) Title of the axis corresponding to the value
	* `time_label`: (type: string) Title for the time axis which appears in each frame next to the formmated date/time variable
	* `frame_duration`: (type: int -> default 500) Frame and transition duration time in milliseconds
	* `date_format`: (type: str) Format for the displayed date/time, should be compatible with strftime format, [see strftime reference](https://strftime.org/).

### Example plot: Top 10 crops from 1961 to 2018

See example notebooks under `example/`.

```python
import pandas as pd
from raceplotly.plots import barplot

data = pd.read_csv('https://raw.githubusercontent.com/lc5415/raceplotly/main/example/FAOSTAT_data.csv')

my_raceplot = barplot(data,  item_column='Item', value_column='Value', time_column='Year')

my_raceplot.plot(item_label = 'Top 10 crops', value_label = 'Production quantity (tonnes)', frame_duration = 800)

```

![](https://github.com/lc5415/raceplotly/blob/main/example/race_example.gif)

### Example with specified colors for different category.

See example notebooks under `example/color`.

```python
import pandas as pd
from raceplotly.plots import barplot

data = pd.read_csv('https://raw.githubusercontent.com/lc5415/raceplotly/main/example/FAOSTAT_data.csv')

# To add specific color to the categories, a new coloumn with rgb values for each category has to be created.
# Assigning colors to the categories.
colors = {'Sugar cane': 'rgba(0, 76, 109, 1)',
          'Potatoes': 'rgb(208, 210, 211)',
          'Wheat': 'rgb(208, 210, 211)',
          'Rice, paddy':'rgba(66, 114, 146, 1)',
          'Maize':'rgba(40, 95, 127, 1)',
          'Sugar beet':'rgb(208, 210, 211)',
          'Rice, paddy (rice milled equivalent)':'rgb(208, 210, 211)',
          'Sweet potatoes':'rgb(208, 210, 211)',
          'Barley':'rgb(208, 210, 211)',
          'Cassava':'rgb(208, 210, 211)',
          'Soybeans':'rgb(208, 210, 211)',
          'Oil palm fruit':'rgb(208, 210, 211)',
          'Vegetables, fresh nes':'rgb(208, 210, 211)'}

# Default color for cateogry is black when color is not specifed explicitly

# Mapping the items with the color for the whole dataset.
data['color'] = data['Item'].map(colors)

my_raceplot = barplot(data,  item_column='Item', value_column='Value', time_column='Year', item_color='color')

my_raceplot.plot(item_label = 'Top 10 crops', value_label = 'Production quantity (tonnes)', time_label = 'Year: ', ## overwrites default `Date: `
                 frame_duration = 800)

```

![](https://github.com/lc5415/raceplotly/blob/main/example/color/race_with_color_example.gif)
