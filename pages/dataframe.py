import streamlit as st
from dataset import df
from estudos.Python.streamlit.pages.utils import convert_csv, mensagem_sucesso

st.title('Dataset de Vendas')
with st.expander('colunas'):
    colunas = st.multiselect(
        'Selecione as colunas',
        list(df.columns),
        list(df.columns)
        )
st.sidebar.title('Filtros')
with st.sidebar.expander('Categoria do produto'):
    categorias = st.multiselect(
        'Selecione as categorias',
        df['Categoria do Produto'].unique(),
        df['Categoria do Produto'].unique()
    )

with st.sidebar.expander('Preço do produto'):
    preco = st.slider(
        'Selecione o preço',
        0, 5000,
        (0, 5000)
    )

with st.sidebar.expander('Data da compra'):
    data_compra = st.date_input(
        'Selecione a data',
        (df['Data da Compra'].min(),
         df['Data da Compra'].max()
         )
    )

query = '''
    `Categoria do Produto` in @categorias and \
    @preco[0]  <= Preço <= @preco[1] and \
    @data_compra[0] <= `Data da Compra` <= @data_compra[1]
'''
filtro_dados = df.query(query)
filtro_dados = filtro_dados[colunas]

st.markdown(f'A tabela possui :blue[{filtro_dados.shape[0]}] linhas e :blue[{filtro_dados.shape[1]}] colunas')

st.markdown('Escreva um nome do arquivo')

coluna1, coluna2 = st.columns(2)
with coluna1:
    nomeArquivo = st.text_input(
        '',
        label_visibility = 'collapsed'
    )
    nomeArquivo += '.csv'
with coluna2:
    st.download_button(
        'Baixar aquivo',
        data = convert_csv(filtro_dados),
        file_name = nomeArquivo,
        mime = 'text/csv',
        on_click = mensagem_sucesso()
    )

st.dataframe(filtro_dados)