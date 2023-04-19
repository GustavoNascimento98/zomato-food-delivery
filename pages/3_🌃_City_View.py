import pandas as pd
import plotly.express as px
import numpy as np
import streamlit as st
from PIL import Image

import inflection
import seaborn as sns
import matplotlib.pyplot as plt

import modules.utils as utils
import modules.cities_data as cities_data

df = pd.read_csv('dataset/zomato.csv')

df1 = utils.clean_dataset(df)


st.set_page_config(page_title='City View', page_icon='🌃', layout='wide')

# ================================================================================================================
# Sidebar
# ================================================================================================================

image_path = 'images/logo.png'
image = Image.open(image_path)

st.sidebar.image(image, width=120)

st.sidebar.markdown('# Fome Zero')
st.sidebar.markdown('#### The best way to get your food')
st.sidebar.markdown('''---''')



price_range = st.sidebar.slider(
    label='Select the price range (USD)',
    value=st.session_state.price_range,
    min_value=0.0,
    max_value=650.0
)

#st.session_state.price_range = price_range



countries_list = df1['country_name'].unique().tolist()

countries_options = st.sidebar.multiselect(
    'Select the countries: ',
    countries_list,
    default=st.session_state.countries
)

#st.session_state.countries = countries_options



df1 = df1.loc[df1['average_cost_for_two(USD)'].between(*price_range, inclusive=True), :]
df1 = df1.loc[df1['country_name'].isin(countries_options), :]

# ================================================================================================================


# ================================================================================================================
# Layout streamlit
# ================================================================================================================


st.markdown('# 🌃 City View')


country_map = { country: country.lower().replace(' ', '_') for country in df1['country_name'].unique()}

with st.container():
    cols = st.columns(5, gap='large')
    
    metrics = cities_data.metrics(df1)
    
    with cols[0]:
        
        city, country, value = metrics[0]
        
        st.metric('Most restaurants', value)
        st.write(f'**{city}**')
        country_flag = Image.open(f'images/flags/{country_map.get(country)}.png')
        st.image(country_flag)
        
        
    with cols[1]:
        
        city, country, value = metrics[1]
        
        st.metric('Highest average price', f'${value:.2f}')
        st.write(f'**{city}**')
        country_flag = Image.open(f'images/flags/{country_map.get(country)}.png')
        st.image(country_flag)
        
        
    with cols[2]:
        
        city, country, value = metrics[2]
        
        st.metric('Lowest average price', f'${value:.2f}')
        st.write(f'**{city}**')
        country_flag = Image.open(f'images/flags/{country_map.get(country)}.png')
        st.image(country_flag)
        
        
    with cols[3]:
        
        city, country, value = metrics[3]
        
        st.metric('Most cuisines', value)
        st.write(f'**{city}**')
        country_flag = Image.open(f'images/flags/{country_map.get(country)}.png')
        st.image(country_flag)
        
    with cols[4]:
        
        city, country, value = metrics[4]
        
        st.metric('Restaurant Rated >4', value)
        st.write(f'**{city}**')
        country_flag = Image.open(f'images/flags/{country_map.get(country)}.png')
        st.image(country_flag)


        
        
st.divider()


st.write('# Restaurants in the selected city')

with st.container():
    cols = st.columns(2)
    
    with cols[0]:

        
        selected_country = st.selectbox('Select a Country', countries_options)
        
        
        df2 = df1.query('country_name == @selected_country').copy()
        
        
        
        selected_city = st.selectbox('Select a City', df2['city'].unique())
        
        rating_option = st.radio('Select a rating option:', ('All', *df2['rating_text'].unique()))
        
        
        if rating_option != 'All':
            df2 = df2.query('rating_text == @rating_option')
        
        
        
    with cols[1]:
        
        with st.container():
            st.empty()
        with st.container():
            st.empty()
        with st.container():
            st.empty()
        with st.container():
            st.empty()
        with st.container():
            st.empty()
        with st.container():
            st.empty()
        with st.container():
            st.empty()
        with st.container():
            st.empty()
        with st.container():
            st.empty()
        with st.container():
            st.empty()
        with st.container():
            st.empty()
            
        
        with st.container():
            st.write(f'## {selected_city}')

            country_flag = Image.open(f'images/flags/{country_map.get(selected_country)}.png')
            st.image(country_flag)

            delivering = st.checkbox('Only restaurants with delivering?')

            if delivering:
                df2 = df2.query('has_online_delivery == 1')
                st.write('Showing only the restaurants with delivery service')


                
with st.container():
    
    df2_city = df2.query('city == @selected_city')
    latitude, longitude = df2_city['latitude'].median(), df2_city['longitude'].median()
    
    try:
        utils.map_view(df2_city, lat=latitude, lon=longitude, zoom=9)
        
    except:
        st.write('## No Matches Found')
        map_error = Image.open('images/map_error.png')
        st.image(map_error)



st.divider()

st.write('# City Metrics')

with st.container():
    
    tabs = st.tabs(['Restaurants', 'Ratings', 'Cuisines'])
    
    with tabs[0]:
        fig = cities_data.restaurants_graph(df1)
        st.plotly_chart(fig, use_container_width=True)
    
    
    with tabs[1]:
        
        cols = st.columns(2)
        
        with cols[0]:
            fig = cities_data.rated_over_4_graph(df1)
            st.plotly_chart(fig, use_container_width=True)
            
        with cols[1]:
            fig = cities_data.rated_under_2dot5_graph(df1)
            st.plotly_chart(fig, use_container_width=True)
            
            
    with tabs[2]:
        fig = cities_data.cuisines_graph(df1)
        st.plotly_chart(fig, use_container_width=True)

    

st.session_state.update({
    'price_range': price_range,
    'countries': countries_options,
    'country': selected_country
})