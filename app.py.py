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

def gerar_pagina_html():
    # Lê o CSV e processa os dados
    df = ler_csv()

    if df is not None:
        # Cria um arquivo HTML simples para exibir os dados
        with open('pagina.html', 'w', encoding='utf-8') as f:
            f.write('<html>\n<head>\n<title>Dados do CSV</title>\n</head>\n<body>\n')
            f.write('<h1>Dados do CSV</h1>\n')
            f.write('<table border="1">\n')
            
            # Escreve cabeçalho da tabela
            f.write('<tr>\n')
            for col in df.columns:
                f.write(f'<th>{col}</th>\n')
            f.write('</tr>\n')
            
            # Escreve os dados
            for i, row in df.iterrows():
                f.write('<tr>\n')
                for value in row:
                    f.write(f'<td>{value}</td>\n')
                f.write('</tr>\n')
            
            f.write('</table>\n')
            f.write('</body>\n</html>')
        
        print("Página HTML gerada com sucesso: pagina.html")
    else:
        print("Não foi possível gerar a página HTML devido a erro na leitura do CSV.")

# Chamada para gerar a página HTML
gerar_pagina_html()
