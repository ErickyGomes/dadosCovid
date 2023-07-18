import pandas as pd
import plotly.express as px
import streamlit as st

# Lendo arquivo CSV importado do GITHUB
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

# Alterando os nomes das colunas do arquivo importado
df = df.rename(columns={
    'newDeaths': 'Novos óbitos',
    'newCases': 'Novos casos',
    'deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes',
    'totalCases_per_100k_inhabitants': 'Casos por 100 mil habitantes'
})

# Seleção do estado
# state = 'MS'
estados = list(df['state'].unique())
state = st.sidebar.selectbox('Qual estado?', estados)


# Seleção da coluna
# column = 'Casos por 100 mil habitantes'
colunas = ['Novos óbitos', 'Novos casos', 'Óbitos por 100 mil habitantes', 'Casos por 100 mil habitantes']
column = st.sidebar.selectbox('Qual tipo de informação?', colunas)

# Seleção das linhas que pertencem ao estado
df = df[df['state'] == state]

fig = px.line(df, x='date', y=column, title=column + ' - ' + state)
fig.update_layout(xaxis_title='Data', yaxis_title=column.upper(), title={'x': 0.5})

st.title('DADOS COVID - BRASIL')
st.subheader('Nessa Aplicação o usuario tem a opção de escolher o estado e o tipo de informação para mostrar o '
             'grafico. Utilize o menu lateral para alterar o filtro')


# mostrar grafico
# fig.show()
st.plotly_chart(fig, use_container_width=True)

st.caption('Os dados foram obtidos a partir do site: '
           'https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')
