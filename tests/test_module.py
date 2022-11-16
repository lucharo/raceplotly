import pandas as pd
from raceplotly.plots import barplot

# load data
data = pd.read_csv(
    "https://raw.githubusercontent.com/lucharo/raceplotly/main/example/dataset/FAOSTAT_data.csv"
)


def test_plot_horizontal():
    # instantiate barplot
    my_raceplot = barplot(
        data, item_column="Item", value_column="Value", time_column="Year"
    )

    # plot horizontal version
    my_raceplot.plot(
        title="Top 10 Crops from 1961 to 2018",
        item_label="Top 10 crops",
        value_label="Production quantity (tonnes)",
        frame_duration=800,
    )
    assert True


def test_plot_vertical():
    # instantiate barplot
    my_raceplot = barplot(
        data, item_column="Item", value_column="Value", time_column="Year"
    )

    # plot vertically
    my_raceplot.plot(
        title="Top 10 Crops from 1961 to 2018",
        orientation="vertical",
        item_label="Crops",
    )
    assert True


def test_specific_color_input():
    # To add specific color to the categories, a new dictionary with rgb values for each category has to be created.

    # Assigning colors to the categories.
    # Top 3 categories have been assigned with different shades of blue and the rest are all grey
    colors = {
        "Sugar cane": "rgba(0, 76, 109, 1)",
        "Potatoes": "rgb(208, 210, 211)",
        "Wheat": "rgb(208, 210, 211)",
        "Rice, paddy": "rgba(66, 114, 146, 1)",
        "Maize": "rgba(40, 95, 127, 1)",
        "Sugar beet": "rgb(208, 210, 211)",
        "Rice, paddy (rice milled equivalent)": "rgb(208, 210, 211)",
        "Sweet potatoes": "rgb(208, 210, 211)",
        "Soybeans": "rgb(208, 210, 211)",
        "Vegetables, fresh nes": "rgb(208, 210, 211)",
        "Cassava": "rgb(208, 210, 211)",
        "Oil palm fruit": "rgb(208, 210, 211)",
        "Barley": "rgb(208, 210, 211)",
    }

    # Mapping the items with the color for the whole dataset.
    data["color"] = data["Item"].map(colors)

    # Default color for category will be assigned randomly if not specified explicitly
    my_raceplot = barplot(
        data,
        item_column="Item",
        value_column="Value",
        time_column="Year",
        item_color=colors,
    )

    # In this case color for 'Rice, paddy (rice milled equivalent)', 'Sugar beet' and 'Sweet potatoes' will be randomly assingned
    my_raceplot.plot(
        item_label="Top 10 crops",
        value_label="Production quantity (tonnes)",
        time_label="Year: ",
        frame_duration=800,
    )

    assert True


def test_mixed_color_input():
    # To add specific color to the categories, a new dictionary with rgb values for each category has to be created.
    # Assigning colors to few the categories and leaving the rest to be assigned randomly
    colors = {
        "Sugar cane": "rgba(0, 76, 109, 1)",
        "Wheat": "rgb(208, 210, 211)",
        "Maize": "rgba(40, 95, 127, 1)",
        "Rice, paddy (rice milled equivalent)": "rgb(208, 210, 211)",
        "Soybeans": "rgb(208, 210, 211)",
        "Vegetables, fresh nes": "rgb(208, 210, 211)",
        "Cassava": "rgb(208, 210, 211)",
        "Oil palm fruit": "rgb(208, 210, 211)",
        "Barley": "rgb(208, 210, 211)",
    }

    # Mapping the items with the color for the whole dataset.
    data["color"] = data["Item"].map(colors)

    # Default color for category will be assigned randomly if not specified explicitly
    my_raceplot = barplot(
        data,
        item_column="Item",
        value_column="Value",
        time_column="Year",
        item_color=colors,
    )

    # In this case color for 'Rice, paddy (rice milled equivalent)', 'Sugar beet' and 'Sweet potatoes' will be randomly assingned
    my_raceplot.plot(
        item_label="Top 10 crops",
        value_label="Production quantity (tonnes)",
        time_label="Year: ",
        frame_duration=800,
    )

    assert True
