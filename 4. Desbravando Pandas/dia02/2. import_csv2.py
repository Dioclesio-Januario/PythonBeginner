# %%
import pandas as pd

# %% Import csv
df = pd.read_csv("../data/products.csv",
                 sep=";",
                 names=["ID", "Name", "Description"])
df

# %% Alterando nomes
df = df.rename(columns={"ID": "Id",
                        "Name": "Nome",
                        "Description": "Descricao"})
df
