import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash
import dash_leaflet as dl


# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages (add as needed)
from apps import vgames, global_sales, Home

navbar = dbc.Navbar(
        dbc.Container(
            [
                dbc.NavbarBrand("Benjamin Franklin Bridge Data Dashboard", href='#'),
                dbc.Nav(
                    [
                        dbc.NavItem(dbc.NavLink('Home', href='/apps/Home')),
                        dbc.DropdownMenu(
                        children=[
                            #dbc.DropdownMenuItem(dcc.Link('Other Options', href='/apps/global_sales'), header=True),
                            dbc.DropdownMenuItem(dcc.Link('Video Games', href='/apps/vgames')),
                            dbc.DropdownMenuItem(dcc.Link('Global Sales', href='/apps/global_sales')),
                        ],
                        nav=True,
                        in_navbar=True,
                        label="More",
                    ),
                ],
                className="mr-auto",
                navbar=True,
            ),
        ],
    ),

    color="primary",
    dark=True,

)


content = html.Div(id="page-content", children=[])

app.layout = html.Div([
    dcc.Location(id="url"),
    navbar,
    content,
])



'''
# Sets up page with links to other pages
app.layout = html.Div([
    html.Div([
        dcc.Link('Video Games | ', href='/apps/vgames'),
        dcc.Link('Other Products | ', href='/apps/global_sales'),
        dcc.Link('Apples | ', href='/apps/global_sales'),
        dcc.Link('Bananas | ', href='/apps/global_sales'),
    ], className="row"),
        dcc.Location(id='url', refresh = False),    #reads the path of the sublink
        html.Div(id='page-content', children = [])
])
'''

@app.callback(Output(component_id='page-content', component_property='children'),
              [Input(component_id='url', component_property='pathname')])


def display_page(pathname):

    if pathname == '/apps/Home':
        return  Home.layout

    if pathname == '':
        return  Home.layout

    if pathname == '/apps/vgames':
        return vgames.layout

    if pathname == '/apps/global_sales':
        return  global_sales.layout

    else:
        return "404 Page Error! Please Choose a Link"

# Leave code in to test locally, otherwise remove before deployment
if __name__ == '__main__':
    app.run_server(debug=True)