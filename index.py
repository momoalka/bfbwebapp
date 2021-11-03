import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages (add as needed)
from apps import vgames, global_sales


# Sets up page with links to other pages
app.layout = html.Div([
    html.Div([
        dcc.Link('Video Games|', href='/apps/vgames'),
        dcc.Link('Other Products|', href='/apps/global_sales'),
    ], className ="row"),
        dcc.Location(id='url', refresh = False),    #reads the path of the sublink
        html.Div(id='page-content', children = [])
])

@app.callback(Output(component_id='page-content', component_property='children'),
              [Input(component_id='url', component_property='pathname')])

def display_page(pathname):

    if pathname == '/apps/vgames':
        return vgames.layout

    if pathname == '/apps/global_sales':
        return  global_sales.layout

    else:
        return "404 Page Error! Please Choose a Link"


