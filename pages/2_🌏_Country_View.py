import pandas as pd
import plotly.express as px
import numpy as np
import streamlit as st
from PIL import Image

from countryinfo import CountryInfo

import modules.utils as utils
import modules.countries_data as countries_data 


df = pd.read_csv('dataset/zomato.csv')

df1 = utils.clean_dataset(df)

st.set_page_config(page_title='Country View', page_icon='🌏', layout='wide')

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



df1 = df1.loc[df1['average_cost_for_two(USD)'].between(*price_range, inclusive='both'), :]
df1 = df1.loc[df1['country_name'].isin(countries_options), :]

# ================================================================================================================


# ================================================================================================================
# Layout streamlit
# ================================================================================================================


st.markdown('# 🌎 Country View')

country_map = { country: country.lower().replace(' ', '_') for country in df1['country_name'].unique()}

with st.container():
    cols = st.columns(5, gap='large')
    
    metrics = countries_data.metrics(df1)
    
    with cols[0]:
        
        country, value = metrics[0]
        
        st.metric('Highest average price', f'${value:.2f}')
        st.write(country)
        
        country_flag = Image.open(f'images/flags/{country_map.get(country)}.png')
        st.image(country_flag)
        
        
    with cols[1]:
        
        country, value = metrics[1]
        
        st.metric('Lowest average price', f'${value:.2f}')
        st.write(country)
        
        country_flag = Image.open(f'images/flags/{country_map.get(country)}.png')
        st.image(country_flag)
        
        
    with cols[2]:
        
        country, value = metrics[2]
        
        st.metric('Most Restaurants', value)
        st.write(country)
        
        country_flag = Image.open(f'images/flags/{country_map.get(country)}.png')
        st.image(country_flag)
        
        
    with cols[3]:
        
        country, value = metrics[3]
        
        st.metric('Best Rated (Average)', f'{value:.1f}/5.0')
        st.write(country)
        
        country_flag = Image.open(f'images/flags/{country_map.get(country)}.png')
        st.image(country_flag)
        
        
    with cols[4]:
        
        country, value = metrics[4]
        
        st.metric('Worst Rated (Average)', f'{value:.1f}/5.0')
        st.write(country)
        
        country_flag = Image.open(f'images/flags/{country_map.get(country)}.png')
        st.image(country_flag)

        
        
st.divider()



st.write('# Main Metrics per Country')

with st.container():
    tabs = st.tabs(['Average Cost', 'Restaurants', 'Cities'])
    
    with tabs[0]:
        fig = countries_data.average_cost_graph(df1)
        
        st.plotly_chart(fig, use_container_width=True)
        
        
    with tabs[1]:
        fig = countries_data.restaurants_graph(df1)
        
        st.plotly_chart(fig, use_container_width=True)
        
        
    with tabs[2]:
        fig = countries_data.cities_graph(df1)
        
        st.plotly_chart(fig, use_container_width=True)
        
        
        
st.divider()



st.markdown('# Information Selected Country')


with st.container():
    cols = st.columns(2)
    
    with cols[0]:
        
        try:
            index_default = countries_options.index(st.session_state.country)
        except:
            index_default = 0
        
        
        country_selected_view = st.selectbox('Select a Country', countries_options, index=index_default)
        
        country_flag = Image.open(f'images/flags/{country_map.get(country_selected_view)}.png')
        st.image(country_flag)
        
        country_infos = CountryInfo(country_selected_view)
        
        
        
    with cols[1]:
        st.write(f'**Capital**:    &nbsp;&nbsp;{country_infos.capital()}')
        st.write(f'**Population**: &nbsp;&nbsp;{country_infos.population():,}')
        st.write(f'**Continent**:  &nbsp;&nbsp;{country_infos.region()}')
        st.write(f'**Region**:     &nbsp;&nbsp;{country_infos.subregion()}')
        
        
        
df_country = df1.query('country_name == @country_selected_view')[['city', 'latitude', 'longitude']]
df_aux = df_country.groupby('city').median().reset_index()

with st.container():
    tabs = st.tabs(['Map View', 'Cost Distribution per City'])
    
    with tabs[0]:
        countries_data.country_map(df_aux)
        
    with tabs[1]:
        
        try:
            
            fig = countries_data.cost_distribution(df1, country_selected_view)
            
            st.write('### This graph only accounts for the restaurants whose cost was bellow 100 USD')
            
            st.plotly_chart(fig, use_container_width=True)
            
        except:
            
            cols = st.columns([1, 4])
            
            with cols[0]:
                image = Image.open(f'images/not_found')
                st.image(image, width=200)
                
            with cols[1]:
                st.empty()
                st.write('## There is not enough data to make a distribution')
                st.write('It is necessary at least 50 datapoints for each city.')
                st.write('None of them have met the requirement.')
            
            
            

st.session_state.update({
    'price_range': price_range,
    'countries': countries_options,
    'country': country_selected_view
})
