# %%
import pandas as pd

# %% Importando arquivo csv separado por ";" (.. volta duas pastas)
df_customers = pd.read_csv("../data/customers.csv", sep=";")
df_customers

# %% Tamanho do DF
df_customers.shape

# %% Memoria ocupada
df_customers.info(memory_usage="deep")

# %% Estatistica descritiva
df_customers["Points"].describe()

# %% Para converter o dtype de object para int/float
df_customers["Points"].astype(int)

# %% Operacoes (adicionando 1000)
df_customers["Points"] + 1000
# df_customers["Points"] > 1000

# %% Filtrando dados > 1000
condicao = df_customers["Points"] > 1000
df_customers[condicao]

# %% Maximo de pontos
df_customers["Points"].max()

# %% Filtrando dados: pessoa com mais pontos
condicao = df_customers["Points"] == df_customers["Points"].max()
# df_customers[condicao]
# df_customers[condicao]["Name"]
df_customers[condicao]["Name"].iloc[0]

# %% Dados entre 1000 e 2000
condicao = (df_customers["Points"] >= 1000) & (df_customers["Points"] <= 2000)
df_customers[condicao]
# df_customers[condicao].describe()

# %% Se quiser trabalhar com uma condicao, fazer copia (sem prejudicar os DF original)
condicao = (df_customers["Points"] >= 1000) & (df_customers["Points"] <= 2000)
df_1000_2000 = df_customers[condicao].copy()
df_1000_2000  # Novo df para ser manipulado (desvinculado do DF original)

# %% Seleccionar varias colunas
df_customers[["Name", "Points"]]

# %% Ordenar colunas (alphabetical)
df_customers.sort_index(axis="columns")

# %% Renomear colunas
df_renomeado = df_customers.rename(columns={"Name": "Nome",
                                            "Points": "Pontos",
                                            "UUID": "ID"})
df_customers = df_renomeado  # Atribuir os nomes para o DF original
df_customers
