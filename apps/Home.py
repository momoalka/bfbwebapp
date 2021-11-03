import dash_leaflet as dl
import json
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
import dash_bootstrap_components as dcc


GEOTIFF_ID = "geotiff-id"
GEOTIFF_MARKER_ID = "geotiff-marker-id"
COORDINATE_CLICK_ID = "coordinate-click-id"

def render_example5():

    return [
        html.H1("", style={"textAlign": "center"}),
        html.H2("Benjamin Franklin Bridge", style={"textAlign": "center"}),
        html.P("Long Span Suspension Bridge Crossing From Philadelphia, PA into Camden, NJ", style={"textAlign": "center"}),
        html.P("Project Scope:", style={"textAlign": "left",'width': 1000,'margin': "auto"}),

        # Short Project Description
        html.P(   '',
            style={'width': 1000, 'height': 215, "textAlign": "left", 'margin': "auto"},
        ),
        #html.Div(id='textarea-example-output', style={'whiteSpace': 'pre-line', 'margin': "auto"}),
        html.Img(src=app.get_asset_url('bfb.jpg'), style={'width': 1000, 'margin': "auto", 'padding': '1rem'},),

        html.P("Mapped Location:", style={"textAlign": "left", 'width': 1000, 'margin': "auto", 'padding': '1rem'}),
        #Map to Site Location
        dl.Map(style={'width': 1000, 'height': 500, 'margin': "auto", 'padding': '1rem'},
               center=[39.95348, -75.13454],
               zoom=15,
               children=[
                   dl.TileLayer(url="http://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z} "),
                   dl.GeoTIFFOverlay(id=GEOTIFF_ID, interactive=True, style={'width': '1000px', 'height': '500px'}),
                   dl.Marker(
                       id="marker",
                       interactive=True,
                       position=[39.95348, -75.13454],
                       draggable=False,
                   ),
                   html.Div(id=GEOTIFF_MARKER_ID)
               ]),

        #html.P("Coordinate (click on map):", style={"textAlign": "center"}),
        html.Div(id=COORDINATE_CLICK_ID, style={"textAlign": "center"})
    ]

@app.callback(
    Output('map', 'figure'),
    [Input('get', 'n_clicks')])

def register_example5(app):

    @app.callback(Output(GEOTIFF_MARKER_ID, 'children'),
                  [Input(GEOTIFF_ID, 'click_lat_lng_val')])
    def geotiff_marker(x):
        if x is not None:
            lat, lon, val = x
            return dl.Marker(position=[lat, lon],  children=[
                dl.Tooltip('Test')
            ])
        else:
            return None


def register_example1(app):
    @app.callback(Output(COORDINATE_CLICK_ID, 'children'),
                  [Input(GEOTIFF_ID, 'click_lat_lng_val')])
    def click_coord(e):
        if e is not None:
            return json.dumps(e)
        else:
            return "-"

# Create layout.
layout = html.Div(
    #html.H1("", style={"textAlign": "center"}),
    render_example5(), style={"textAlign": "center"})
