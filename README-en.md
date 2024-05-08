# Zomato Dashboard English
[![pt-br](https://img.shields.io/badge/language-pt--br-green.svg)](https://github.com/GustavoNascimento98/zomato-food-delivery/blob/main/README.md)
[![en](https://img.shields.io/badge/language-en-red.svg)](https://github.com/GustavoNascimento98/zomato-food-delivery/blob/main/README-en.md)

![](images/zomato-banner.png)

**Table of contents**

- [1. Business Problem](#1-business-problem)
- [2. Assumptions made for the analysis](#2-assumptions-made-for-the-analysis)
- [3. Planning the solution](#3-planning-the-solution)
- [4. Top 3 Insights](#4-top-3-insights)
- [5. Final Product](#5-final-product)
- [6. Conclusion](#6-conclusion)
- [7. Next Steps](#7-next-steps)

</br>

# 1. Business Problem

Zomato is a technology company that has created an application that allows users to access information about local restaurants registered on their platform.

This company operates on a restaurant marketplace business model. In other words, its core business is to facilitate the connection and transactions between customers and restaurants. Restaurants register within Zomato's platform, which provides information such as address, type of cuisine served, whether it offers reservations, delivery services, and also a rating for the restaurant's services and products, among other details.

As a Data Scientist, I was tasked with creating a solution for the company where the main strategic KPIs could be organized in one place for easy access and decision-making.

Initially, I was provided with a dataset containing the following variables:

<details>
<summary><strong> Dataset </strong></summary>
</br>

| Column               | Description                                                                        |
| :------------------- | :--------------------------------------------------------------------------------- |
| Restaurant ID        | Restaurant ID                                                                      |
| Restaurant Name      | Name of the restaurant                                                             |
| Country Code         | Country Code                                                                       |
| City                 | City where the restaurant is located                                               |
| Address              | Restaurant address                                                                 |
| Locality             | Location and landmarks of the restaurant                                           |
| Locality Verbose     | Location and landmarks of the restaurant with further details                      |
| Longitude            | Restaurant longitude                                                               |
| Latitude             | Restaurant latitude                                                                |
| Cuisines             | Types of cuisines served at the restaurant                                         |
| Average Cost for two | Average cost for a meal for two at the restaurant                                  |
| Currency             | Country's currency                                                                 |
| Has Table booking    | Can we book tables in Restaurant? </br>1 - Yes; 0 - No                             |
| Has Online delivery  | Can we have online delivery ? </br>1 - Yes; 0 - No                                 |
| Is delivering now    | Is the Restaurant delivering food now? </br>1 - Yes; 0 - No                        |
| Switch to order menu | -                                                                                  |
| Price range          | Price range of the restaurant; </br>1 to 4 - Higher value indicates pricier dishes |
| Aggregate rating     | Average rating of the restaurant                                                   |
| Rating color         | Hexadecimal color code of the restaurant based on its average rating               |
| Rating text          | Category in which the restaurant falls based on its average rating                 |
| Votes                | Number of reviews the restaurant has received                                      |

</details></br>


With this data, we need to answer the following business questions:

<details>
<summary><strong> General </strong></summary>

1. How many restaurants are registered?


2. How many countries are registered?


3. How many cities are registered?


4. What is the total number of reviews made?


5. What is the total number of distinct cuisines?

</details></br>


<details>
<summary><strong> Country </strong></summary>

1. What is the name of the country with the most registered cities?


2. What is the name of the country with the most registered restaurants?


3. What is the name of the country with the most restaurants with a price level equal to 4 registered?


4. What is the name of the country with the highest number of distinct cuisine types?


5. What is the name of the country with the highest number of reviews made?


6. What is the name of the country with the highest number of restaurants that offer delivery?


7. What is the name of the country with the highest number of restaurants that accept reservations?


8. What is the name of the country with the highest average number of reviews registered?


9. What is the name of the country with the highest average rating registered?


10. What is the name of the country with the lowest average rating registered?


11. What is the average price of a meal for two per country?

</details></br>


<details>
<summary><strong> City </strong></summary>

1. What is the name of the city with the most registered restaurants?


2. What is the name of the city with the most restaurants with an average rating above 4?


3. What is the name of the city with the most restaurants with an average rating below 5?


4. What is the name of the city with the highest average price of a meal for two?


5. What is the name of the city with the highest number of distinct cuisine types?


6. What is the name of the city with the highest number of restaurants that accept reservations?


7. What is the name of the city with the highest number of restaurants that offer delivery?


8. What is the name of the city with the highest number of restaurants that accept online orders?


</details></br>


# 2. Assumptions made for the analysis

1. A análise foi realizada com dados de restaurantes de 15 países.

2. Cada restaurante possui uma única especialidade culinária (`cuisine`)

3. Marketplace foi o modelo de negócio assumido.

4. As 3 principais visões do negócio foram:
    1. Visão Geral
    2. Visão Países
    3. Visão Cidades
    
    

# 3. Planning the solution

O painel estratégico utilizando as métricas que refletem as 3 principais visões do modelo de negócio da empresa:
  1. Visão geral dos restaurantes
  2. Visão dos restaurantes por país
  3. Visão dos restaurantes por cidade
  

Cada visão é representada pelo seguinte conjunto de métricas:

<details>
<summary><b> Visão geral dos restaurantes </b></summary>

1. Número de restaurantes na base.


2. Número de países registrados.


3. Numero de cidades únicas.


4. Soma total de avaliações feitas.


5. Número total de tipos de culinária distintas.

</details>


<details>
<summary><b> Visão dos restaurantes por país </b></summary>

1. País com maior preço médio para dois.


2. País com menor preço médio para dois.


3. País com mais restaurantes cadastrados.


4. País com melhor média de avaliação.


5. País com pior média de avaliação.

</details>



<details>
<summary><b> Visão dos restaurantes por cidade </b></summary>

1. Cidade com mais restaurantes cadastrados.


2. Cidade com maior preço médio para dois.


3. Cidade com menor preço médio para dois.


4. Cidade com mais variações de culinária.


5. Cidade com mais avaliações com média maior que 4.

</details>



# 4. Top 3 Insights

1. Culinária Indiana possui a melhor avaliação média.

2. Brasil é o País com a pior avaliação média.

3. Turquia é o País com os restaurantes mais baratos.



# 5. Final Product

Painel online, hospedado em uma Cloud e disponível para acesso em qualquer dispositivo conectado à Internet.

O painel pode ser acessado através desse link: [Dashboard Fome Zero](https://gustavonascimento98-fome-zero.streamlit.app/)



# 6. Conclusion

O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO.

Da visão da país, podemos concluir que a Singapura é o país que possui o maior preço médio dos restaurantes.



# 7. Next Steps

1. Aumentar o número de métricas.

2. Criar novos filtros.

3. Adicionar novas visões de negócio.
