import folium
import plotly.express as px

from countryinfo import CountryInfo



def metrics(dataframe):
    
    metrics = []
    
    # first metric
    df_aux = dataframe[['restaurant_id', 'city', 'country_name']].groupby(['city', 'country_name']).nunique().reset_index()
    
    max_index = df_aux['restaurant_id'].idxmax()
    city, country, value = df_aux.loc[max_index, 'city'], df_aux.loc[max_index, 'country_name'], df_aux.loc[max_index, 'restaurant_id']
    metrics.append( (city, country, value) )
    
    
    
    df_aux = dataframe[['average_cost_for_two(USD)', 'city', 'country_name']].groupby(['city', 'country_name']).mean().reset_index()
    
    # second metric
    max_index = df_aux['average_cost_for_two(USD)'].idxmax()
    city, country, value = df_aux.loc[max_index, 'city'], df_aux.loc[max_index, 'country_name'], df_aux.loc[max_index, 'average_cost_for_two(USD)']
    metrics.append( (city, country, value) )
    
    
    # third metric
    min_index = df_aux['average_cost_for_two(USD)'].idxmin()
    city, country, value = df_aux.loc[min_index, 'city'], df_aux.loc[min_index, 'country_name'], df_aux.loc[min_index, 'average_cost_for_two(USD)']
    metrics.append( (city, country, value) )
    
    
    
    # fourth metric
    df_aux = dataframe[['cuisines', 'city', 'country_name']].groupby(['city', 'country_name']).nunique().reset_index()
    
    max_index = df_aux['cuisines'].idxmax()
    city, country, value = df_aux.loc[max_index, 'city'], df_aux.loc[max_index, 'country_name'], df_aux.loc[max_index, 'cuisines']
    metrics.append( (city, country, value) )
    
    
    # fifth metric
    df_aux = ( dataframe.query('aggregate_rating > 4')[['restaurant_id', 'city', 'country_name']]
              .groupby(['city', 'country_name']).nunique().reset_index() )
    
    max_index = df_aux['restaurant_id'].idxmax()
    city, country, value = df_aux.loc[max_index, 'city'], df_aux.loc[max_index, 'country_name'], df_aux.loc[max_index, 'restaurant_id']
    metrics.append( (city, country, value) )
    
    return metrics
    
    
    
def restaurants_graph(dataframe):
    df_aux = ( dataframe[['restaurant_id', 'city', 'country_name']]
          .groupby(['city', 'country_name'])
          .nunique()
          .sort_values('restaurant_id', ascending=False)
          .reset_index() 
         )
    
    
    fig = px.bar(df_aux.head(10),
       x='city', 
       y='restaurant_id', 
       color='country_name', 
       text='restaurant_id',
       title='Top 10 cities with most restaurants',
       labels={'city': 'City', 'restaurant_id': 'Number of Restaurants', 'country_name': 'Country'}
      )
    
    return fig


def rated_over_4_graph(dataframe):
    
    df_aux = ( dataframe.loc[dataframe['aggregate_rating'] > 4, ['restaurant_id', 'city', 'country_name']]
              .groupby(['country_name', 'city'])
              .nunique()
              .sort_values(['restaurant_id', 'city'], ascending=[False, True])
              .reset_index() )
    
    fig = px.bar(df_aux.head(7),
       x='city',
       y='restaurant_id',
       text='restaurant_id', 
       color='country_name',
       labels={'city': 'City', 'restaurant_id': 'Number of restaurantes', 'country': 'Country'},
       title='Top 7 cities with more restaurants rated over 4'
       
      )
    
    return fig


def rated_under_2dot5_graph(dataframe):
    
    df_aux = ( dataframe.loc[dataframe['aggregate_rating'] < 2.5, ['restaurant_id', 'city', 'country_name']]
              .groupby(['country_name', 'city'])
              .nunique()
              .sort_values(['restaurant_id', 'city'], ascending=[False, True])
              .reset_index() )
    
    fig = px.bar(df_aux.head(7),
       x='city',
       y='restaurant_id',
       text='restaurant_id', 
       color='country_name',
       labels={'city': 'City', 'restaurant_id': 'Number of restaurantes', 'country': 'Country'},
       title='Top 7 cities with more restaurants rated under 2.5'
       
      )
    
    return fig


def cuisines_graph(dataframe):
    
    df_aux = ( dataframe[['cuisines', 'city', 'country_name']]
          .groupby(['city', 'country_name'])
          .nunique()
          .sort_values('cuisines', ascending=False)
          .reset_index() 
         )
    
    
    fig = px.bar(
        
        df_aux.head(10),
        x='city',
        y='cuisines',
        text='cuisines',
        color='country_name',
        labels={'city': 'City', 'cuisines': 'Cuisines', 'country_name': 'Country'},
        title='Top 10 cities with most variety of cuisines'
    )
    
    
    return fig