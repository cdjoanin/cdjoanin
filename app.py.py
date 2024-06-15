import pandas as pd
import time
import subprocess
import os

# Configurações
arquivo_csv = 'C:\\Users\\Leonardo - CPD\\Desktop\\GIT\\painel.csv'  # caminho relativo ao diretório do script
repositorio_git = 'git@github.com:cdjoanin/cdjoanin.git'  # ajuste para o seu repositório Git
intervalo_verificacao = 10  # intervalo de verificação em segundos


def ler_csv():
    try:
        # Lê o arquivo CSV
        df = pd.read_csv(arquivo_csv, sep=';', quotechar='"')

        # Remove as aspas do campo VEICULO
        df['VEICULO'] = df['VEICULO'].str.replace('"', '')

        # Aqui você pode processar o dataframe conforme necessário
        # Por exemplo, imprimir o conteúdo para verificação
        print(df)

        return df  # Retorna o dataframe lido e processado
    except Exception as e:
        print(f"Erro ao ler arquivo CSV: {e}")
        return None

def commit_e_push():
    try:
        # Obtém o diretório atual do script
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))

        # Muda para o diretório do arquivo CSV
        os.chdir(diretorio_atual)

        # Adiciona todas as mudanças ao Git
        subprocess.run(["git", "add", arquivo_csv])
        # Faz o commit das alterações
        subprocess.run(["git", "commit", "-m", "Atualização do arquivo CSV"])
        # Faz o push para o repositório remoto
        subprocess.run(["git", "push", "origin", "master"])

        print("Alterações no arquivo CSV foram enviadas para o Git.")
    except Exception as e:
        print(f"Erro ao fazer commit e push para o Git: {e}")

if __name__ == "__main__":
    # Loop principal
    while True:
        # Verifica se houve alterações no arquivo CSV
        novo_df = ler_csv()
        if novo_df is not None:
            # Se houve alterações, faz commit e push
            commit_e_push()
        
        # Aguarda o próximo intervalo de verificação
        time.sleep(intervalo_verificacao)