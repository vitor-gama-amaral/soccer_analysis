import pandas as pd

# URL da lista oficial de maiores artilheiros
url = "https://en.wikipedia.org/wiki/List_of_Premier_League_players_with_100_or_more_goals"

# Lê as tabelas da página
tables = pd.read_html(url)

# A primeira tabela contém a lista dos jogadores com 100+ gols
top_scorers = tables[0]

# Exibe os primeiros colocados no terminal
print(top_scorers[['Rank', 'Player', 'Goals', 'Apps', 'Ratio', 'First', 'Last']].head(10))

# Salva em um arquivo CSV
top_scorers.to_csv("premier_league_top_scorers_all_time.csv", index=False)
print("\nArquivo 'premier_league_top_scorers_all_time.csv' gerado com sucesso!")