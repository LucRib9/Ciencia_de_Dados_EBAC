# Ciência de Dados -  Exercício - Módulo 15 
# Conceitos principais do pacote streamlit

# Importação dos pacotes necessários para esta tarefa
import streamlit as st # Responsável pela criação de páginas na web
import pandas as pd # Leitura de dados e construção de tabelas
import numpy as np # Possibilita diferentes operações e métodos matemáticos


st.title("Curso de Ciência de Dados - EBAC ")
st.title("Tarefa do Módulo 15")


st.title("*2. Gráficos*") 

"""
Nesta seção são visualizados dois tipos de gráficos presentes no pacote 
streamlit, o de linhas (chart) e o sobre mapa (map).
"""

"""
No caso do gráfico de linhas, vejamos o caso de 3 linhas com 20 valores
aleatórios inseridos em cada uma. 
"""
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)



"""
Em relação ao mapa, são necesários os valores de latitude e longitude do 
local que se deseja visualizar. Neste exemplo, são inseriodos 1000 valores 
aleatórios na região de San Francisco - EUA.
"""

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
