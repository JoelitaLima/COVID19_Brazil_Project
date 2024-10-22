#VACINAÇÂO
#Vamos processar os dados de vacinação da universidade de Oxford.

import pandas as pd

#Extração
Os dados estão compilados em um único arquivo.
vaccines = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv', sep=',', parse_dates=[3], infer_datetime_format=True)

vaccines.head()

#Vamos selecionar as colunas de interesse e as linhas referentes ao Brasil.
vaccines = vaccines.query('location == "Brazil"').reset_index(drop=True)
vaccines = vaccines[['location', 'population', 'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated', 'total_boosters', 'date']]

#Wrangling
#Vamos manipular os dados para o dashboard. O foco é em garantir uma boa granularidade e qualidade da base de dados.
#visão geral rápida e detalhada do DataFrame.
vaccines.shape

vaccines.info()

#Vamos começar tratando os dados faltantes, a estratégia será a de preencher os buracos com o valor anterior válido mais próximo.
vaccines = vaccines.fillna(method='ffill')

#Vamos também filtrar a base de dados de acordo com a coluna date para garantir que ambas as bases de dados tratam do mesmo período de tempo.
vaccines = vaccines[(vaccines['date'] >= '2021-01-01') & (vaccines['date'] <= '2021-12-31')].reset_index(drop=True)

#Agora, vamos alterar o nome das colunas.
vaccines = vaccines.rename(
  columns={
    'location': 'country',
    'total_vaccinations': 'total',
    'people_vaccinated': 'one_shot',
    'people_fully_vaccinated': 'two_shots',
    'total_boosters': 'three_shots',
  }
)

#Vamos então computar novas colunas para enriquecer a base de dados.

#Chaves temporais:
vaccines['month'] = vaccines['date'].apply(lambda date: date.strftime('%Y-%m'))
vaccines['year']  = vaccines['date'].apply(lambda date: date.strftime('%Y'))

#Dados relativos:
vaccines['one_shot_perc'] = round(vaccines['one_shot'] / vaccines['population'], 4)
vaccines['two_shots_perc'] = round(vaccines['two_shots'] / vaccines['population'], 4)
vaccines['three_shots_perc'] = round(vaccines['three_shots'] / vaccines['population'], 4)

#Garantir o tipo do dado é fundamental para consistência da base de dados. Vamos fazer o type casting das colunas.
vaccines['population'] = vaccines['population'].astype('Int64')
vaccines['total'] = vaccines['total'].astype('Int64')
vaccines['one_shot'] = vaccines['one_shot'].astype('Int64')
vaccines['two_shots'] = vaccines['two_shots'].astype('Int64')
vaccines['three_shots'] = vaccines['three_shots'].astype('Int64')

#Por fim, vamos reorganizar as colunas e conferir o resultado final.
vaccines = vaccines[['date', 'country', 'population', 'total', 'one_shot', 'one_shot_perc', 'two_shots', 'two_shots_perc', 'three_shots', 'three_shots_perc', 'month', 'year']]

vaccines.tail()

# Carregamento
# Com os dados manipulados, vamos persisti-lo em disco, fazer o seu download e carrega-lo no Google Data Studio.

vaccines.to_csv('./covid-vaccines.csv', sep=',', index=False)





