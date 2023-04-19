
import pandas as pd
import plotly.express as px
import numpy as np
import inflection
from countryinfo import CountryInfo
import requests

import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

    

def country_name(id_country):
    return countries.get(id_country)


def create_price_tag(price_tag):
    if price_tag == 1:
        return 'cheap'
    elif price_tag == 2:
        return 'normal'
    elif price_tag == 3:
        return 'expensive'
    else:
        return 'gourmet'
    

def color_name(color_code):
    return colors.get(color_code)


def rename_columns(dataframe):
    df = dataframe.copy()
    old_cols = list(df.columns)

    old_cols = map(lambda x: inflection.titleize(x), old_cols)    # Uppercase the first letter of each word in a string
    old_cols = map(lambda x: x.replace(' ', ''), old_cols)        # Remove all spaces in the string

    new_cols = map(lambda x: inflection.underscore(x), old_cols)  # Adds an underscore '_' before all uppercase letters and
                                                                  # lowercases the whole string

    df.columns = new_cols

    return df



def exchange_rate(country_name):
    currency_code = CountryInfo(country_name).currencies()[0]

    return conversion_rates.get(currency_code)





def clean_dataset(dataframe):
    df1 = dataframe.copy()

    # Elimina todos os registros (linhas) que possuem algum elemento faltante (NaN)
    df1 = df1[df1.notnull().all(axis=1)]

    # Adiciona a coluna 'Country Name'
    countries_column = df1['Country Code'].apply(country_name)
    df1.insert(
        loc=3,
        column='Country Name',
        value=countries_column
    )

    # Adiciona a coluna 'Price Tag'
    price_tag_column = df1['Price range'].apply(create_price_tag)
    df1.insert(
        loc=18,
        column='Price Tag',
        value=price_tag_column
    )

    # Adiciona a coluna de 'Color Ranking'
    color_ranking_column = df1['Rating color'].apply(color_name)
    df1.insert(
        loc=21,
        column='Color Ranking',
        value=color_ranking_column
    )

    # Selecionando o tipo de prato 'Cuisine'
    df1['Cuisines'] = df1['Cuisines'].apply(lambda x: x.split(',')[0])


    # Renomeando as colunas
    df1 = rename_columns(df1)
    
    
    country_currency = { country: exchange_rate(country) for country in df1['country_name'].unique() }
    
    
    # Cria a coluna de preços para dois países
    df1['average_cost_for_two(USD)'] = df1.apply(lambda x: x['average_cost_for_two'] / country_currency.get(x['country_name']), axis=1)
    
    
    
    good      = ['Bueno', 'Bom', 'Buono', 'Baik', 'İyi']
    very_good = ['Muito bom', 'Muito Bom', 'Bardzo dobrze', 'Muy Bueno', 'Skvělá volba', 'Velmi dobré', 'Veľmi dobré', 'Çok iyi', 'Sangat Baik']
    excellent = ['Excelente', 'Vynikajúce', 'Harika', 'Eccellente', 'Skvělé', 'Wybitnie', 'Terbaik']
    average   = ['Biasa']
    
    # Agrupa as notas de avaliação em uma mesma lingua
    df1['rating_text'] = df1['rating_text'].replace(very_good, 'Very Good')
    df1['rating_text'] = df1['rating_text'].replace(good, 'Good')
    df1['rating_text'] = df1['rating_text'].replace(excellent, 'Excellent')
    df1['rating_text'] = df1['rating_text'].replace(average, 'Average')
    
    
    return df1




def map_view(dataframe, lat=0, lon=0, zoom=1):
    df = dataframe.copy()
    
    # create an empty canvas in which we will add the map
    fig = folium.Figure(width=1920, height=1080)
    
    # create the map object and adds it to the canvas ('fig')
    map_ = folium.Map(location=(lat, lon), max_bounds=True, zoom_start=zoom).add_to(fig)
    
    # create the object ('instance') of the class MarkerCluster which will cluster the markers on the map
    marker_cluster = MarkerCluster().add_to(map_)

    
    for index, line in df.iterrows():
        
        name = line["restaurant_name"]
        price_for_two_USD = line["average_cost_for_two(USD)"]
        cuisine = line["cuisines"]
        rating = line["aggregate_rating"]
        color = f'{line["color_ranking"]}'
        
        html = "<p><strong>{}</strong></p>"
        html += "<p>Price: {} USD for two"
        html += "<br />Type: {}"
        html += "<br />Aggragate Rating: {}/5.0"
        
        html = html.format(name, round(price_for_two_USD, 2), cuisine, rating)

        popup = folium.Popup(
            folium.Html(html, script=True),
            max_width=500,
        )
        
        
        folium.Marker(
            location=(line['latitude'], line['longitude']),
            popup=popup,
            icon=folium.Icon(color=color, icon='home', prefix='fa')
        
        ).add_to(marker_cluster)
        
    folium_static(map_, width=900, height=500)
    
    return None





countries = {
    1: 'India',
    14: 'Australia',
    30: 'Brazil',
    37: 'Canada',
    94: 'Indonesia',
    148: 'New Zealand',
    162: 'Philippines',
    166: 'Qatar',
    184: 'Singapore',
    189: 'South Africa',
    191: 'Sri Lanka',
    208: 'Turkey',
    214: 'United Arab Emirates',
    215: 'United Kingdom',
    216: 'United States of America',
}



colors = {
    '3F7E00': 'darkgreen',
    '5BA829': 'green',
    '9ACD32': 'lightgreen',
    'CDD614': 'orange',
    'FFBA00': 'red',
    'CBCBC8': 'darkred',
    'FF7800': 'darkred',
}




# Where USD is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/42b6485eff2810800b518ee1/latest/USD'

# Making our request
response = requests.get(url)
data = response.json()

conversion_rates = data.copy().get('conversion_rates')


