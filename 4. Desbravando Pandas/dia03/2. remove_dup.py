# %%
import pandas as pd

# %% Criando DataFrame
data = {"Nome": ["Téo", "Nah", "Maria", "Nah", "Lara", "Téo"],
        "Idade": [32, 33, 2, 33, 31, 32],
        }
df = pd.DataFrame(data)
df

# %% Remove duplicatas
df.drop_duplicates()


# OU


# %% Criando DataFrame
data = {"Nome": ["Téo", "Nah", "Maria", "Nah", "Lara", "Téo"],
        "Idade": [32, 33, 2, 33, 31, 32],
        "updated_at": [1, 2, 3, 1, 2, 3]
        }
df = pd.DataFrame(data)
df

# %% Remove duplicatas considerando apenas Nome e Idade
# df.drop_duplicates()  # Nao remove nenhuma linha pois todas linhas sao diferentes

# Organizar pela ultima data de update
df = df.sort_values(by="updated_at",
                    ascending=False)

# Manter a primeira duplicata (ultimo update)
df.drop_duplicates(subset=["Nome", "Idade"],
                   keep="first")
