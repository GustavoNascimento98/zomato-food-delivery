# Zomato Dashboard
[![pt-br](https://img.shields.io/badge/language-pt--br-green.svg)](https://github.com/GustavoNascimento98/zomato-food-delivery/blob/main/README.md)
[![en](https://img.shields.io/badge/language-en-red.svg)](https://github.com/GustavoNascimento98/zomato-food-delivery/blob/main/README-en.md)

![](images/zomato-banner.png)

**Tabela de Conteúdos**

- [1. Problema de negócio](#1-problema-de-negócio)
- [2. Premissas assumidas para a análise](#2-premissas-assumidas-para-a-análise)
- [3. Estratégia da solução.](#3-estratégia-da-solução)
- [4. Top 3 Insights de dados](#4-top-3-insights-de-dados)
- [5. Produto final do projeto](#5-produto-final-do-projeto)
- [6. Conclusão](#6-conclusão)
- [7. Próximos passos](#7-próximos-passos)

</br>

# 1. Problema de negócio

A Zomato é uma empresa de tecnologia que criou um aplicativo que permite que permite ao usuários consultar informações sobre os restaurantes locais cadastrados.

Essa empresa possui um modelo de negócios de marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da Zomato, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.

Como Cientista de Dados me foi pedido para criar uma solução para a empresa onde fosse possível ter os principais KPI’s estratégicos organizados em uma única local, para que possa consultar e conseguir tomar decisões simples, porém importantes. 

Inicialmente me foi passado um dataset com as seguintes variáveis:

<details>
<summary><strong> Dataset </strong></summary>
</br>

| Coluna               | Descrição                                                                                       |
| :------------------- | :---------------------------------------------------------------------------------------------- |
| Restaurant ID        | ID do restaurante                                                                               |
| Restaurant Name      | Nome do Restaurante                                                                             |
| Country Code         | Código do País                                                                                  |
| City                 | Nome da Cidade onde o restaurante está                                                          |
| Address              | Endereço do restaurante                                                                         |
| Locality             | Localização e pontos de referência do restaurante                                               |
| Locality Verbose     | Localização e pontos de referência do restaurante (Mais informações)                            |
| Longitude            | Ponto geográfico de Longitude do Restaurante                                                    |
| Latitude             | Ponto geográfico de Latitude do Restaurante                                                     |
| Cuisines             | Tipos de Culinária servidos no restaurante                                                      |
| Average Cost for two | Preço Médio de um prato para duas pessoas no restaurante                                        |
| Currency             | Moeda do país                                                                                   |
| Has Table booking    | Se o restaurante possui serviços de reserva; </br>1 - Sim; 0 - Não                              |
| Has Online delivery  | Se o restaurante possui serviços de pedido on-line; </br>1 - Sim; 0 - Não                       |
| Is delivering now    | Se o restaurante faz entregas; 1 - Sim; 0 - Não                                                 |
| Switch to order menu | -                                                                                               |
| Price range          | Variação de preços do restaurante; </br>1 a 4 - Quanto maior o valor, mais caro serão os pratos |
| Aggregate rating     | Nota média do restaurante                                                                       |
| Rating color         | Código Hexadecimal da cor do restaurante com base em sua nota média                             |
| Rating text          | Categoria em que o restaurante está com base em sua nota média                                  |
| Votes                | Quantidade de avaliações que o restaurante já recebeu                                           |

</details></br>


Com esses dados devemos responder as seguinte questões de negócios:

<details>
<summary><strong> Geral </b></summary>

1. Quantos restaurantes únicos estão registrados?


2. Quantos países únicos estão registrados?


3. Quantas cidades únicas estão registradas?


4. Qual o total de avaliações feitas?


5. Qual o total de tipos de culinária registrados?

</details></br>


<details>
<summary><strong> País </strong></summary>

1. Qual o nome do país que possui mais cidades registradas?


2. Qual o nome do país que possui mais restaurantes registrados?


3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?


4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?


5. Qual o nome do país que possui a maior quantidade de avaliações feitas?


6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?


7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?


8. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?


9. Qual o nome do país que possui, na média, a maior nota média registrada?


10. Qual o nome do país que possui, na média, a menor nota média registrada?


11. Qual a média de preço de um prato para dois por país?

</details></br>


<details>
<summary><strong> Cidade </strong></summary>

1. Qual o nome da cidade que possui mais restaurantes registrados?


2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?


3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 5?


4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?


5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?


6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?


7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?


8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?

</details></br>


# 2. Premissas assumidas para a análise

1. A análise foi realizada com dados de restaurantes de 15 países.

2. Cada restaurante possui uma única especialidade culinária (`cuisine`)

3. Marketplace foi o modelo de negócio assumido.

4. As 3 principais visões do negócio foram:
    1. Visão Geral
    2. Visão Países
    3. Visão Cidades
    
    

# 3. Estratégia da Solução

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



# 4. Top 3 Insights de dados

1. Culinária Indiana possui a melhor avaliação média.

2. Brasil é o País com a pior avaliação média.

3. Turquia é o País com os restaurantes mais baratos.



# 5. Produto final do projeto

Painel online, hospedado em uma Cloud e disponível para acesso em qualquer dispositivo conectado à Internet.

O painel pode ser acessado através desse link: [Dashboard Fome Zero](https://gustavonascimento98-fome-zero.streamlit.app/)



# 6. Conclusão

O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO.

Da visão da país, podemos concluir que a Singapura é o país que possui o maior preço médio dos restaurantes.



# 7. Próximos passos

1. Aumentar o número de métricas.

2. Criar novos filtros.

3. Adicionar novas visões de negócio.
