import pandas as pd

# Gera os códigos dos anos das temporadas (ex: '9394', '9495', ..., '2324', '2425')
seasons = []
for start_year in range(1993, 2026):
    end_year = start_year + 1
    season_code = f"{str(start_year)[2:]}{str(end_year)[2:]}"
    seasons.append((f"{start_year}/{end_year}", season_code))

all_seasons_data = []

print("Iniciando o download das temporadas...")

for season_label, code in seasons:
    # URL padrão do Football-Data para a Premier League (E0)
    url = f"https://www.football-data.co.uk/mmz4281/{code}/E0.csv"
    
    try:
        # Lê o CSV diretamente da URL
        df = pd.read_csv(url, encoding='latin1')
        
        # Adiciona uma coluna identificando a temporada
        df['Season'] = season_label
        
        # Seleciona as colunas principais caso existam no arquivo
        cols_of_interest = ['Season', 'Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']
        df_filtered = df[[col for col in cols_of_interest if col in df.columns]]
        
        all_seasons_data.append(df_filtered)
        print(f"✓ Temporada {season_label} baixada com sucesso.")
    except Exception as e:
        # Algumas temporadas antigas podem ter estrutura ligeiramente diferente ou não estar disponíveis
        print(f"✗ Não foi possível baixar a temporada {season_label}.")

# Unifica todos os DataFrames em um único
if all_seasons_data:
    final_df = pd.concat(all_seasons_data, ignore_index=True)
    
    # Renomeia colunas para facilitar a leitura
    final_df.rename(columns={
        'FTHG': 'HomeGoals',
        'FTAG': 'AwayGoals',
        'FTR': 'FullTimeResult'
    }, inplace=True)
    
    # Salva o resultado final em um único arquivo CSV
    output_filename = "premier_league_all_seasons.csv"
    final_df.to_csv(output_filename, index=False)
    print(f"\nDownload concluído! Arquivo salvo como: {output_filename}")
    print(f"Total de partidas consolidadas: {len(final_df)}")