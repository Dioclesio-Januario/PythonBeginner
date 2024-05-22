# %%
import pandas as pd
import numpy as np

# %% Import csv
df = pd.read_csv("../data/customers.csv", sep=";")
df

# %% Criar nova coluna a partir de outra
df["Points_double"] = df["Points"] * 2
df["Points_double"] = df["Points"] / 2
df

# %% Criar nova coluna a partir de duas
df["Points_div"] = df["Points_double"] / df["Points"]
df

# %% Criar nova coluna com um escalar
df["constante"] = 1
df

# %% Criando nova coluna com operacoes
df["Points_log"] = np.log(df["Points"])
df

# %% Transformando nomes para maiuscula e pegando o primeiro(antes do _)


def get_first(nome: str):
    nome = nome.upper()
    return nome.split("_")[0]


# %% Aplicando a def em toda coluna Names
df["Name_first"] = df["Name"].apply(get_first)
df


# OU


# %% Funcao lambda
# get_f = lambda nome: nome.upper().split("_")[0]
# df["Name_f"] = df["Name"].apply(get_f)
# df

# %% Intervalo de pontos
def intervalo_pontos(pontos):
    if pontos < 2500:
        return "Baixo"
    elif pontos < 3500:
        return "Medio"
    else:
        return "Alto"


# %% Aplicando na coluna pontos
df["Faixa_pontos"] = df["Points"].apply(intervalo_pontos)
df
