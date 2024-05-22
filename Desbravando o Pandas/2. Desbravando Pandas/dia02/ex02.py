# %%
import pandas as pd

# %% Carregue os dados do arquivo homicidios-mulheres-nao-negras
df = pd.read_csv("../data/homicidios-mulheres-nao-negras.csv", sep=";")
df

# %% Informe quais colunas são do tipo numérico
# E quais são do tipo ‘object’
df.dtypes

# %% Informe o tamanho destes dados em memória
df.info(memory_usage="deep")
