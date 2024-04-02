# Instalar as bibliotecas : pandas sqlalchemy e psycopg2-binary
# pip install pandas sqlalchemy psycopg2-binary

import pandas as pd
from sqlalchemy import create_engine


# cria uma conexão com o banco postgres
# string de conexão: postgresql://usuário:senha@localhost:5432/nomebanco
senha = input('Digite a senha do banco de dados: ')
engine = create_engine(f'postgresql://postgres:{senha}@localhost:5432/ecommerce')

for file_name in ["projeto_BDI/produtos.csv", "projeto_BDI/vendas.csv"]:
	df = pd.read_csv(file_name, sep=',')
	# if "Preco" in df.columns:
		# df['Preco'] = df['Preco'].str.replace('$', '', regex=False).astype(float)

	df = df.loc[:, ~df.columns.str.contains('^Unnamed')].copy()

	# salva o dataframe como tabela no banco conectado
	# nome_da_tabela, engine de conexão
	df.to_sql(f'{file_name.split(".")[0].split("/")[-1]}', engine, index=False)
