import os
import numpy as np

import dash
import dash_daq as daq
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_core_components as dcc

from dash_daq import DarkThemeProvider

app = dash.Dash()

app.scripts.config.serve_locally = True
app.config['suppress_callback_exceptions'] = True

server = app.server

root_layout = html.Div([
    dcc.Interval(id="upon-load", interval=1000, n_intervals=0),
    dcc.Location(id='url', refresh=False),

    html.Div([
            daq.ToggleSwitch(
                id='toggleTheme',
                label=['Light Theme', 'Dark Theme'],
                style={'float': 'right'},
            ),
    ]),

    html.Div(id='page-content'),
])


light_layout = html.Div([
    dcc.Interval(id="stream", interval=1000, n_intervals=0),
    html.Div([
        html.H2("Accelerometer Control Panel",
                style={'color': '#1d1d1d',
                       'margin-left': '2%',
                       'display': 'inline-block',
                       'text-align': 'center'}),
        html.Img(src="https://s3-us-west-1.amazonaws.com/plotly-tutorials/" \
                     "excel/dash-daq/dash-daq-logo-by-plotly-stripe.png",
                 style={'position': 'relative',
                        'float': 'right',
                        'right': '10px',
                        'height': '75px'})
    ], className='banner', style={
        'height': '75px',
        'margin': '0px -10px 10px',
        'background-color': '#EBF0F8',
        }),
    html.Div([
        html.H3("Phidget Info", className="six columns"),
    ], className='row Title'),
    html.Div([
        html.Div([
            html.Div("Attached:", className="two columns"),
            html.Div("1041 - PhidgetSpatial 0/0/3 Basic", id="device-attached",
                     className="four columns"),
            daq.ToggleSwitch(
                id='connection',
                label=['Disconnected', 'Connected'],
                value=True,
                className="five columns",
                size=15,
            ),
            daq.Indicator(
                id="connection-est",
                value=True,
                className="one columns",
                style={'margin': '6px'}
            )
        ], className="row attachment"),
        html.Hr(style={'marginBottom': '0', 'marginTop': '0'}),
        html.Div([
            html.Div("Version:", className="two columns"),
            html.Div("203", id="device-version", className="four columns"),
            html.Div("Serial Number:", className="two columns"),
            html.Div("478682", id="device-serial")
        ], className="row version-serial"),
        html.Div([
            html.Div("Channel: ", className="two columns"),
            html.Div("0", id="device-channel", className="four columns"),
        ], className="row channel")
    ]),

    html.Div([
        html.Div([
            html.Div([
                html.H3("Settings")
            ], className='Title'),
            html.Div([
                html.Div(id="channel-name"),
                html.Div([
                    html.Div([
                        "Change Interval"
                    ], className="three columns", style={'marginTop': '10px'}),
                    html.Div([
                        daq.Slider(
                            id="slider1",
                            value=0,
                            min=1,
                            max=16,
                            step=0.01,
                            marks={i: str(i) for i in range(1, 17)},
                            disabled="True",
                            className="eleven columns")
                    ], className="seven columns", style={'marginTop': '15px'}),
                    html.Div([
                        daq.LEDDisplay(
                            id="display",
                            value=0.00,
                            size=10,
                            style={'textAlign': 'center'})
                    ], className="two columns", style={'marginTop': '6px'})
                ], className="row stuff", style={'margin': '5px 0'}),
                html.Div([
                    html.Div([
                        "Data Interval"
                    ], className="three columns", style={'marginTop': '10px'}),
                    html.Div([
                        daq.Slider(
                            id="slider2",
                            value=1000,
                            min=1,
                            max=1000,
                            step=None,
                            marks={0: "0", 500: "500", 1000: "1000"},
                            className="eleven columns",
                            disabled=True),
                    ], className="seven columns", style={'marginTop': '15px'}),
                    html.Div([
                        daq.LEDDisplay(
                            id="display2",
                            value=1000,
                            size=10,
                            style={'textAlign': 'center', 'marginTop': '5px'},)
                    ], className="two columns",)
                ], className="row stuff"),
            ]),
        ], className="six columns"),

        html.Div([
            html.Div([
                html.H3("G-Force")
            ], className='Title'),
            html.Div([
                html.Div([
                    html.Div(
                        "X-axis:",
                        style={'textAlign': 'right'},
                        className="three columns"),
                    html.Div(
                        id="x-value",
                        className="one columns",
                        style={'marginRight': '10px'}),
                    html.Div(
                        "g",
                        className="one columns")
                ], className="row"),
                html.Div([
                    html.Div(
                        "Y-axis:",
                        style={'textAlign': 'right'},
                        className="three columns"),
                    html.Div(
                        id="y-value",
                        className="one columns",
                        style={'marginRight': '10px'}),
                    html.Div(
                        "g",
                        className="one columns")
                ], className="row"),
                html.Div([
                    html.Div(
                        "Z-axis:",
                        style={'textAlign': 'right'},
                        className="three columns"),
                    html.Div(
                        id="z-value",
                        className="one columns",
                        style={'marginRight': '10px'}),
                    html.Div(
                        "g",
                        className="one columns")
                ], className="row"),
                html.Div([
                    html.Div(
                        "TIme Stamp:",
                        style={'textAlign': 'right'},
                        className="three columns"),
                    html.Div(
                        id="time-stamp",
                        className="one columns",
                        style={'marginRight': '10px'}),
                    html.Div(
                        "s",
                        className="one columns")
                ], className="row"),
            ]),
        ], className="six columns"),
    ], className="row info"),

    html.Div([
        html.H3("Data")
    ], className='Title'),
    html.Div([
        html.Div([
            html.Div([
                daq.Gauge(
                    id="x-gauge",
                    label="X-axis",
                    labelPosition="bottom",
                    units="g",
                    value=0,
                    min=-8,
                    max=8,
                    showCurrentValue=True
                )
            ], className='six columns', style={'margin-bottom': '15px'}),

            html.Div([
                daq.Gauge(
                    id="y-gauge",
                    label="Y-axis",
                    labelPosition="bottom",
                    units="g",
                    value=0,
                    min=-8,
                    max=8,
                    showCurrentValue=True,
                )
            ], className='six columns'),
        ], style={'margin': '15px 0'})
    ], className='row x-y'),
    html.Div([
        html.Div([
            html.Div([
                daq.Gauge(
                    id="z-gauge",
                    label="Z-axis",
                    labelPosition="bottom",
                    units="g",
                    value=0,
                    min=-8,
                    max=8,
                    showCurrentValue=True,
                )
            ], className='six columns'),
        ])
    ], className='row z'),
], style={'padding': '0px 10px 15px 10px',
          'marginLeft': 'auto', 'marginRight': 'auto', "width": "900px",
          'boxShadow': '0px 0px 5px 5px rgba(204,204,204,0.4)'})


dark_layout = DarkThemeProvider([
    dcc.Interval(id="stream", interval=1000, n_intervals=0),
    html.Div(id="inner", children=[
        html.Div([
            html.H2("Accelerometer Control Panel",
                    style={'color': '#EBF0F8',
                           'margin-left': '2%',
                           'display': 'inline-block',
                           'text-align': 'center'}),
            html.Img(src="https://s3-us-west-1.amazonaws.com/plotly-" +
                         "tutorials/excel/dash-daq/dash-daq-logo-by-" +
                         "plotly-stripe+copy.png",
                     style={'position': 'relative',
                            'float': 'right',
                            'right': '10px',
                            'height': '75px'})
        ], className='banner', style={
            'height': '75px',
            'margin': '0px -10px 10px',
            'background-color': '#1d1d1d',
            }),
        html.Div([
            html.H3("Phidget Info", className="six columns"),
        ], className='row Title'),
        html.Div([
            html.Div([
                html.Div("Attached:", className="two columns"),
                html.Div("1041 - PhidgetSpatial 0/0/3 Basic",
                         id="device-attached",
                         className="four columns"),
                daq.ToggleSwitch(
                    id='connection',
                    label=['Disconnected', 'Connected'],
                    value=True,
                    className="five columns",
                    size=15,
                ),
                daq.Indicator(
                    id="connection-est",
                    value=True,
                    className="one columns",
                    style={'margin': '6px'}
                )
            ], className="row attachment"),
            html.Hr(style={'marginBottom': '0', 'marginTop': '0'}),
            html.Div([
                html.Div("Version:", className="two columns"),
                html.Div("203", id="device-version", className="four columns"),
                html.Div("Serial Number:", className="two columns"),
                html.Div("478682", id="device-serial")
            ], className="row version-serial"),
            html.Div([
                html.Div("Channel: ", className="two columns"),
                html.Div("0", id="device-channel", className="four columns"),
            ], className="row channel")
        ]),

        html.Div([
            html.Div([
                html.Div([
                    html.H3("Settings")
                ], className='Title'),
                html.Div([
                    html.Div(id="channel-name"),
                    html.Div([
                        html.Div([
                            "Change Interval"
                        ], className="three columns",
                           style={'marginTop': '10px'}),
                        html.Div([
                            daq.Slider(
                                id="slider1",
                                value=0,
                                min=0,
                                max=16,
                                step=0.01,
                                marks={i: str(i) for i in range(0, 17)},
                                disabled="True",
                                className="eleven columns")
                        ], className="seven columns",
                                 style={'marginTop': '15px'}),
                        html.Div([
                            daq.LEDDisplay(
                                id="display",
                                value=1.00,
                                size=10,
                                style={'textAlign': 'center'})
                        ], className="two columns",
                                 style={'marginTop': '6px'})
                    ], className="row stuff", style={'margin': '5px 0'}),
                    html.Div([
                        html.Div([
                            "Data Interval"
                        ], className="three columns",
                           style={'marginTop': '10px'}),
                        html.Div([
                            daq.Slider(
                                id="slider2",
                                value=1000,
                                min=1,
                                max=1000,
                                step=None,
                                marks={0: "0", 500: "500", 1000: "1000"},
                                className="eleven columns",
                                disabled=True),
                        ], className="seven columns",
                                 style={'marginTop': '15px'},),
                        html.Div([
                            daq.LEDDisplay(
                                id="display2",
                                value=1000,
                                size=10,
                                style={'textAlign': 'center',
                                       'marginTop': '5px'},)
                        ], className="two columns",)
                    ], className="row stuff"),
                ]),
            ], className="six columns"),

            html.Div([
                html.Div([
                    html.H3("G-Force")
                ], className='Title'),
                html.Div([
                    html.Div([
                        html.Div(
                            "X-axis:",
                            style={'textAlign': 'right'},
                            className="three columns"),
                        html.Div(
                            id="x-value",
                            className="one columns",
                            style={'marginRight': '10px'}),
                        html.Div(
                            "g",
                            className="one columns")
                    ], className="row"),
                    html.Div([
                        html.Div(
                            "Y-axis:",
                            style={'textAlign': 'right'},
                            className="three columns"),
                        html.Div(
                            id="y-value",
                            className="one columns",
                            style={'marginRight': '10px'}),
                        html.Div(
                            "g",
                            className="one columns")
                    ], className="row"),
                    html.Div([
                        html.Div(
                            "Z-axis:",
                            style={'textAlign': 'right'},
                            className="three columns"),
                        html.Div(
                            id="z-value",
                            className="one columns",
                            style={'marginRight': '10px'}),
                        html.Div(
                            "g",
                            className="one columns")
                    ], className="row"),
                    html.Div([
                        html.Div(
                            "TIme Stamp:",
                            style={'textAlign': 'right'},
                            className="three columns"),
                        html.Div(
                            id="time-stamp",
                            className="one columns",
                            style={'marginRight': '10px'}),
                        html.Div(
                            "s",
                            className="one columns")
                    ], className="row"),
                ]),
            ], className="six columns"),
        ], className="row info"),

        html.Div([
            html.H3("Data")
        ], className='Title'),
        html.Div([
            html.Div([
                html.Div([daq.Gauge(
                    id="x-gauge",
                    label="X-axis",
                    labelPosition="bottom",
                    units="g",
                    value=0,
                    min=-8,
                    max=8,
                    theme={'dark': True},
                    showCurrentValue=True,
                )], className='six columns', style={'margin-bottom': '15px'}),

                html.Div([daq.Gauge(
                    id="y-gauge",
                    label="Y-axis",
                    labelPosition="bottom",
                    units="g",
                    value=0,
                    min=-8,
                    max=8,
                    showCurrentValue=True,
                )], className='six columns'),
            ], style={'margin': '15px 0'})
        ], className='row x-y'),
        html.Div([
            html.Div([
                html.Div([daq.Gauge(
                    id="z-gauge",
                    label="Z-axis",
                    labelPosition="bottom",
                    units="g",
                    value=0,
                    min=-8,
                    max=8,
                    showCurrentValue=True,
                    theme={'dark': True}
                )], className='six columns'),
            ])
        ], className='row z'),
    ], style={'padding': '0px 10px 15px 10px',
              'marginLeft': 'auto', 'marginRight': 'auto', "width": "900px",
              'boxShadow': '0px 0px 5px 5px rgba(204,204,204,0.4)',
              'backgroundColor': '#2a3f5f', 'color': 'white'})
])

app.layout = root_layout


@app.callback(Output('toggleTheme', 'value'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/dark':
        return True
    else:
        return False


@app.callback(Output('page-content', 'children'),
              [Input('toggleTheme', 'value')])
def page_layout(value):
    if value:
        return dark_layout
    else:
        return light_layout


@app.callback(Output("stream", "interval"),
              [Input("connection", "value")])
def update_interval(value):
    if not value:
        return 3.6E6
    return 1000


@app.callback(Output("connection-est", "value"),
              [Input("connection", "value")])
def update_connection_indicator(value):
    return value


@app.callback(Output("display", "value"),
              [Input("slider1", "value")])
def update_change_display(value):
    return value


@app.callback(Output("display2", "value"),
              [Input("slider2", "value")])
def update_data_display(value):
    return value


@app.callback(Output("x-value", "children"),
              [Input("stream", "n_intervals")])
def stream_x(value):
    return str("{0:.3f}".format(round(np.random.normal(0, 0.5), 3)))


@app.callback(Output("y-value", "children"),
              [Input("stream", "n_intervals")])
def stream_x_text(value):
    return str("{0:.3f}".format(round(np.random.normal(0, 0.5), 3)))


@app.callback(Output("z-value", "children"),
              [Input("stream", "n_intervals")])
def stream_y_text(value):
    return str("{0:.3f}".format(round(np.random.normal(0, 0.5), 3)))


@app.callback(Output("time-stamp", "children"),
              [Input("stream", "n_intervals")])
def time_stamp_text(value):
    return str(value)


@app.callback(Output("x-gauge", "value"),
              [Input("x-value", "children")])
def stream_x_gauge(value):
    return float(value)


@app.callback(Output("y-gauge", "value"),
              [Input("y-value", "children")])
def stream_y_gauge(value):
    return float(value)


@app.callback(Output("z-gauge", "value"),
              [Input("z-value", "children")])
def stream_z_gauge(value):
    return float(value)


external_css = ["https://codepen.io/chriddyp/pen/bWLwgP.css",
                "https://cdn.rawgit.com/samisahn/dash-app-stylesheets/" +
                "0925c314/dash-accelerometer.css",
                "https://fonts.googleapis.com/css?family=Dosis"]


for css in external_css:
    app.css.append_css({"external_url": css})

if 'DYNO' in os.environ:
    app.scripts.append_script({
        'external_url': 'https://cdn.rawgit.com/chriddyp/' +
                        'ca0d8f02a1659981a0ea7f013a378bbd/raw/' +
                        'e79f3f789517deec58f41251f7dbb6bee72c44ab/plotly_ga.js'
    })

if __name__ == '__main__':
    app.run_server(port=9000, debug=True)
