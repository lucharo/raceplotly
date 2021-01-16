import plotly.graph_objects as go
import pandas as pd
from random import sample
import numpy as np
import datetime

class barplot(object):
    '''
    Class to make bar chart 'race' plots using plotly.

    Arguments:
    * item_column: usually a string denoting the column that you wish to rank (e.g. countries, food, people...)
    * value_column: numerical value

    '''
    
    def __init__(self, df: pd.DataFrame = None, item_column: str = None, value_column: str = None , time_column: str = None , item_color: str = None , top_entries: int = 10):
        self.df = df
        self.item_column = item_column
        self.value_column = value_column
        self.time_column = time_column
        self.item_color = item_color
        self.top_entries = top_entries
        self.title = ''
        self.fig = None
        self.orientation = None
        self.date_format = None

    def plot(self, title: str = None, orientation: str = 'horizontal', initial_frame = 'min', value_label: str = None, item_label: str = None, time_label: str = 'Date: ', frame_duration: int = 500, date_format: str = None):
        '''
        By default the time variable is appended to the title string

        * self.orientation: if this is horizontal the value_column is the x-axis, if this is set to
        vertical the value_column is the y_axis
        '''

        self.orientation = orientation # record last self.orientation used 
        self.date_format = date_format # record last date_format
        self.title = title

        #get colors
        self.__get_colors()
        
        # make frame1, the one that appears before the animation playy
        self.__make_frame1(initial_frame)

        # define ui: adds Play,Pause buttons and defines empty slider
        self.__define_ui(time_label)

        # make frames, also updates sliders at each frame
        self.fig['frames'] = self.__make_frames(title, frame_duration)

        # update sliders in layout to sliders_dict with all the steps defined
        self.fig["layout"]["sliders"] = [self.sliders_dict]
        
        if (item_label is not None) or (value_label is not None):
            if orientation == 'horizontal':
                self.fig.update_xaxes(title_text= value_label,
                        visible = True, showticklabels= True)
                self.fig.update_yaxes(title_text= item_label, 
                        visible = True, showticklabels= False)
            else: 
                self.fig.update_xaxes(title_text= item_label,
                        visible = True, showticklabels= False)
                self.fig.update_yaxes(title_text= value_label, 
                        visible = True, showticklabels= True)
                
        self.fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = frame_duration
        self.fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = frame_duration

        return self.fig

    def __make_frames(self, title: str, frame_duration: int):
        '''
        bar_race.make_frames automatically makes frame fromt the earliest to the latest available time stamp
        '''

        x, y = self.__check_orientation()
        frames = []
        ## sorted date to iterate through them
        dates = np.sort(self.df[self.time_column].unique())
        for date in dates:
            
            # specified date string for plotly frame id and for printing in plot
            if isinstance(date, np.datetime64):
                date = pd.to_datetime(str(date)) 
                try:
                    date_str = date.strftime(format = self.date_format) if self.date_format is not None else str(date)
                except:
                    raise Exception("Something was wrong setting the date_format, please check the strftime (https://strftime.org/) documentation for date formatting and try again")
            else: 
                date_str = str(date)
                    
            # filter out by year
            snap_data = self.df[self.df[self.time_column] == date]

            # get_top 10
            snap_data = snap_data.sort_values(self.value_column, ascending=False).iloc[:self.top_entries,:]

            # get top enttry at top of chart
            snap_data = snap_data.sort_values(self.value_column, ascending=True)

            # make frame
            frames.append(
                go.Frame(
                    data=[
                        go.Bar(
                            x=snap_data[x],
                            y=snap_data[y],
                            marker_color=snap_data['color'],
                            cliponaxis=False,
                            hoverinfo='all',
                            hovertemplate = '<extra></extra>', #annoying and obscure, see docs 
                            ## (https://community.plotly.com/t/remove-trace-0-next-to-hover/33731)
                            textposition='outside',
                            texttemplate='%{x}<br>%{y:.4s}' if self.orientation == 'vertical' else '%{y}<br>%{x:.4s}',
                            textangle = 0,
                            orientation = 'h' if self.orientation == 'horizontal' else 'v'
                        )
                    ],
                    layout=go.Layout(
                        font={'size': 14},
                        plot_bgcolor = '#FFFFFF',
                        xaxis={
                            'showline': False,
                            'visible': True
                        } if self.orientation == 'vertical' else 
                        {
                            'showline': True,
                            'visible': True,
                            'range': (0, self.df[self.value_column].max())
                        },
                        yaxis={
                            'showline': True,
                            'visible': True,
                            'range': (0, self.df[self.value_column].max())
                        } if self.orientation == 'vertical' else
                        {
                            'showline': False,
                            'visible': True
                        },
                        bargap=0.15,
                        title= title
                    ),
                    name = date_str
                )
            )

            slider_step = {"args": [
                [date_str],
                {"frame": {"duration": frame_duration, "redraw": False},
                 "mode": "immediate",
                 "transition": {"duration": frame_duration}}
            ],
                           "label": date_str,
                           "method": "animate"}
            self.sliders_dict["steps"].append(slider_step)


        return frames

    def __make_frame1(self, time_frame1 = 'min'):
        """
        Internal use

        time_frame1 can be a number that equals one of the entries in the time column 
        or key values such as 'min' or 'max'
        """

        if time_frame1 == 'min':
            time_frame1 = self.df[self.time_column].min()
        elif time_frame1 == 'max':
            time_frame1 = self.df[self.time_column].max()

        # filter by year
        frame1 = self.df[self.df[self.time_column] == time_frame1]

        # get top entries
        frame1  = frame1.sort_values(self.value_column, ascending=False).iloc[:self.top_entries,:]

        # return in ascending order so that top bar corresponds to largest value  
        frame1 = frame1.sort_values(self.value_column, ascending=True) 
        
        x, y = self.__check_orientation()

        # Create figure
        self.fig = go.Figure(
            data=[
                go.Bar(
                    x=frame1[x],
                    y=frame1[y],
                    marker_color=frame1['color'],
                    hoverinfo='all',
                    textposition='outside',
                    texttemplate='%{x}<br>%{y:.4s}' if self.orientation == 'vertical' else '%{y}<br>%{x:.4s}',
                    textangle= 0,
                    cliponaxis=False,
                    orientation = 'h' if self.orientation == 'horizontal' else 'v'
                )
            ],
            layout=go.Layout(
                font={'size': 14},
                plot_bgcolor = '#FFFFFF',
                xaxis={
                    'showline': False,
                    'visible': False
                } if self.orientation == 'vertical' else 
                {
                    'showline': True,
                    'visible': True,
                    'range': (0, self.df[self.value_column].max())
                },
                yaxis={
                    'showline': True,
                    'visible': True,
                    'range': (0, self.df[self.value_column].max())
                } if self.orientation == 'vertical' else
                {
                    'showline': False,
                    'visible': False
                },
                bargap=0.15,
                title= self.title
            ),
            frames = []
        )


    def __check_orientation(self):

        if self.orientation == 'horizontal':
            x = self.value_column
            y = self.item_column
        elif self.orientation == 'vertical':
            y = self.value_column
            x = self.item_column
        else:
            raise Exception('Please provide a valid value for orientation: horizontal or vertical')

        return x, y

    def __define_ui(self, time_label: str = None):
        
        self.fig["layout"]["updatemenus"] = [
            {
                "buttons": [
                    {
                        "args": [None, {"frame": {"duration": 500, "redraw": False},
                                        "fromcurrent": True, "transition": {"duration": 300,
                                                                            "easing": "quadratic-in-out"}}],
                        "label": "Play",
                        "method": "animate"
                    },
                    {
                        "args": [[None], {"frame": {"duration": 0, "redraw": False},
                                          "mode": "immediate",
                                          "transition": {"duration": 0}}],
                        "label": "Pause",
                        "method": "animate"
                    }
                ],
                "direction": "left",
                "pad": {"r": 10, "t": 87},
                "showactive": True,
                "type": "buttons",
                "x": 0.1,
                "xanchor": "right",
                "y": 0,
                "yanchor": "top"
            }
        ]

        self.sliders_dict = {
            "active": 0,
            "yanchor": "top",
            "xanchor": "left",
            "currentvalue": {
                "font": {"size": 20},
                "prefix": time_label,
                "visible": True,
                "xanchor": "right"
            },
            "transition": {"duration": 300, "easing": "cubic-in-out"},
            "pad": {"b": 10, "t": 50},
            "len": 0.9,
            "x": 0.1,
            "y": 0,
            "steps": [] # empty, gets filled when frames are made
        }
        

    def __get_colors(self):
        if (self.item_color == None):
            colors = {item: 'rgb({}, {}, {})'.format(*sample(range(256), 3)) for item in self.df[self.item_column].unique()}
            self.df['color'] = self.df[self.item_column].map(colors)
        else:
            self.df=self.df.rename(columns={self.item_color: "color"})
