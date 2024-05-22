# %%
import pandas as pd
import numpy as np

# %% Create DF com NaN (dados faltantes)
data = {"nome": ["Téo", "Nah", "Lah", "Mah", "Jo"],
        "idade": [31, 32, 34, 12, np.nan],
        "renda": [np.nan, 3245, 357, 12432, np.nan]}

df = pd.DataFrame(data)
df

# %% Identificar dados faltantes no DF
df.isna()
# df.isna().sum() # Quantos NaN (soma true)?

# %% Identificar dados faltantes na coluna
df["idade"].isna()
# df["idade"].isna().sum() # Quantos NaN (soma true)?

# %% Taxa de NaN (quantos % de dados faltam em cada coluna?)
df.isna().mean()

# %% Preencher os NaN (substituir) - ANALISE DE DADOS
# df.fillna(0) # Com zero
df.fillna({"idade": df["idade"].mean(),
           "renda": df["renda"].mean()})

# %% Remove linhas com NaN (excepto nome)
df.dropna()
# df.dropna(how="all") # Se toda linha for NaN
# df.dropna(subset=["idade", "renda"], how="all") # Se idade e renda for NaN
# df.dropna(subset=["idade", "renda"], how="any") # Se idade ou renda for NaN

# %% Remove colunas com NaN
df.dropna(axis="columns")
