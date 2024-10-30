from dash import html,dcc
import dash_bootstrap_components as dbc
from app import app

list_of_locations = {
    'All': 0,
    'Manhattan': 1,
    'Bronx':2,
    'Brooklyn':3,
    'Queens':4,  
    'Staten Island':5,
}
slider_size = [100, 500, 1000, 10000, 100000]


controlers = dbc.Row([
    # TITULO DO DASH
    html.Img(id='logo',src=app.get_asset_url('dash_nerd.png'), style={'width':'50%','margin-top':'30px'}),
    html.H3('Vendas de imóveis - NYC', style={'margin-top':'30px'}),
    html.P('Dashboard para análise de vendas de imóveis em New York'),

    # FUNÇÕES DE SELEÇÃO 
    ### DISTRITO 
    html.H4('Distrito', style={'margin-top':'50px', 'margin-bottom':'25px'}),
    dcc.Dropdown(
        id='location-dropdown',
        options=[{'label':i,'value':j} for i,j in list_of_locations.items()],
        value=0,
        placeholder='Selecione o distrito'),

    ### METRAGEM 
    html.H4('Metragem (m2)', style={'margin-top':'20px', 'margin-bottom':'20px'}),
    dcc.Slider(min=0,max=4, id='slider-square-size', step= None,
        marks={i:str(j) for i,j in enumerate(slider_size)}),
    
    ### CONTROLE
    html.H4('Variável de controle', style={'margin-top':'20px', 'margin-bottom':'20px'}),
    dcc.Dropdown(
        options=[
            {'label':'YEAR BUILT','value':'YEAR BUILT'},
            {'label':'TOTAL UNITS','value':'TOTAL UNITS'},
            {'label':'SALE PRICE','value':'SALE PRICE'}],
        value='SALE PRICE',
        id='dropdown-color'),


])