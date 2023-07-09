# Ciência de Dados -  Exercício - Módulo 15 
# Conceitos principais do pacote streamlit

# Importação dos pacotes necessários para esta tarefa
import streamlit as st # Responsável pela criação de páginas na web
import pandas as pd # Leitura de dados e construção de tabelas
import numpy as np # Possibilita diferentes operações e métodos matemáticos


st.title("Curso de Ciência de Dados - EBAC ")
st.title("Tarefa do Módulo 15")


st.title("*3. Widgets*")

"""
Nesta página encontram-se alguns dos widgets presentes no pacote streamlit.
Divirta-se com eles!
"""

"""
No primeiro exemplo, temos um slider que devolve o quadrado do número 
selecionado:
"""
x = st.slider('x')  # 👈 isto é um widget
st.write(x, 'ao quadrado é', x * x)


"""
Um ponto muito importante do pacote streamlit é o de poder salvar textos, 
valores, comandos, entre outras coisas em chaves (keys). No exemplo abaixo, 
é possível salvar seu nome na chave "nome".
"""

st.text_input("Seu nome", key="nome")

"""
O valor de uma chave pode ser visualizado em qualquer momento, através do 
comando st.session_state.[chave]:
"""
st.session_state.nome


"""
Outro fator importante é a possibilidade de esconder um algum componente da
página (gráfico, tabela, imagem) através do comando st.checkbox. Quando 
marcado (tal como neste exemplo) o item fica visível na página.
"""

if st.checkbox('Mostrar tabela'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data


"""
No último exemplo de widget, será guardado um termo selecionado de uma tabela
dentro de uma variável. 
"""

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Qual é o seu número preferido nas opções abaixo?',
     df['first column'])

'You selected: ', option