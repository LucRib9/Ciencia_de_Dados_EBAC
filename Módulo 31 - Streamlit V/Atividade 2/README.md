# RFV

Neste projeto são analisados os RFV (Recência, Frequência e Valor) das compras dos clientes de uma loja. Quanto mais alto o RFV do
cliente, maiores os bônus que ele pode ter (descontos maiores, amostras grátis de novos produtos, recomendações, etc).

## Descrição do projeto

As características dos clientes e de suas respectivas compras analisadas neste projeto são:
* ID_cliente - número de identificação da pessoa;
* CodigoCompra - Código de identicação da compra realizada;
* DiaCompra - Data em que a compra foi realizada;
* ValorTotal - Valor da compra realizada.

### Link para a aplicação (LIVE)
[https://telemarketing-ebac-wzu2.onrender.com/](https://rfv-ebac.onrender.com/)

## Utilização

### Dependencias

* O código deste projeto pode ser lido e executado em qualquer sistema operacional, desde que tenha uma editor de códigos que reconheça a linguagem python
  (tal como Visual Studio Code), um software capaz de executar o código no formato py (por exemplo o Git Bash) e um leitor de planilhas no formato csv
  (pode utilizar o libre office).
* Os pacotes necessários para rodar o código são:
- pandas==2.1.4
- scikit-learn==1.4.2
- seaborn==0.13.1
- streamlit==1.30.0
- matplotlib==3.7.5
- protobuf==4.25.2
- numpy==1.26.4
  
o que pode ser confirmado no arquivo requirements.txt.

### Instalação

* Os arquivos necessários (código e planilha) podem ser obtidos nesta pasta (Atividade 1), sendo encontrados logo acima deste arquivo README.
* Para visualizar o código e os dados utilizados, faça o download dos arquivos "app_RFV.py", "dados_input 1.csv" e "dados_test_input 2.csv".

### Executando o projeto

* Caso queira apenas visualizar o site desenvolvido neste projeto, acesse o link presente na seção "Link para a aplicação (LIVE)" logo acima.
* Por outro lado, para editar o código abra o arquivo "app_RFV.py" pelo editor presente no seu SO.
* Em relação aos dados, caso queira alterá-los, abra um dos arquivos "dados_input 1.csv" ou "dados_test_input 2.csv" pelo office do seu SO.
* Para acessar o site desenvolvido pelo código diretamente, abra o terminal do seu sistema (Git Bash, CMD do Windows ou Conda)
  e digite os seguintes comandos:
  
```
cd [NOME DA PASTA NA QUAL O CÓDIGO FOI SALVO]
python -m streamlit run app_RFV.py
```

* Ao entrar no site, é necessário carregar os dados do banco. Isto pode ser feito de duas formas:
  1. Arrastando o arquivo csv para a área "Drag and drop files here";
  2. Clicando em "Browse files" e selecione a planilha csv na pasta em que ela foi salva.  

* Com o carregamento dos dados, aparecerá na tela um conjunto de tabelas onde se encontram os dados de cada cliente, tais como "Recência" (informa há quantos dias o cliente realizou a última compra), "Frequência" (número de vezes que o cliente realizou compras com a loja) e "Valor" (gasto total de cada cliente no período analisado).
* Após estas tabelas são realizadas as classificações de cada cliente em relação aos seus comportamentos, podendo variar entre "D" (pior classificação) e "A" (melhor tipo de cliente).
* A tabela final com todos os dados e análises pode ser baixada por meio do botão "Download" no final da página.

## Ajuda

Caso restem dúvidas sobre o funcionamento do projeto, entre em contato com o autor. 

## Autores

Nomes dos desenvolvedores do projeto e informação para entrar em contato.

Lucas Ribeiro
[@LucasRibeiro](www.linkedin.com/in/lucas-data-science)

## Histórico de versões.

* 0.2
	* Ajustes de diversos bugs e otimização
* 0.1
    * Primeira versão

## Licença de uso

Esse projeto possui licença de uso - acesse o arquivo LICENSE.md para mais detalhes.

## Fontes de inspiração

Inspiração, trechos de códigos utilizados, etc.
* [readme-template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
