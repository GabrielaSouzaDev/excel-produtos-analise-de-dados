# Autor: Gabriela Souza
# Projeto de analise de dados no excel com Pandas

import pandas as pd

planilha = pd.read_excel('vendas.xlsx')

resultado = planilha.groupby(['ID_Produto','Nome_Produto'])['Quantidade_Vendida'].sum()

for (id, produto), quantidade in resultado.items():
    print(f'{id} - {produto} - {quantidade}')