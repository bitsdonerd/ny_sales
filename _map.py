from dash import dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go 

###  Figures and Plots 

fig = go.Figure()
fig.update_layout(template='plotly_dark', paper_bgcolor= 'rgba(0,0,0,0)')

### Make the map 

map = dbc.Row([
    dcc.Graph(id='map-graph', figure= fig),
], style={'height':'80vh'})