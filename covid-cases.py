# Pacotes nativos do Python
import numpy as np
import pandas as pd
import math
from typing import Iterator
from datetime import datetime, timedelta

#Extração
#Esse código utiliza a biblioteca pandas para ler um arquivo CSV diretamente de um URL. A variável cases armazena os dados do CSV sobre COVID-19, exemplo para 01/12/2021.

cases = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/01-12-2021.csv', sep=',')

cases.head()
