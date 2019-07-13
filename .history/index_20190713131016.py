import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app
server = app.server
from apps import world, country

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    dcc.ConfirmDialog(
        id='confirm',
        message='Danger danger! Are you sure you want to continue?'
    )
])



@app.callback(Output('page-content', 'children'),
             [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/country':
        return country.layout

    else:
        return world.layout

if __name__ == '__main__':
    app.run_server()