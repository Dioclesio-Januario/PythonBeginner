# %%
import pandas as pd

# %% Carregue os dados do arquivo homicidios
df = pd.read_csv("../data/homicidios.csv", sep=";")

# Informe a quantidade de linhas e colunas
df

# %% Informe o nome da primeira coluna
df.columns[0]

# %% Informe o nome da última coluna
df.columns[-1]
