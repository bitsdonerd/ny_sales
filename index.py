from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from app import app
from _map import * 
from _histogram import *
from _controllers import * 

###  Data Manipulation 
df_data = pd.read_csv(r"C:/Users/Lukas/Documents/Data Science/WORKSPACE/ny_sales\dataset/cleaned_data.csv", index_col=0)
mean_lat = df_data['LATITUDE'].mean()
mean_long = df_data['LONGITUDE'].mean()
df_data['size_m2'] = df_data['GROSS SQUARE FEET'] / 10.764
df_data = df_data[df_data['YEAR BUILT'] > 0]
df_data['SALE DATE'] = pd.to_datetime(df_data['SALE DATE'])

### Manipulation of House Sizes 
df_data.loc[df_data['size_m2'] > 10000, 'size_m2'] = 10000
df_data.loc[df_data['SALE PRICE'] > 50000000, 'SALE PRICE'] = 50000000
df_data.loc[df_data['SALE PRICE'] < 10000, 'SALE PRICE'] = 10000

### Layout
app.layout = dbc.Container(
        children=[
            dbc.Row([
                dbc.Col([controlers], md=3),
                dbc.Col([map, hist], md=9),

            ])

        ], fluid=True, )

### Callbacks
@app.callback([Output('hist-graph', 'figure'),Output('map-graph', 'figure')],
            [Input('location-dropdown', 'value'),
             Input('slider-square-size', 'value'),
             Input('dropdown-color', 'value')])

def update_hist(location, square_size, color_map):
    if location is None:
        df_intermediate =df_data.copy()
    else:
        df_intermediate = df_data[df_data['BOROUGH'] == location] if location != 0 else df_data.copy()
        size_limit = slider_size[square_size] if square_size is not None else df_data['GROSS SQUARE FEET'].max()
        df_intermediate =  df_intermediate[df_intermediate['GROSS SQUARE FEET'] <= size_limit]

    hist_fig = px.histogram(df_intermediate,x=color_map, opacity=0.75)
    hist_layout = go.Layout(
        margin = go.layout.Margin(l=10, r=0, t=0, b=50),
        showlegend=False,
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)')
    hist_fig.layout = hist_layout
    

    px.set_mapbox_access_token(open('keys/mapbox_key').read())
    map_fig = px.scatter_mapbox(df_intermediate, lat="LATITUDE", lon="LONGITUDE",color=color_map, size="size_m2", size_max=15, zoom=10, opacity=0.4)
    map_fig.update_layout(mapbox=dict(center=go.layout.mapbox.Center(lat=mean_lat,lon=mean_long)),
        template='plotly_dark', paper_bgcolor= 'rgba(0,0,0,0)',
        margin=go.Margin(l=10,r=10,t=10,b=10))
    

    return hist_fig, map_fig

if __name__ == '__main__':
    app.run_server(debug=True)