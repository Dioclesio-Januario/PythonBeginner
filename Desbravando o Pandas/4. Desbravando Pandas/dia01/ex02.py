# %%
import pandas as pd

# %% Converta o seguinte dicionário para DataFrame e obtenha:
# Sumário de cada coluna
# Média da coluna idade
# Último nome da coluna nome

dados = {"nome": ["Téo", "Nah", "Napoleão"],
         "idade": [31, 32, 14]}
df = pd.DataFrame(dados)
df

# %% Sumario de cada coluna
df.describe()
# df.info()

# %% Media da coluna idade
media = df.describe()
media["idade"]['mean']

# %% Ultimo nome da coluna nome
# df["nome"].tail(1)
df["nome"].iloc[-1]
