import folium
import plotly.express as px
import plotly.figure_factory as ff

from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
from countryinfo import CountryInfo
import xyzservices.providers as xyz

api_token = 'b3557d7b-28a3-4743-8717-485445b16830'

def country_map(dataframe):

    m = folium.Map(location=[dataframe['latitude'].mean(), dataframe['longitude'].mean()], zoom_start=4)
    
    tile_provider = xyz.Stadia.StamenToner

    tile_provider['url'] = tile_provider['url'] + f'?api_key={api_token}'

    folium.TileLayer(
        tiles=tile_provider.build_url(api_key=api_token),
        attr=tile_provider.attribution,
        name=tile_provider.name,
        max_zoom=tile_provider.max_zoom,
        detect_retina=True
    ).add_to(m)

    folium.LayerControl().add_to(m)

    for index, line in dataframe.iterrows():
        folium.Circle(
            radius=100,
            location=(line['latitude'], line['longitude']),
            popup=line['city'],
            color="crimson",
            fill=False,
        ).add_to(m)

        folium.CircleMarker(
            location=(line['latitude'], line['longitude']),
            radius=25,
            popup=line['city'],
            color="#3186cc",
            fill=True,
            fill_color="#3186cc",
        ).add_to(m)

    folium_static(m, width=900, height=500)
    
    
    return None




def metrics(dataframe):
    metrics = []
    
    
    df_aux = dataframe[['average_cost_for_two(USD)', 'country_name']].groupby('country_name').mean().reset_index()
    
    # first metric
    max_index = df_aux['average_cost_for_two(USD)'].idxmax()
    metrics.append( (df_aux.loc[max_index, 'country_name'], df_aux.loc[max_index, 'average_cost_for_two(USD)']) )
    
    # second metric
    min_index = df_aux['average_cost_for_two(USD)'].idxmin()
    metrics.append( (df_aux.loc[min_index, 'country_name'], df_aux.loc[min_index, 'average_cost_for_two(USD)']) )
    
    
    
    # third metric
    df_aux = dataframe[['country_name', 'restaurant_id']].groupby('country_name').nunique().reset_index()
    max_index = df_aux['restaurant_id'].idxmax()
    metrics.append( (df_aux.loc[max_index, 'country_name'], df_aux.loc[max_index, 'restaurant_id']) )
    
    
    
    df_aux = dataframe[['aggregate_rating', 'country_name']].groupby('country_name').mean().reset_index()
    
    # fourth metric
    max_index = df_aux['aggregate_rating'].idxmax()
    metrics.append( (df_aux.loc[max_index, 'country_name'], df_aux.loc[max_index, 'aggregate_rating']) )
    
    
    # fifth metric
    min_index = df_aux['aggregate_rating'].idxmin()
    metrics.append( (df_aux.loc[min_index, 'country_name'], df_aux.loc[min_index, 'aggregate_rating']) )
    
    
    
    return metrics



def average_cost_graph(dataframe):
    
    df_aux = ( dataframe[['average_cost_for_two', 'country_name', 'average_cost_for_two(USD)']]
                    .groupby(['country_name'])
                    .mean()
                    .sort_values(by='average_cost_for_two(USD)', ascending=False)
                    .reset_index() 
              )
    
    
    fig = px.bar(
        df_aux, 
        x='country_name', 
        y='average_cost_for_two(USD)',
        labels={'country_name': 'Country', 'average_cost_for_two(USD)': 'Average Cost for Two (USD)'},
        title='Average Cost per Country',
        text='average_cost_for_two(USD)',
        text_auto='.2f'
    )
    
    return fig



def restaurants_graph(dataframe):
    
    df_aux = ( dataframe[['country_name', 'restaurant_id']]
              .groupby('country_name')
              .nunique().sort_values(by='restaurant_id', ascending=False)
              .reset_index()
             )
    
    fig = px.bar(
        
            df_aux, 
            x='country_name', 
            y='restaurant_id', 
            labels={'country_name': 'Country', 'restaurant_id': 'Number of Restaurants'}, 
            title='Restaurants per Country', 
            text='restaurant_id'
        )
    
    return fig



def cities_graph(dataframe):
    
    df_aux = ( dataframe[['city', 'country_name']]
              .groupby('country_name')
              .nunique().sort_values('city', ascending=False)
              .reset_index() 
             )
    
    fig = px.bar(
        
            df_aux, 
            x='country_name', 
            y='city', 
            labels={'country_name': 'Country', 'city': 'Number of Cities'}, 
            title='Cities per Country', 
            text='city'
        )
    
    return fig


def cost_distribution(dataframe, selected_country):

    df_country = dataframe.query('country_name == @selected_country')

    hist_data = []
    cities = []

    for selected_city in df_country['city'].unique():

        df_city = df_country.query('city == @selected_city')

        if df_city.shape[0] >= 50:

            hist_data.append( df_city.loc[df_city['average_cost_for_two(USD)'] < 100, 'average_cost_for_two(USD)'].values )
            cities.append(selected_city)
    
    
    fig = ff.create_distplot(hist_data, cities, bin_size=10, show_hist=False)

    fig.update_layout(title_text=f'Average Cost for Two distribution in {selected_country} (USD)')

            
    return fig

