from dataset import df
import pandas as pd
import streamlit as st
import time


def format_number(value, prefix = ''):

    for unit in ['', 'mil']:
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000
    return f'{prefix} {value:.2f} milhões'

#Dataframe receita por estado

df_rec_estado = df.groupby('Local da compra')[['Preço']].sum()
df_rec_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']].merge(df_rec_estado, left_on='Local da compra', right_index=True).sort_values('Preço', ascending=False)

# print(df_rec_estado)

#dataframe receita mensal

df_rec_mensal = df.set_index('Data da Compra').groupby(pd.Grouper(freq='ME'))['Preço'].sum().reset_index()
df_rec_mensal['Ano'] = df_rec_mensal['Data da Compra'].dt.year
df_rec_mensal['Mes'] = df_rec_mensal['Data da Compra'].dt.month_name()

# print(df_rec_mensal)

#dataframe receita por categoria

df_rec_categoria = df.groupby('Categoria do Produto')[['Preço']].sum().sort_values('Preço', ascending=False)

# print(df_rec_categoria.head())

#dataframe vendedores

df_vendedores = pd.DataFrame(df.groupby('Vendedor')['Preço'].agg(['sum','count']))

# print(df_vendedores)

#função para converter arquivo csv

@st.cache_data

def convert_csv(df):
    return df.to_csv(index=False).encode('utf-8')

def mensagem_sucesso():
    success = st.success(
        'Arquivo baixado com sucesso!')
    time.sleep(3)
    success.empty()
