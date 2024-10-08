# from dash import Dash, dcc, html, Input, Output, callback
# import os


# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = Dash(__name__, external_stylesheets=external_stylesheets)

# server = app.server

# app.layout = html.Div([
#     html.H1('Hello World'),
#     dcc.Dropdown(['LA', 'NYC', 'MTL'],
#         'LA',
#         id='dropdown'
#     ),
#     html.Div(id='display-value')
# ])

# @callback(Output('display-value', 'children'), Input('dropdown', 'value'))
# def display_value(value):
#     return f'You have selected {value}'

# if __name__ == '__main__':
#     app.run(debug=True)


# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc


app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(html.Div("Mobile Responsive Dash App"))),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id="example-graph", figure=fig), xs=12, sm=12, md=6),
                dbc.Col(dcc.Graph(id="example-graph2", figure=fig), xs=12, sm=12, md=6)
            ]
        ),
    ],
    fluid=True
)

# app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
#     html.H1(
#         children='Hello Dash',
#         style={
#             'textAlign': 'center',
#             'color': colors['text']
#         }
#     ),

#     html.Div(children='Dash: A web application framework for your data.', style={
#         'textAlign': 'center',
#         'color': colors['text']
#     }),

#     dcc.Graph(
#         id='example-graph-2',
#         figure=fig
#     )
# ])

if __name__ == '__main__':
    app.run(debug=True)
