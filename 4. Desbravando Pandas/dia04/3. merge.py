# JUNTANDO DATAFRAMES

# %%
import pandas as pd

# %% Create DF users (sistema)
data_users = {"id": [1, 2, 3, 4],
              "nome": ["Teo", "Mat", "Nah", "Mah"],
              "idade": [31, 31, 32, 32]}

df_user = pd.DataFrame(data_users)
df_user

# %% Create DF transactions (compra)
data_transacoes = {"id_user": [1, 1, 1, 2, 3, 3, 5],
                   "vl": [432, 532, 123, 6, 4, 87, 10],
                   "qtProdutos": [2, 1, 3, 6, 10, 2, 7]}

df_transacao = pd.DataFrame(data_transacoes)
df_transacao

# %% Operando dois DF com merge (df_transacao a esquerda e df_user a direita)
# df_transacao.merge(df_user) - Especifica esquerda/direita

# Mantem linhas de df_transacao (how) e puxa df_user
# [id_user como chave da esquerda (left_on) e id como chave da direita (right_on)]
df_transacao.merge(df_user,
                   how="left",
                   left_on="id_user",
                   right_on="id")
