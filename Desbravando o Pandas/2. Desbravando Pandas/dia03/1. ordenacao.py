# %%
import pandas as pd

# %% Import csv
df = pd.read_csv("../data/customers.csv", sep=";")
df

# %% Ordenar DF por pontos
df.sort_values(by="Points")
# df.sort_values(by="Points", ascending=False)

# %% Ordenar DF por 1. pontos e 2. nome
df.sort_values(by=["Points", "Name"])
# df.sort_values(by=["Points", "Name"], ascending=[False, True])
