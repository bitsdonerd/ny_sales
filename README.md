# ny_sales

### 1. Introdução
Este projeto é uma ferramenta de análise de vendas de imóveis em Nova York, construída em Python. Ele fornece uma visão interativa e detalhada do mercado imobiliário, visualizando as vendas por localidade e exibindo análises através de um dashboard. O software permite que o usuário explore dados de vendas de propriedades até 2022, facilitando decisões baseadas em dados.

### 2. Objetivo do Projeto
O objetivo deste projeto é oferecer uma plataforma para análise visual de vendas de imóveis, permitindo que os usuários examinem tendências e padrões no mercado imobiliário. As funcionalidades principais incluem:

Visualização interativa das vendas no mapa utilizando Mapbox.
Dashboards com gráficos dinâmicos usando Plotly.

### 3. Tecnologias Utilizadas
Python: Linguagem principal para manipulação de dados e integração com bibliotecas.
Mapbox: Plataforma para visualização de mapas e dados geoespaciais.
Plotly: Ferramenta para criar gráficos interativos e dashboards.
Bibliotecas de Data Science (Pandas, NumPy): Manipulação e análise de dados.
Dataset: Conjunto de dados de vendas de imóveis até 2022.

### 4. Instalação e Configuração
Passo a passo para instalação e configuração do ambiente:

Pré-requisitos: Python 3.7+, e pacotes necessários (pandas, plotly, mapbox, numpy).
Instalação dos Pacotes: Instale os pacotes com pip install pandas plotly mapbox numpy.
bash
Copiar código
pip install pandas plotly mapbox numpy
Configuração do Mapbox:
Crie uma conta no Mapbox e obtenha uma chave de API.
Defina a chave de API no código para permitir a visualização do mapa.

### 5. Funcionalidades
Importação e Manipulação de Dados: Carrega e limpa o dataset de vendas de imóveis para análise.
Visualização Interativa no Mapa: Exibe as vendas de imóveis por localização usando o Mapbox.
Dashboard Dinâmico: Utiliza o Plotly para criar gráficos interativos que apresentam as vendas por tipo de propriedade, ano, faixa de preço.

### 6. Como Usar o Software
Carregamento de Dados: Execute o script para carregar o dataset e preparar os dados.
Exibição no Mapa: Visualize o mapa interativo com vendas de imóveis em diferentes regiões.
Exploração do Dashboard: Navegue pelos gráficos para entender as tendências de vendas.

### 7. Como Clonar e Executar o Projeto Localmente
Para exibir o dashboard na máquina localmente:

Passo 1: Clonar o Repositório
Abra o terminal ou prompt de comando.

Execute o comando para clonar o repositório:

git clone https://github.com/bitsdonerd/ny_sales
Entre na pasta do projeto: cd nome-do-repositorio

Passo 2: Criar e Ativar um Ambiente Virtual
No diretório do projeto, crie um ambiente virtual para isolar as dependências do projeto:
python3 -m venv venv

Ative o ambiente virtual:
No Windows: venv\Scripts\activate
No macOS/Linux: source venv/bin/activate

Passo 3: Instalar Dependências
Com o ambiente virtual ativo, instale as dependências necessárias usando o requirements.txt do projeto:

pip install -r requirements.txt

Passo 4: Configurar a Chave de API do Mapbox
Crie uma conta no Mapbox.

Obtenha sua chave de API no painel do Mapbox.
Insira a chave de API no código, substituindo o valor da variável mapbox_access_token:
mapbox_access_token = 'sua_chave_de_api_aqui'

Passo 5: Executar o Projeto
Execute o script principal para iniciar o mapa interativo e o dashboard:
python ny_sales.py

Passo 6: Visualizar o Mapa e o Dashboard
Após executar o script, o mapa e o dashboard estarão disponíveis. Se o projeto incluir um servidor local para visualização, as instruções para acessá-lo serão exibidas no terminal (ex.: http://localhost:5000).