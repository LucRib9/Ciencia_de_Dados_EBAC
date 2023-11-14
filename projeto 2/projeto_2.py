import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

sns.set(context='talk', style='ticks')

st.set_page_config(
     page_title="Previsão de Renda",
     page_icon=":heavy_dollar_sign:",
     layout="wide",
)

st.title("Projeto 2 - Previsão de Renda")

st.text("""Este projeto consiste em tentar prever a renda dos clientes de uma instituição  
financeira a partir de informações básicas deles. As respectivas informações são
sexo, posse de veículo e de imóvel, número de filhos, idade, tempo de emprego, 
número de pessoas na residência, tipo de renda, educação, estado civil e tipo de 
residência. 
Neste streamlit, encontram-se as análises univariadas e bivariadas e de estabilidade
temporal de tais variáveis, tendo sido tomadas entre Janeiro de 2015 e Março de 2016,
tendo como variável resposta, a renda do cliente.
A previsão de renda em si, a partir de Machine Learning, encontra-se no arquivo 
projeto-2.ipynb.""")

st.write('# Análise exploratória da previsão de renda')

renda = pd.read_csv('./input/previsao_de_renda.csv')

#plots
st.write('## Gráficos univariada')
st.write('#### Variáveis Quantitativas')
st.text("""Começando com a variável resposta 'renda', que por ser uma variável contínua, sua 
análise será através de um histograma e boxplot.""")

# Univariada renda
st.write('#### renda')
fig, ax = plt.subplots(1,2,figsize=(20,10))
sns.histplot(x='renda', data=renda, ax=ax[0])
sns.boxplot(y='renda', data=renda, ax=ax[1])
st.pyplot(plt)
st.write(renda['renda'].describe())
st.text("""De acordo com a descrição, a renda média dos clientes é de, aproximadamente, 5697(8267) reais,
com a mediana em torno de 3500 reais. Considerando que a distância interquartil dessa variável
 é a diferença entre os valores de 75% (terceiro quartil) e 25% (primeiro quartil), ela é:
6392.1675 - 2026.1100 = 4366.0575. Os possíveis outliers são aqueles que têm valores maiores do 
que o limite superior, sendo este calculado pela soma do terceiro quartil com 1,5 vezes a diferença 
interquartil, ou seja 6392.1675 + 1.5 x 4366.0575 = 12941.2537. Desta forma, os valores de renda 
acima de 12941.25 são possíveis outliers.""")

# Univariada tempo_emprego
st.write('#### tempo_emprego')
fig, ax = plt.subplots(1,2,figsize=(20,10))
sns.histplot(x='tempo_emprego', data=renda, ax = ax[0])
sns.boxplot(y='tempo_emprego', data=renda, ax = ax[1])
st.pyplot(plt)
st.write(renda['tempo_emprego'].describe())
st.text("""A média do tempo de emprego das pessoas em questão é próximo de 7(6) anos. Além disso, 
verifica-se que a maior parte das pessoas tem tempo de emprego entre 3 e 10 anos. Há
possíveis outliers acima dos 20 anos de emprego.""")

# Univariada idade
st.write('#### idade')
fig, ax = plt.subplots(1,2,figsize=(15,10))
sns.histplot(x='idade', data=renda, ax = ax[0])
sns.boxplot(y='idade', data=renda, ax = ax[1])
st.pyplot(plt)
st.write(renda['idade'].describe())
st.text("""A média das idades dos clientes é de 43(11) anos. É notável que a maior parte deles estão
entre 34 e 53 anos.""")

# Univariada qtd_filhos
st.write('#### qtd_filhos')
fig, ax = plt.subplots(1,1,figsize=(9,6))
sns.countplot(x='qtd_filhos', data=renda)
st.pyplot(plt)
st.text("""A maior parte das pessoas analisadas não têm filhos.""")

# Univariada qt_pessoas_residencia
st.write('#### qt_pessoas_residencia')
fig, ax = plt.subplots(1,1,figsize=(9,6))
sns.countplot(x='qt_pessoas_residencia', data=renda)
st.pyplot(plt)
st.text("""Em geral, os frequentadores deste banco moram em conjunto com mais uma pessoa. Por outro,
a quantidade de pessoas que moram sozinhas é muito semelhante à das que moram com mais 
duas pessoas.""")

st.write('#### Variáveis Qualitativas')

# sexo 
st.write('#### sexo')
fig, ax = plt.subplots(1,1,figsize=(9,6))
sns.countplot(x='sexo', data=renda)
st.pyplot(plt)
st.text("""Verifica-se uma predominância de clientes do sexo feminino.""")

# posse_de_veiculo
st.write('#### posse_de_veiculo')
fig, ax = plt.subplots(1,1,figsize=(9,6))
sns.countplot(x='posse_de_veiculo', data=renda)
st.pyplot(plt)
st.text("""A maior parte dos clientes não possuem veículo.""")

# posse_de_imovel
st.write('#### posse_de_imovel')
fig, ax = plt.subplots(1,1,figsize=(9,6))
sns.countplot(x='posse_de_imovel', data=renda)
st.pyplot(plt)
st.text("""Por outro lado, a quantidade de pessoas que  possuem imóvel é quase o dobro das que 
não possuem.""")

# tipo_renda
st.write('#### tipo_renda')
fig, ax = plt.subplots(1,1,figsize=(9,6))
tipos = sns.countplot(x='tipo_renda', data=renda)
tipos.tick_params(axis='x', rotation=45)
st.pyplot(plt)
st.text("""O tipo de renda predominante é a de trabalhadores assalariados. Enquanto que quase 
não há bolsistas no conjunto analisado.""")

# educacao
st.write('#### educacao')
fig, ax = plt.subplots(1,1,figsize=(9,6))
educ = sns.countplot(x='educacao', data=renda)
educ.tick_params(axis='x', rotation=45)
st.pyplot(plt)
st.text("""Verifica-se que a maior parte das pessoas possui a educação no nível secundário, 
seguido pelos que possuem terminaram o nível superior. """)

# estado_civil
st.write('#### estado_civil')
fig, ax = plt.subplots(1,1,figsize=(9,6))
sns.countplot(x='estado_civil', data=renda)
st.pyplot(plt)
st.text("""A maior parte dos cliente são casados, enquanto entre os estados civis restantes, 
percebe-se um leve predomínio dos solteiros.""")

# tipo_residencia
st.write('#### tipo_residencia')
fig, ax = plt.subplots(1,1,figsize=(9,6))
resid = sns.countplot(x='tipo_residencia', data=renda)
resid.tick_params(axis='x', rotation=45)
st.pyplot(plt)
st.text("""Há um claro predomínio de residências do tipo casa, de forma que quase não são 
notadas diferenças entre as quantidades dos outros tipos.""")

st.write('## Gráficos bivariada')

st.text("""Nesta seção serão realizadas as análises bivariadas da variável resposta 'renda'
em função das variáveis explicativas. No caso das variaveis quantitativas, serão 
verificadas as correlações entre elas e a variável resposta 'renda'. Para as 
variáveis qualitativas, veremos tanto a estabilidade temporal de cada variável, 
quanto a da média da variável 'renda' de acordo com as explicativas.""")

st.write('#### Variáveis Quantitativas')
st.text("""Começando pelas variáveis quantitativas, vejamos as Matrizes de Dispersão e Correlação 
delas, além do Clustermap:""")

# separando as variáveis quantitativas
quantitativas = renda[['qtd_filhos', 'idade', 'tempo_emprego',
              'qt_pessoas_residencia', 'renda']]

st.write("#### Matriz de Dispersão")
sns.pairplot(quantitativas)
sns.despine()
st.pyplot(plt)
st.text("""A Análise da matriz de dispersão, retorna os seguintes insights:
- As pessoas com maiores rendas tendem a ter menor quantidade de filhos, sendo maior
nos casos em que o cliente ou não tem filhos ou tem dois;
- Há uma maior concentração de renda nas pessoas que vivem com mais uma única na residência;
- Nos casos das variáveis 'idade' e 'tempo_emprego', a renda está, em geral, dispersa entre
0 e 50000, não tendo como afirmar diretamente a influência delas.""")

st.write("#### Clustermap")
cmap = sns.diverging_palette(h_neg=850, h_pos=350, as_cmap=True)
cluster = sns.clustermap(quantitativas.corr(), figsize=(10, 10), center = 0, cmap=cmap)
plt.setp(cluster.ax_heatmap.get_yticklabels(), rotation=0)
sns.despine()
st.pyplot(plt)
st.text("""A observação do clustermap mostra que a variável quantitativa mais correlacionada à 
'renda' é a 'tempo_emprego', cuja correlação está entre 0.25 e 0.50.
As três variáveis restantes estão muito próximas de zero. """)

st.write("#### Matriz de Correlação ")
st.write(quantitativas.corr())
st.text("""Tal como foi visto no clustermap, a variável quantitativa com maior correlação com 
a variável resposta 'renda' é a 'tempo_emprego', visto que sua correlação é de 0.38. 
Nas variáveis restantes ('qtd_filhos', 'idade' e 'qt_pessoas_residencia'), a 
correlação varia entre 0.02 e 0.04, sendo elas extremamente baixas para afirmar 
que são influenciaveis à renda da pessoa.""")

st.write("#### Gráfico de Dispersão")
st.text("""Dado que a maior correlação está entre a 'renda' e o 'tempo_emprego', vejamos de 
forma mais aprofundada o gráfico de dispersão de tais variáveis, com a reta de tendência
nele presente.""")
fig, ax = plt.subplots(1,1,figsize=(9,6))
sns.regplot(x='tempo_emprego', y='renda', data = renda)
st.pyplot(plt)
st.text("""É possível notar um leve crescimento na reta de tedência de acordo com o aumento 
do tempo de emprego da pessoa, confirmando com a correlação positiva entre elas.""")

st.write('#### Variáveis Qualitativas')
st.text("""Para as variáveis qualitativas, antes das análises da estabilidade temporal,
verifiquemos a relação entre as variáveis booleanas ('posse_de_veiculo' e 
'posse_de_imovel') com a renda.""")

# Bivariadas - posse_de_veiculo e posse_de_imovel
st.write("#### Bivariadas - renda x posse_de_veiculo e posse_de_imovel ")
fig, axes = plt.subplots(1,2,figsize=(15,6))
sns.pointplot(x="posse_de_imovel", y="renda",
              data=renda, dodge=True, ci=95,
               ax = axes[0], color='red')
sns.pointplot(x="posse_de_veiculo", y="renda",
              data=renda, dodge=True, ci=95,
              ax = axes[1], color='green')
st.pyplot(plt)
st.text("""Analisando os dois gráficos, nota-se:
- Não uma diferença significativa entre a renda das pessoas que possuem imóvel em relação 
às que não possuem;
- A renda das pessoas que possuem veículo tende a ser maior em relação àquelas que não 
possuem. Considerando o intervalo de confiança, a diferença é de maior do que
1000 reais.
Dessa forma, a 'posse_de_veiculo' tende a ser uma variável preditora de renda.""")

st.write('## Gráficos temporais')
st.text("""Agora, verifiquemos a estabilidade temporal da média da renda de acordo com cada
variável qualitativa, além da própria variável explicativa.""")

st.write("#### sexo")
fig, axes = plt.subplots(1,2,figsize=(18,9))
ax0 = axes[0]
estab_sex = sns.countplot(x='data_ref', hue='sexo', data=renda, ax=ax0)
estab_sex.tick_params(axis='x', rotation=90)
estab_sex.legend(loc = 'lower center', bbox_to_anchor=(0.5, -.35),ncol = 3)
ax1 = axes[1]
renda_sex = sns.pointplot(x='data_ref', hue='sexo', y='renda', data=renda, ax=ax1)
renda_sex.tick_params(axis='x', rotation=90)
renda_sex.legend(loc = 'lower center', bbox_to_anchor=(0.5, -.35), ncol = 3)
st.pyplot(plt)
st.text("""As quantidades de clientes de cada sexo não se alteraram de forma significativa 
durante o período em análise, tendo sempre um maior número de mulheres (praticamente o 
dobro em relação à quantidade de homens). Por outro lado, a renda dos homens foi maior 
do que a das mulheres, enquanto que a renda feminina ficou em torno de 4000 reais 
durante o período, a renda masculina variou entre 8000 e 100000 reais (maior do que o 
dobro da renda feminina).""")

st.write("#### posse_de_imovel")
fig, axes = plt.subplots(1,2,figsize=(18,9))
ax0 = axes[0]
estab_sex = sns.countplot(x='data_ref', hue='posse_de_imovel', data=renda, ax=ax0)
estab_sex.tick_params(axis='x', rotation=90)
estab_sex.legend(loc = 'lower center', bbox_to_anchor=(0.5, -.35),ncol = 3)
ax1 = axes[1]
renda_sex = sns.pointplot(x='data_ref', hue='posse_de_imovel', y='renda', data=renda, ax=ax1)
renda_sex.tick_params(axis='x', rotation=90)
renda_sex.legend(loc = 'lower center', bbox_to_anchor=(0.5, -.35), ncol = 3)
st.pyplot(plt)
st.text("""Não houveram variações significativas nos números de clientes que têm ou não imóveis, 
com a maior parte deles possuindo imóvel. Também não foram notadas diferenças entre as 
rendas em relação a esta variável qualitativa.""")

st.write("#### posse_de_veiculo")
fig, axes = plt.subplots(1,2,figsize=(18,9))
ax0 = axes[0]
estab_sex = sns.countplot(x='data_ref', hue='posse_de_veiculo', data=renda, ax=ax0)
estab_sex.tick_params(axis='x', rotation=90)
estab_sex.legend(loc = 'lower center', bbox_to_anchor=(0.5, -.35),ncol = 3)
ax1 = axes[1]
renda_sex = sns.pointplot(x='data_ref', hue='posse_de_veiculo', y='renda', data=renda, ax=ax1)
renda_sex.tick_params(axis='x', rotation=90)
renda_sex.legend(loc = 'lower center', bbox_to_anchor=(0.5, -.35), ncol = 3)
st.pyplot(plt)
st.text("""A maior parte dos clientes analisados durante o intervalo de tempo não possui veículo. 
Além disso, a renda daqueles que possuem veículo foi maior do que os que não possem, 
havendo uma breve semelhança entre elas nos meses de Janeiro, Maio, Junho e Agosto 
de 2015 e Março de 2016.""")

st.write("#### tipo_renda")
fig, axes = plt.subplots(1,2,figsize=(18,9))
ax0 = axes[0]
estab_sex = sns.countplot(x='data_ref', hue='tipo_renda', data=renda, ax=ax0)
estab_sex.tick_params(axis='x', rotation=90)
estab_sex.legend(loc = 'lower center', bbox_to_anchor=(0.5, -.4),ncol = 3)
ax1 = axes[1]
renda_sex = sns.pointplot(x='data_ref', hue='tipo_renda', y='renda', data=renda, ax=ax1)
renda_sex.tick_params(axis='x', rotation=90)
renda_sex.legend(loc = 'lower center', bbox_to_anchor=(0.5, -.4), ncol = 3)
st.pyplot(plt)
st.text("""Não foram notadas variações nas quantidades dos tipos de renda durante todo o intervalo,
com maior quantidade dos clientes sendo assalariados, seguidos por empresários e pensionistas.
Os que apresentaram menor renda durante todo o período foram os pensionistas, com uma média
em torno de 4000 reais. Por outro lado os servidores públicos apresentaram as maiores rendas
durante o período, variando entre 6000 e 10000 reais. Os empresários e assalariados tiveram
rendas semelhantes, sendo em torno de 6000 reais. No caso dos bolsistas, a quantidade de 
clientes deste tipo foi muito pequena durante todo o tempo, além de apresentarem variações
bruscas em suas rendas, indo de, aproximadamente, 4000 a 8000 reais.""")

st.write("#### educacao")
fig, axes = plt.subplots(1,2,figsize=(20,9))
ax0 = axes[0]
estab_sex = sns.countplot(x='data_ref', hue='educacao', data=renda, ax=ax0)
estab_sex.tick_params(axis='x', rotation=90)
estab_sex.legend(loc = 'lower center', bbox_to_anchor=(0.5, -.4),ncol = 3)
ax1 = axes[1]
renda_sex = sns.pointplot(x='data_ref', hue='educacao', y='renda', data=renda, ax=ax1)
renda_sex.tick_params(axis='x', rotation=90)
renda_sex.legend(loc = 'lower center', bbox_to_anchor=(0.5, -.4), ncol = 3)
st.pyplot(plt)
st.text("""O níveis de educação predominantes dos dos clientes foram secundário e superior completo, 
com o nível secundário sendo o mais comum entre janeiro e agosto de 2015 (variando entre 
650 a 700 pessoas, enquanto que o nível superior completou ficou entre 250 e 300 pessoas).
A partir de setembro, passou a haver uma proximidade entre as quantidades de clientes com
nível secundário e superior completo, possivelmente, parte dos que apresentavam apenas o
secundário terminaram o nível superior neste período. 
Em relação à renda, nota-se que aquelas dos níveis secundário e superior completo foram 
semelhantes no tempo de análise, sendo ambas próximas a 6000 reais. Os níveis restantes 
tiveram grandes variações na renda média, com destaque à Pós graduação, indo de 2000 a 
12000 reais.""")

st.write("#### tipo_residencia")
fig, axes = plt.subplots(1,2,figsize=(18,9))
ax0 = axes[0]
estab_sex = sns.countplot(x='data_ref', hue='tipo_residencia', data=renda, ax=ax0)
estab_sex.tick_params(axis='x', rotation=90)
estab_sex.legend(loc = 'lower center', bbox_to_anchor=(0.5, -.4),ncol = 3)
ax1 = axes[1]
renda_sex = sns.pointplot(x='data_ref', hue='tipo_residencia', y='renda', data=renda, ax=ax1)
renda_sex.tick_params(axis='x', rotation=90)
renda_sex.legend(loc = 'lower center', bbox_to_anchor=(0.5, -.4), ncol = 3)
st.pyplot(plt)
st.text("""Não foram notadas mudanças nas distribuições dos tipos de residência, com a maior quantidade
de pessoas morando em casa (aproximadamente 90% dos clientes) durante o tempo de análise. As
pessoas que apresentaram maiores rendas foram os que vivem em estúdio durante a maior parte
do tempo, ainda assim, tais rendas variaram entre abaixo de 5000 a acima de 15000 reais. 
Também foram notadas alterações significativas nas pessoas que vivem de aluguel e aquelas que 
vivem em residência governamental, principalmente setembro e dezembro de 2015. Os tipos de 
residência restantes (com os pais, casa e comunitário) tiveram rendas mais estáveis durante 
este tempo, sendo próximas a 5000 reais.""")

st.write("#### estado_civil")
fig, axes = plt.subplots(1,2,figsize=(18,9))
ax0 = axes[0]
estab_sex = sns.countplot(x='data_ref', hue='estado_civil', data=renda, ax=ax0)
estab_sex.tick_params(axis='x', rotation=90)
estab_sex.legend(loc = 'lower center', bbox_to_anchor=(0.5, -.4),ncol = 3)
ax1 = axes[1]
renda_sex = sns.pointplot(x='data_ref', hue='estado_civil', y='renda', data=renda, ax=ax1)
renda_sex.tick_params(axis='x', rotation=90)
renda_sex.legend(loc = 'lower center', bbox_to_anchor=(0.5, -.4), ncol = 3)
st.pyplot(plt)
st.text("""Nota-se que durante o tempo de análise, a maior parte das pessoas são casadas (aproximadamente 
70% delas) e que não houveram mudanças significativas nas distribuições dos estados civis dos
clientes. Além disso, não foram notadas diferenças significativas nas rendas de cada estado 
civil, com excessão do detalhe de que as pessoas viúvas foram as que tiveram menores rendas 
durante o ano de 2015.""")
