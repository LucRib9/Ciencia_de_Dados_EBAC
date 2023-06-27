#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importando os pacotes necessários
# pandas é necessário para a leitura dos arquivos de dados
# com o matplotlib.pyplot é possível fazer gráficos 
import pandas as pd
import matplotlib.pyplot as plt 

# O uso do sys permite a inserção de argumentos
# Com os é possível criar diretórios no sistema
import sys
import os

''' 
Nesta tarefa é pedido para que sejam feitos gráficos com
os dados do sinasc nos meses entre março e dezembro do ano de 
2019. Cada mês deve ser inserido no programa como argumento.
Para isso, será usada a função que imprime os gráficos desenvolvida
na tarefa anterior. Os gráficos de cada mês serão salvos em pastas 
nomeadas de acordo com o mês, tendo a forma "2019-XX", com XX sendo
o número do mês.
Os Argumentos são colocados através do cmd do sistema do computador
utilizado. Isso ocorre quando um argumento é escrito ao lado do nome
do código quando ele é chamado (por exemplo: codigo.py argumento_1).
Um fator importante a ser lembrado é o de que o argumento[0] sempre 
é o nome do código utilizado.
'''

# função para a criação de gráficos
def faz_graficos(df, value, index, funcao, ylabel=None,
                       xlabel=None, ajeito=None):
    ''' Função responsável pela construção de gráficos por meio do 
    pacote pandas. Para que ela funcione, ela precisa receber os 
    seguintes parâmetros: 
    df: DataFrame com os dados para o gráfico;
    value: Coluna do DataFrame com as medições que serão colocadas
    no eixo y do gráfico;
    index: Lista com a(s) Coluna(s) do DataFrame com os dados que 
    servem de base para as medições. Se houverem mais de uma coluna,
    uma delas será para separar as medições;
    funcao: Função que será aplicada sobre os dados, podendo ser 
    contagem (count), média (mean), mediana (median), entre outras;
    ylabel: Nome do eixo y;
    xlabel: Nome do eixo x;
    ajeito: Forma de separar os dados, podendo ser "sort" que aplica 
    o sort_values ao gráfico, ou "unstack" que aplica o unstack no 
    gráfico.
    Ao receber os parâmetros, ela faz a leitura das colunas selecionadas
    no DataFrame e aplica uma função sobre elas, relacionando-as. Além 
    disso, ela ordena os resultados de acordo com o parâmetro "ajeito"
    fornecido pelo usuário. Se isso não for especificado, os resultados 
    aparecem na ordem em que encontram-se no index do DataFrame. Em rela-
    ção as nomes dos eixos dos gráficos, eles podem ser ser alterados pelos
    parâmtros "ylabel" e "xlabel"; caso contrário, são preenchidos com os 
    nomes das colunas em questão. Por fim, o gráfico é imprimido.
    A função não retorna algo. 
    '''
    if ajeito == 'sort':
        pd.pivot_table(df, values=value, index=index,
                       aggfunc=funcao).sort_values(value).plot(figsize=[15, 5])
    elif ajeito == 'unstack':
        pd.pivot_table(df, values=value, index=index,
                       aggfunc=funcao).unstack().plot(figsize=[15, 5])
    else:
        pd.pivot_table(df, values=value, index=index,
                       aggfunc=funcao).plot(figsize=[15, 5])
    
    if xlabel != None:
        plt.xlabel(xlabel)
    
    if ylabel != None:
        plt.ylabel(ylabel)
    
    return None   


# Lista com os meses inseridos
meses = sys.argv

# Número de meses (argumentos) inseridos no código 
total_meses = len(meses)

# Impressão da lista com os argumentos (meses) inseridos
print("Os meses em questão são: ", meses[1:total_meses]) 

# Número de meses em questão (desconsiderando o título do código)
print("O total de meses a serem analisados é: ", total_meses - 1)

# Leitura e impressão dos dados de cada mês
for mes in range(1, total_meses):
    sinasc = pd.read_csv('./input/SINASC_RO_2019_'+meses[mes]+'.csv')
    
    # Impressão das datas mínima e máxima do período lido
    print("A data inicial é: ", sinasc.DTNASC.min())
    print("A data final é: ", sinasc.DTNASC.max())
    
    # Nome para a pasta com os dados do mês
    mes_analisado = sinasc.DTNASC.max()[:7]
    print(mes_analisado)
    
    # Criação da pasta para os gráficos
    os.makedirs('./output/figs/'+mes_analisado, exist_ok=True)
    
    # Plot e download dos gráficos

    # Média das Idades da Mães
    faz_graficos(df=sinasc, value='IDADEMAE', index='DTNASC', funcao='mean',
                 ylabel='Média das Idades das Mães', xlabel='Data de Nascimento')
    plt.title('Média das Idades da Mães')
    plt.savefig('./output/figs/'+mes_analisado+'/media idade mae x tempo.png')

    # Quantidade de bebês nascidos ao longo do ano
    faz_graficos(df=sinasc, value='IDADEMAE', index='DTNASC', 
                 funcao='count', ylabel='Quantidade de Bebês Nascidos', 
                 xlabel='Data de Nascimento')
    plt.title('Quantidade de bebês nascidos ao longo do ano')
    plt.savefig('./output/figs/'+mes_analisado+'/quantidade de bebes nascidos.png')

    # Quantidade de bebês nascidos de acordo com o sexo
    faz_graficos(df=sinasc, value='IDADEMAE', index=['DTNASC', 'SEXO'], 
                 funcao='count', ylabel='Quantidade de Bebês Nascidos', 
                 xlabel='Data de Nascimento', ajeito='unstack')
    plt.title('Quantidade de bebês nascidos de acordo com o sexo')
    plt.savefig('./output/figs/'+mes_analisado+'/quantidade de bebes nascidos de acorco com o sexo.png')

    # Peso Médio dos bebês (especificando o sexo da criança) x Tempo
    faz_graficos(df=sinasc, value='PESO', index=['DTNASC', 'SEXO'], funcao='mean',
                 ylabel='Peso médio dos Bebês (em gramas)', 
                 xlabel='Data de Nascimento', ajeito='unstack')
    plt.title('Peso Médio dos bebês (especificando o sexo da criança) x Tempo')
    plt.savefig('./output/figs/'+mes_analisado+'/peso médio dos bebes.png')

    # Peso Mediano dos Bebês X Escolaridade da Mãe
    faz_graficos(df=sinasc, value='PESO', index='ESCMAE', funcao='median',
                 ylabel='Peso Mediano dos Bebês', xlabel='Escolaridade da Mãe',
                 ajeito='sort')
    plt.title('Peso Mediano dos Bebês X Escolaridade da Mãe')
    plt.savefig('./output/figs/'+mes_analisado+'/peso dos bebes x escolaridade da mae.png')

    # APGAR1 X Período de Gestação
    faz_graficos(df=sinasc, value='APGAR1', index='GESTACAO', funcao='mean',
                 ylabel='APGAR1 Médio', xlabel='Gestação', ajeito='sort')
    plt.title('APGAR1 X Período de Gestação')
    plt.savefig('./output/figs/'+mes_analisado+'/apgar1 x gestacao.png')

    # APGAR5 X Período de Gestação
    faz_graficos(df=sinasc, value='APGAR5', index='GESTACAO', funcao='mean',
                 ylabel='APGAR5 Médio', xlabel='Gestação', ajeito='sort')
    plt.title('APGAR5 X Período de Gestação')
    plt.savefig('./output/figs/'+mes_analisado+'/apgar5 x gestacao.png')

