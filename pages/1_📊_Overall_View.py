# importing important libraries

import pandas as pd
import plotly.express as px
import numpy as np
import datetime
import streamlit as st
from PIL import Image



import modules.utils as utils

df = pd.read_csv('dataset/zomato.csv')

df1 = utils.clean_dataset(df)



st.set_page_config(page_title='Overall', page_icon='📊', layout='wide')


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



countries_list = df1['country_name'].unique().tolist()

countries_options = st.sidebar.multiselect(
    'Select the countries: ',
    countries_list,
    default=st.session_state.countries
)



df1 = df1.loc[df1['average_cost_for_two(USD)'].between(*price_range, inclusive=True), :]
df1 = df1.loc[df1['country_name'].isin(countries_options), :]

# ================================================================================================================



# ================================================================================================================
# Layout streamlit
# ================================================================================================================


st.markdown('# 📊 Overall Metrics')

with st.container():
    col1, col2, col3, col4, col5 = st.columns(5, gap='large')
    
    with col1:
        number_restaurants = df1['restaurant_id'].nunique()
        col1.metric('Restaurants', number_restaurants)
        
    with col2:
        number_countries = df1['country_name'].nunique()
        col2.metric('Countries', number_countries)
        
    with col3:
        number_cities = df1['city'].nunique()
        col3.metric('Cities', number_cities)
        
    with col4:
        total_ratings = df1['votes'].sum()
        col4.metric('Total Ratings', f'{total_ratings:,}')
        
    with col5:
        number_cuisines = df1['cuisines'].nunique()
        col5.metric('Cuisines', number_cuisines)

        
        

st.markdown('''---''')


country_currency = { country: utils.exchange_rate(country) for country in df1['country_name'].unique() }

df_currency = ( pd.DataFrame(country_currency.items(), columns=['country', 'exchange_rate(USD)'])
               .sort_values('exchange_rate(USD)')
               .reset_index(drop=True) )

with st.expander('Exchange Rates'):
    
    cols = st.columns(2)
    
    with cols[0]:
        current_time = datetime.datetime.now()
        
        st.write('## Current Time')
        st.write(current_time.strftime("%a, %b %d, %Y"))
        st.write(current_time.strftime("%I:%M:%S %p"))
        
        next_day = datetime.datetime.today() + datetime.timedelta(days=1)
        st.write('## Next Update')
        st.write(next_day.strftime("%a, %b %d, %Y"))
        st.write(current_time.strftime("00:00:01 AM"))
        
        
    with cols[1]:
        st.dataframe(df_currency)


    
st.markdown('## Restaurants Location')

with st.container():
    utils.map_view(df1)


    

st.session_state.update({
    'price_range': price_range,
    'countries': countries_options,
    'country': countries_options[0]
})