
import json
import pandas as pd

file = open('vendas.json')

data = json.load(file)

# print(data)

df = pd.DataFrame.from_dict(data)

df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format = '%d/%m/%Y')

# print(df['Data da Compra'])

file.close()