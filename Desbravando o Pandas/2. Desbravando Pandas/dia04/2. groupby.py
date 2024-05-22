# AGREGAR DADOS (resumir os dados)

# %%
import pandas as pd

# %% Import excel
df = pd.read_excel("../data/transactions.xlsx")
df

# %% Pontos acumulados de um usuario (filtrar e somar os pontos)
condicao = df["IdCustomer"] == "5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"
df_user = df[condicao]
df_user["Points"].sum()

# %%  Pontos acumulados de todos usuarios
df_sumary = df.groupby(["IdCustomer"])["Points"].sum()
df_sumary
# df_sumary.reset_index() # Devolve em DF

# %%  Pontos acumulados com quantidade de transacoes
(df.groupby(["IdCustomer"]).agg({"Points": "sum",
                                "UUID": "count",
                                 "DtTransaction": "max"})
 .rename(columns={"Points": "Valor",
                  "UUID": "Frequencia",
                  "DtTransaction": "UltimaData"})
 .reset_index())
