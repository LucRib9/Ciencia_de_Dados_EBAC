# Ciência de Dados -  Exercício - Módulo 15 
# Conceitos principais do pacote streamlit

# Importação dos pacotes necessários para esta tarefa
import streamlit as st # Responsável pela criação de páginas na web
import pandas as pd # Leitura de dados e construção de tabelas
import numpy as np # Possibilita diferentes operações e métodos matemáticos
import time # Controla o tempo de pausa do código

st.title("Curso de Ciência de Dados - EBAC ")
st.title("Tarefa do Módulo 15")

st.title("*4. Layout*")

"""
O Layout de uma página é a organização dos respectivos widgets nela presentes.
Aqui podem ser vistos alguns casos básicos disso.
"""

"""
No primeiro caso, temos a utilização de uma barra lateral, que pode ser acessada 
pela seta no canto superior esquerdo desta interface. Ao clicar na seta, aparecerá
uma barra com os nomes das páginas desta tarefa. Além de uma caixa de seleção como 
exemplo. 
"""
st.markdown(":point_left:")

# Uso da barra lateral

# Insere uma barra de seleção à barra lateral:
add_selectbox = st.sidebar.selectbox(
    'Como você quer que entremos em contato?',
    ('Email', 'Telefone Residencial', 'Celular')
)


"""
Outro item que pode ser adicionado à barra lateral é o slider. No caso, temos um
que é limitado entre 0 e 100, com valores pré-definidos como 25.0 e 75.0. Veja 
ao lado.
"""
st.markdown(":point_left:")

# Adiciona um slider à barra lateral:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)


"""
Cada página desenvolvida pelo streamlit pode ser dividida em colunas. No 
exemplo abaixo, a página foi divida em duas colunas, tendo um botão do lado
esquerdo e uma seleção de itens no lado direito. O último exemplo é 
inspirado em Harry Potter, onde o usuário escolhe sua casa de Hogwarts.
"""

# Divisão da página em duas colunas
left_column, right_column = st.columns(2)

# You can use a column just like st.sidebar:
left_column.button('Me aperte!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
  chosen = st.radio(
        'Chapéu Seletor',
        ("Grifinória", "Corvinal", "Lufa-Lufa", "Sonserina"))
  st.write(f"Você está na casa de  {chosen}!")



"""
É possível inserir barras de progresso na página desenvolvida. A barra pode 
ser usada para vários fins, seja para mostrar o carregamento da página ou 
o progresso do upload de arquivos. No exemplo abaixo, temos uma barra que 
de 0 a 100, tendo um tempo de espera de 0.1 s em cada valor.
"""
# Inserção de barra de progresso
'Iniciando uma longa computação...'

# Adiciona uma barra de progresso
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteração {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...e terminamos!'



"""
O nome da página pode ser colocado em evidência, seja na própria página ou 
na barra lateral.
"""

# Marcação do nome da página na barra lateral
st.sidebar.markdown("# Layout")

# Marcação do nome da página na própria página
st.markdown("# Layout")