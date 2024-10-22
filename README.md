
<img src="https://raw.githubusercontent.com/andre-marcos-perez/ebac-course-utils/main/media/logo/newebac_logo_black_half.png" alt="ebac-logo">

---

# Análise de Dados: COVID-19 Dashboard
Professor [André Perez](https://www.linkedin.com/in/andremarcosperez/)

---


# **Tópicos**

<ol type="1">
  <li>Introdução;</li>
  <li>Análise Exploratória de Dados;</li>
  <li>Visualização Interativa de Dados;</li>
</ol>



## 1\. Introdução

> A COVID-19 é uma infecção respiratória aguda causada pelo coronavírus SARS-CoV-2, caracterizada por sua gravidade potencial, alta transmissibilidade e distribuição global. Fonte: Governo brasileiro ([link](https://www.gov.br/saude/pt-br/assuntos/covid-19)).

> A disponibilidade de dados sobre a evolução da pandemia ao longo do tempo em uma região específica é essencial para o combate eficaz. Este projeto tem como objetivo construir um dashboard interativo para explorar e visualizar dados sobre o avanço dos casos e da vacinação no Brasil. O processamento dos dados é feito via Python, enquanto a construção do painel é realizada no Google Data Studio.



### 1.1. TLDR


 - **Dashboard**:
  - Google Data Studio ([link](https://lookerstudio.google.com/u/0/reporting/9d73aa32-1ef2-4341-a830-7a30791bb9de/page/CJlFE)).

 - **Fontes**:
  - Casos pela universidade John Hopkins ([link](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports));
  - Vacinação pela universidade de Oxford ([link](https://covid.ourworldindata.org/data/owid-covid-data.csv)).



### 1.2. Dados


> O notebook detalha os dados da pandemia do ano de 2021 , focando em casos, mortes e vacinação no Brasil. Os dados estão divididos em dois grupos principais:

> - **Casos e mortes**: Organizados pela **Universidade de John Hopkins - JHU**, disponíveis no GitHub e segregados por dia ([link](https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/01-12-2021.csv)) .

> - **Vacinação**: Compilados pela **Universidade de Oxford - OU**, com granularidade diária em um único arquivo ([link](https://covid.ourworldindata.org/data/owid-covid-data.csv)).

> Os dados após tratados, teremos:

**COLUNAS**                               | **DESCRIÇÂO**
----------------------------------        | ------
**CASOS E MORTES**                        |
Date:                                     | Data de Referências
State:                                    | Estado
Country:                                  | País
Population:                               | População estimada
Confirmed:                                | Número acumulado de infectados
Confirmed_1d:                             | Número diário de infectados
Confirmed_moving_avg_7d:                  | Média móvel de 7 dias do número diário de infectados
Confirmed_moving_avg_7d_rate_14d:         | Média móvel de 7 dias dividido pela média móvel de 7 dias de 14 dias atrás
Deaths:                                   | Número acumulado de mortos
Deaths_1d:                                | Número diário de mortos
Deaths_moving_avg_7d:                     | Média móvel de 7 dias do número diário de mortos
Deaths_moving_avg_7d:                     | Média móvel de 7 dias dividido pela média móvel de 7 dias de 14 dias atrás
Month:                                    | Mês de referência
Year:                                     | Ano de referência









**COLUNAS**                               | **DESCRIÇÂO**
----------------------------------        | ------
**VACINAÇÂO**                             |
Date:                                     | Data de referência
Country:                                  | País
Population:                               | População estimada
Total:                                    | Número acumulado de doses administradas
One_shot:                                 | Número acumulado de pessoas com uma dose
One_shot_perc:                            | Número acumulado relativo de pessoas com uma dose
Two_shots:                                | Número acumulado de pessoas com duas doses
Two_shot_perc:                            | Número acumulado relativo de pessoas com duas doses
Three_shots:                              | Número acumulado de pessoas com três doses
Three_shot_perc:                          | número acumulado relativo de pessoas com três doses
Month:                                    | Mês de referência
Year:                                     | Ano de referência



# Aproveite para explorar os dados e entender melhor a evolução da pandemia --> ([link](https://lookerstudio.google.com/u/0/reporting/9d73aa32-1ef2-4341-a830-7a30791bb9de/page/CJlFE))
