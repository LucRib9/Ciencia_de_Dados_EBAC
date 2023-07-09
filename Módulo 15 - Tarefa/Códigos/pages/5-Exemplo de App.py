# Ciência de Dados -  Exercício - Módulo 15 
# Conceitos principais do pacote streamlit

# Importação dos pacotes necessários para esta tarefa
import streamlit as st # Responsável pela criação de páginas na web
import pandas as pd # Leitura de dados e construção de tabelas
import numpy as np # Possibilita diferentes operações e métodos matemáticos

st.title("Curso de Ciência de Dados - EBAC ")
st.title("Tarefa do Módulo 15")

st.title("*5. Exemplo de App*")
st.markdown("# Viagens de Uber em NY")

st.text('''Esta página utiliza o exemplo de app desenvolvido na documentação do streamlit.
Nela são desenvolvidos histograma, informações em um mapa, além de widgets 
interativos.
Os dados utilizados são públicos, sobre a cidade de New York, demonstrando as varia-
ções no número e localizações de viagens diárias, de acordo com o horário. 
Os dados podem ser acessados no seguinte link:''')
st.markdown('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# Importação dos dados necessários:
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


# Tendo a url com os dados necessários, é possível fazer a leitura deles através do pandas.
# Seguindo o exemplo do streamlit, vamos criar uma função que faz a leitura do arquivo 
# csv presente na url fornecida. Nessa função deve ser informado o número de linhas do 
# arquivo que serão lidas. Após a leitura, a função converte o título de cada coluna 
# para letra minúscula e cria uma coluna com o horário e data das informações presentes 
# em cada linha. Por fim, ela retorna a tabela final ao usuário. Para deixar o código mais 
# ágil, vamos armazernar esta função em cache.
@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Aplicando a função criada à URL dos dados:
# Frase que aparece ao usuário informando o carregamento dos dados.
data_load_state = st.text('Carregando dados...')
# Carregando as 10000 primeiras linhas dos dados a partir da função criada.
data = load_data(10000)
# Notificando o usuário que o carregamento dos dados foi terminado, através
# do cache
data_load_state.text("Pronto! (usando st.cache_data)")

# Caso o usuário queira ver os dados carregados, vamos criar um checkbox que 
# ao ser pressionado permite a respectiva visualização.
if st.checkbox('Mostrar dados raw'):
    st.subheader('Dados Raw')
    st.write(data)

# Com os dados carregados, vamos criar um histograma que mostra o número de 
# viagens por hora.
st.subheader('Número de viagens por hora')

hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

# Também pode ser feito um mapa com os locais de viagem em todas as horas 
# do dia: 
#st.subheader('Mapa com todas as viagens')
#st.map(data)

# Para uma melhor visualização do número de viagens, vamos inserir um slider
# que define o horário de referência de moviemntação no mapa. O slider tem o 
# intervalo entre 0h e 23h, tendo por padrão as 17h.
hour_to_filter = st.slider('hora', 0, 23, 17)  
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Mapa de todas as viagens às {hour_to_filter}:00')
st.map(filtered_data)