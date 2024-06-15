import pandas as pd

arquivo_csv = 'painel.csv'  # caminho relativo ao diretório do script

def ler_csv():
    try:
        # Lê o arquivo CSV
        df = pd.read_csv(arquivo_csv, sep=';', quotechar='"')

        # Remove as aspas do campo VEICULO
        df['VEICULO'] = df['VEICULO'].str.replace('"', '')

        return df  # Retorna o dataframe lido e processado
    except Exception as e:
        print(f"Erro ao ler arquivo CSV: {e}")
        return None
