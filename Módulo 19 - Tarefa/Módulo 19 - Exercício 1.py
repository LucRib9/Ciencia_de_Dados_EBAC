# Curso de Ciência de Dados - EBAC
# Módulo 19: Streamlit II - Atividade 1

# Pacotes necessários para esta atividade:
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import streamlit as st
from PIL import Image

# Função para seleção de ítens da coluna de uma tabela
def selecao_filtros(tabela, coluna, selecionados):
    '''
    Recebe uma tabela, uma coluna específica da tabela e 
    uma lista 'selecionados' com os ítens escolhidos da 
    coluna. 
    Caso o ítem 'Todos' esteja na lista 'selecionados', é 
    devolvida toda a tabela original. Caso contrário, são 
    devolvidos os ítens escolhidos e estes são removidos 
    da tabela.
    '''
    if 'Todos' in selecionados:
        return tabela
    else:
        return tabela[tabela[coluna].isin(selecionados)].reset_index(drop=True)

# Configurações para os gráficos do seaborn, removendo os traços superior
# e lateral direto de cada gráfico
parametros = {"axes.spines.right": False, "axes.spines.top": False}
sns.set_theme(style="ticks", rc=parametros)

# Função principal, onde estão as configurações do site,
# sendo ativada assim que o código é rodado
def main():
    
    #Configurações da página (ícones, título da guia, layout e barra lateral)
    st.set_page_config(page_title = 'Análise de Telemarketing',
                       page_icon = './imagens/icone_telemarketing.png',
                       layout="centered",
                       initial_sidebar_state='expanded')
    
    # Cabeçalho da atividade
    st.write('# Ciência de Dados - EBAC')
    st.write('# Módulo 19 - Streamlit II - Tarefa 1')
    st.write("---")

    # Título da página 
    st.write('# Análise de Telemarketing')
    st.write("---")
    
    # Imagem para a barra lateral da página 
    imagem_lateral = Image.open('./imagens/bank-thematic-interior.jpg')
    st.sidebar.image(imagem_lateral)

    # Leitura dos dados da tabela 'bank'
    bank_original = pd.read_csv('./dados/input/bank-additional-full.csv', sep=';')

    # Cópia da tabela 'bank' para seleção de filtros
    bank = bank_original.copy()

    # Mostra as 5 primeiras linhas da tabela 'bank_original'
    st.write('## Dados originais')
    st.write(bank_original.head())

    # Seleção dos filtros de cada coluna da tabela 'bank' pela barra lateral
    with st.sidebar.form(key='my_form'):

        # Slider com os filtros de idade
        idade_max = int(bank.age.max())
        idade_min = int(bank.age.min())
        idades = st.slider(label='Intervalo de idades',
                           min_value=idade_min,
                           max_value=idade_max,
                           value=(idade_min, idade_max),
                           step=1)
        
        # Filtro seleção de profissões
        lista_profisoes = bank.job.unique().tolist()
        lista_profisoes.append('Todos')
        profisoes_escolhidas =  st.multiselect("Profissão", lista_profisoes, ['Todos'])

        # Filtro seleção de estado civil
        lista_matrimonio = bank.marital.unique().tolist()
        lista_matrimonio.append('Todos')
        matrimonio_escolhido =  st.multiselect("Estado civil", lista_matrimonio, ['Todos'])

        # Filtro seleção Default
        lista_default = bank.default.unique().tolist()
        lista_default.append('Todos')
        default_escolhido =  st.multiselect("Default", lista_default, ['Todos'])

        
        # Filtro seleção Financiamento Imobiliário
        lista_financiamento = bank.housing.unique().tolist()
        lista_financiamento.append('Todos')
        financiamento_escolhido =  st.multiselect("Tem financiamento imobiliário?", lista_financiamento, ['Todos'])

        
        # Filtro seleção Empréstimo?
        lista_emprestimo = bank.loan.unique().tolist()
        lista_emprestimo.append('Todos')
        emprestimo_escolhido =  st.multiselect("Tem empréstimo?", lista_emprestimo, ['Todos'])

        
        # Filtro seleção Meio De Contato?
        lista_contato = bank.contact.unique().tolist()
        lista_contato.append('Todos')
        contato_escolhido =  st.multiselect("Meio de contato", lista_contato, ['Todos'])

        
        # Filtro seleção Mês Do Contato
        lista_mes = bank.month.unique().tolist()
        lista_mes.append('Todos')
        mes_escolhido =  st.multiselect("Mês do contato", lista_mes, ['Todos'])

        
        # Filtro seleção Dia Da Semana
        lista_dia_semana = bank.day_of_week.unique().tolist()
        lista_dia_semana.append('Todos')
        dia_semana_escolhido =  st.multiselect("Dia da semana", lista_dia_semana, ['Todos'])


        # Seleção das linhas na tabela 'bank' de acordo com os filtros selecionados
        bank = (bank.query("age >= @idades[0] and age <= @idades[1]")
                    .pipe(selecao_filtros, 'job', profisoes_escolhidas)
                    .pipe(selecao_filtros, 'marital', matrimonio_escolhido)
                    .pipe(selecao_filtros, 'default', default_escolhido)
                    .pipe(selecao_filtros, 'housing', financiamento_escolhido)
                    .pipe(selecao_filtros, 'loan', emprestimo_escolhido)
                    .pipe(selecao_filtros, 'contact', contato_escolhido)
                    .pipe(selecao_filtros, 'month', mes_escolhido)
                    .pipe(selecao_filtros, 'day_of_week', dia_semana_escolhido)
        )

        # Botão para mostrar a tabela resultante na página
        botao_aplicar = st.form_submit_button(label='Aplicar')
    
    # Mostra as 5 primeiras da tabela de acordo com os filtros
    st.write('## Dados Filtrados')
    st.write(bank.head())
    st.write('---')

    # Gráficos
    # Nesta seção encontam-se os comandos para a criação de dois gráficos
    # No primeiro, está a proporção de aceitação e recusa na tabela original
    # No segundo, a proporção é de acordo com a filtragem.

    # Cria uma figura onde são inseridos os dois gráficos     
    fig, ax = plt.subplots(1, 2, figsize = (5,3))

    # Toma a porcentagem de aceitação e recusa nos dados originais
    percentual_bank_original = bank_original.y.value_counts(normalize = True).to_frame()*100

    # Separa a contagem de aceitação e recusa dos dados originais
    percentual_bank_original = percentual_bank_original.sort_index()

    # Faz o gráfico de barras das proporções dos dados originais
    sns.barplot(x = percentual_bank_original.index, 
                y = 'y',
                data = percentual_bank_original, 
                ax = ax[0])
    ax[0].bar_label(ax[0].containers[0])
    ax[0].set_title('Dados brutos',
                    fontweight ="bold")
    

    # Tenta criar o gráfico com os dados filtrados, retornando uma mensagem de erro caso
    # a seleção esteja fora do banco de dados
    try:

        # Toma a porcentagem de aceitação e recusa nos dados filtrados
        percentual_bank_filtrado = bank.y.value_counts(normalize = True).to_frame()*100

        # Separa a contagem de aceitação e recusa dos dados filtrados
        percentual_bank_filtrado = percentual_bank_filtrado.sort_index()

        # Faz o gráfico de barras das proporções dos dados filtrados
        sns.barplot(x = percentual_bank_filtrado.index, 
                    y = 'y', 
                    data = percentual_bank_filtrado, 
                    ax = ax[1])
        ax[1].bar_label(ax[1].containers[0])
        ax[1].set_title('Dados filtrados',
                        fontweight ="bold")
    except:
        st.error('Erro no filtro')
    
    # Título dos gráficos
    st.write('## Proporção de aceite')

    # Mostra os gráficos
    st.pyplot(plt)

if __name__ == '__main__':
    main()