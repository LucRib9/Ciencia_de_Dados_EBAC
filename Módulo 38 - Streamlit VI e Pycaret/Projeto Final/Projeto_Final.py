# Ciência de Dados - EBAC
# Projeto Final
# Aluno: Lucas Antonio de Sousa Ribeiro

# Imports
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from io import BytesIO
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer 
from sklearn.linear_model import LogisticRegression
from pycaret.classification import load_model, predict_model


# Função para ler os dados
@st.cache_data
def load_data(file_data):
    return pd.read_csv(file_data, sep=',')
    
# Função para converter o df para csv
@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

# Função principal da aplicação
def main():
    # Configuração inicial da página da aplicação
    st.set_page_config(page_title = 'Credit Scoring', \
        page_icon = 'telmarketing_icon.png',
        layout="wide",
        initial_sidebar_state='expanded'
    )

    # Título principal da aplicação
    st.write('# Projeto Final - Credit Scoring')
    st.markdown("---")
    
    # Apresenta a imagem na barra lateral da aplicação
    #image = Image.open("Bank-Branding.jpg")
    #st.sidebar.image(image)

    # Botão para carregar arquivo na aplicação
    st.sidebar.write("## Suba o arquivo")
    data_file_1 = st.sidebar.file_uploader("Credit Scoring data", type='csv')

    # Verifica se há conteúdo carregado na aplicação
    if (data_file_1 is not None):
        df = load_data(data_file_1)

        st.write('## Visualização da Base de Dados')
        st.write(df.head())

        # Separa as colunas numéricas das qualitativas do dataframe
        quantitativas = ['qtd_filhos', 'idade', 'tempo_emprego', 'qt_pessoas_residencia',
        'renda']
        qualitativas = ['sexo', 'posse_de_veiculo', 'posse_de_imovel', 'tipo_renda', 'educacao',
       'estado_civil', 'tipo_residencia']

        # Pipeline de preprocessamento dos dados
        # Pipeline que corrige as numéricas
        numericas = Pipeline(steps=[
            ('nulos', SimpleImputer(strategy='mean')),
            ('outliers', RobustScaler())
        ])

        # Pipeline que converte as categoricas em dummies
        categoricas = Pipeline(steps=[
            ('nulos', SimpleImputer(strategy='most_frequent')),
            ('dummies', OneHotEncoder(handle_unknown='ignore', drop='first'))
        ])

        # Corrige todas as variáveis 
        conversor = ColumnTransformer([
            ('num', numericas, quantitativas),
            ('cat', categoricas, qualitativas)
        ])

        # Faz todo o preprocessamento 
        preprocessamento = Pipeline(steps=[
            ('conversor', conversor),
            ('pca', PCA(n_components=5))
        ])

        # Separa a variável resposta das explicativas
        X = df.drop(columns='mau')
        y = df.mau.astype(int)

        # Ajusta as variáveis explicativas ao Pipeline
        prep_ajuste = preprocessamento.fit_transform(X)
        X_prep = pd.DataFrame(data=prep_ajuste, columns=['PC' + str(i) for i in range(1,6)])
        
        # Carrega o modelo e faz o predict
        model_saved = load_model('model_final')
        predict = model_saved.predict(X_prep)
        score = model_saved.score(X_prep, y)
        
        # Insere o predict no df e mostra os resultados
        df_pred = df.copy()
        df_pred['Predict'] = predict
        st.write('## Resultados do ajuste do modelo')
        st.write(df_pred.head())
        st.write(f'A acurácia do ajuste foi de {100*score:.1f}%.')

        # Converte o df para csv e faz o download
        df_csv = convert_df(df_pred)
        st.download_button(label='📥 Download',
                            data=df_csv,
                            file_name= 'predict.csv')

if __name__ == '__main__':
	main()