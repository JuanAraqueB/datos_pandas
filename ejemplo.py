import pandas as pd

url = 'https://github.com/JuanAraqueB/datos_pandas/blob/main/employees.csv'

data = pd.read_csv(url, delimiter=';')

data.head()

