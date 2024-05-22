# %%
import pandas as pd

# %%
df = pd.read_excel("../data/transactions.xlsx")
df

# %% Remove dup, mantendo a ultima transacao de cada IdCustomer
df_last = df.sort_values(by="DtTransaction", ascending=False)
df_last.drop_duplicates(subset="IdCustomer", keep="first")

# %% Verifica se sao unicos
df_last["IdCustomer"].nunique()
