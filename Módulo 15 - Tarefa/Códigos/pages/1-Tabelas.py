# Ciência de Dados -  Exercício - Módulo 15 
# Conceitos principais do pacote streamlit

# Importação dos pacotes necessários para esta tarefa
import streamlit as st # Responsável pela criação de páginas na web
import pandas as pd # Leitura de dados e construção de tabelas
import numpy as np # Possibilita diferentes operações e métodos matemáticos


st.title("Curso de Ciência de Dados - EBAC ")
st.title("Tarefa do Módulo 15")

st.title("*1. Tabelas*")

"""
Nesta seção vamos criar algumas tabelas (interativas e fixas) através de 
diferentes métodos. 
"""

"""
A primeira tabela é criada através do comando DataFrame do pacote Pandas e
lida diretamente pelos Magic commands do pacote Streamlit.
"""

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df


"""
No segundo caso, a mesma tabela é lida pelo comando st.write do streamlit.
"""
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))



"""
Uma última forma de ler uma tabela é pelo comando st.dataframe do pacote 
streamlit. Ela também é interativa.
"""

# Criação de uma tabela de 10 linhas e 20 colunas, com números aleatórios
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)



"""
Pelo streamlit é possível destacar certos componentes de uma tabela. No caso 
abaixo são destacados os valores máximos de uma tabela semelhante à anterior
(com valores aleatórios).
"""

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))



"""
Para terminar esta seção, vamos fazer a leitura de uma tabela pelo comando 
st.table do streamlit, na qual a tabela resultante é fixa (não-interativa).
Ou seja, não é possível destacar elemento algum, apenas visualizá-lo.
"""

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.table(dataframe)
