# %%
import pandas as pd

# %% Import csv
df = pd.read_csv("../data/customers.csv", sep=";")
df

# %% Convertendo Points de int para str
df["Points"].astype(str)

# %% Gerando nova coluna a partir da coluna Points
df["Points_double"] = df["Points"] * 2
df
