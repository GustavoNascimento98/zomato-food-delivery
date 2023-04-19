import streamlit as st
from PIL import Image


st.set_page_config(page_title='Home', page_icon='🏠', layout='wide')


image_path = 'images/logo.png'
image = Image.open(image_path)
st.sidebar.image(image, width=120)

st.sidebar.markdown('# Fome Zero')
st.sidebar.markdown('#### The best way to get your food')
st.sidebar.markdown('''---''')
st.sidebar.markdown('#### Powered by Comunidade DS')

st.sidebar.markdown('''

Ask for Help

Data Science Team on Discord
'''
)

with st.container():
    
    cols = st.columns([5, 1])
    
    with cols[0]:
 
        st.write('# Welcome to Fome Zero')

        st.write('## The best place to find your favorite restaurant!')
        
    with cols[1]:

        image_path = 'images/restaurant'
        image = Image.open(image_path)
        st.image(image, width=120)




st.write('### How to use this dashboard?')

st.write("""
* **Overall:**
    * **Gerential View**: Main metrics.
    * **Tatics View**: Currency exchange rates.
    * **Geographical View**: Insights of geolocalization.

&nbsp;

* **Country View:**
    * Main metrics per country.
    * Selected country overview

&nbsp;

* **City View:**
    * Main metrics per city.
    * Selected city restaurants information.


""")



if 'price_range' not in st.session_state:
    st.session_state.price_range = (0.0, 400.0)
    
    
if 'countries' not in st.session_state:
    st.session_state.countries = ['Brazil', 'United States of America', 'Australia', 'United Kingdom', 'Canada', 'Turkey', 'South Africa']
    
    
if 'country' not in st.session_state:
    st.session_state.country = st.session_state.countries[0]