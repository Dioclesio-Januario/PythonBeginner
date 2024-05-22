# %%
import pandas as pd

# %% Import excel
df = pd.read_excel("../data/transactions.xlsx")
df

# %% Tamanho do DF
df.shape

# %% Primeiras 5 linhas
df.head()

# %% Ultimas 5 linhas
df.tail()

# %% Ordenar colunas
df = df[["UUID", "IdCustomer", "Points", "DtTransaction"]]
df

# %% Memoria ocupada
df.info(memory_usage="deep")
