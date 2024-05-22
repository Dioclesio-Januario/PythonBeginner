# %%
import pandas as pd

# %% Dicionario (chaves com mesmas dimensoes)
data = {"nome": ["Teo", "Ana", "Julio"],
        "sobrenome": ["Calvo", "Maria", "Roia"],
        "idade": [30, 20, 25],
        "peso": [70, 65, 80]}

# %% Acessando idade
data["idade"][1]

# %% De dicionario para DataFrame
df = pd.DataFrame(data)
df

# %% Acessando idade
df["idade"].iloc[1]

# %% Acessando nome
df["nome"].iloc[0]

# %% Acessando linha
df.iloc[1]

# %% Alterando e vendo indices
df.index = [1, 2, 3]
df.index

# %% Vendo colunas
df.columns

# %% Informacao do DF
df.info()

# %% Verificar memoria em bytes
df.info(memory_usage='deep')

# %% Tipos de dados de cada coluna
df.dtypes

# %% Atribuir nova coluna no DF
df["altura"] = [165, 160, 180]
df

# %% Estatistica (apenas colunas numericas)
df.describe()

# %% Acessando a media do peso
peso = df.describe()
peso["peso"]["mean"]

# %% Mostrando primeiras linhas (5)
df.head()
# df.head(2)

# %% Mostrando ultimas linhas
df.tail()
# df.tail(2)
