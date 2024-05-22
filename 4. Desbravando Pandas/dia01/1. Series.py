# %%
import pandas as pd

# %% Lista
idades = [30, 42, 90, 34]
idades

# %% De lista para Series
series_idades = pd.Series(idades)
series_idades

# %% Media
series_idades.mean()

# %% Mediana
series_idades.median()

# %% Desvio
series_idades.std()

# %% Variancia
series_idades.var()

# %% Primeiro quartil
series_idades.quantile(0.25)

# %% Estatistica
series_idades.describe()

# %% Acessando indices
series_idades[1]

# %% Novos indices
series_idades.index = ['a', 'b', 'c', 'd']
series_idades

# %% Acessando indices
series_idades['b']

# %% Acessando posicao (independente do indice)
series_idades.iloc[1]
series_idades.iloc[0:2]

# %% Nomeando Series
series_idades.name = 'Idades'
series_idades

# %% Nomeando Series ao criar
series_idades = pd.Series(idades, name='idades')
series_idades
