import os
import re
import pandas as pd

def extrair_nome_pasta(caminho_arquivo):
    """
    Extrai o nome da pasta a partir do caminho do arquivo.
    
    Args:
        caminho_arquivo (str): O caminho completo do arquivo.
    
    Returns:
        str: O nome da pasta.
    """
    # Extrai o nome da pasta a partir do caminho
    return os.path.basename(os.path.dirname(caminho_arquivo))

def processar_arquivo(caminho_arquivo):
    """
    Processa um único arquivo .xlsx, extraindo e tratando os dados.

    Args:
        caminho_arquivo (str): O caminho completo do arquivo .xlsx.

    Returns:
        pd.DataFrame: Um DataFrame com os dados tratados.
    """
    print(f"Processando: {caminho_arquivo}")
    
    # Extrai o nome da pasta
    nome_pasta = extrair_nome_pasta(caminho_arquivo)
    
    # Lê o arquivo .xlsx
    # Adapte o `skiprows` e `usecols` conforme o seu arquivo
    df = pd.read_excel(caminho_arquivo, skiprows=2, usecols=[0, 1], header=None)

    # Renomeia as colunas, se necessário.
    # df.columns = ['coluna_A', 'coluna_B']
    
    # Adiciona uma nova coluna com o nome da pasta
    df['origem_pasta'] = nome_pasta
    
    return df

def main(pastas_entrada, caminho_base_entrada, caminho_base_saida, nome_arquivo_saida):
    """
    Função principal que orquestra o processamento de todos os arquivos.

    Args:
        pastas_entrada (list): Lista de nomes das subpastas a serem processadas.
        caminho_base_entrada (str): O caminho para a pasta principal de entrada.
        caminho_base_saida (str): O caminho para a pasta principal de saída.
        nome_arquivo_saida (str): O nome do arquivo CSV de saída.
    """
    todos_os_dfs = []
    
    # Cria a pasta de saída se ela não existir
    os.makedirs(caminho_base_saida, exist_ok=True)
    
    for nome_pasta in pastas_entrada:
        caminho_completo_pasta = os.path.join(caminho_base_entrada, nome_pasta)
        
        # Verifica se a pasta existe
        if not os.path.isdir(caminho_completo_pasta):
            print(f"Aviso: A pasta '{caminho_completo_pasta}' não foi encontrada. Pulando.")
            continue
            
        for nome_arquivo in os.listdir(caminho_completo_pasta):
            # Processa apenas arquivos .xlsx
            if nome_arquivo.endswith('.xlsx'):
                caminho_completo_arquivo = os.path.join(caminho_completo_pasta, nome_arquivo)
                df_tratado = processar_arquivo(caminho_completo_arquivo)
                if df_tratado is not None:
                    todos_os_dfs.append(df_tratado)
    
    if not todos_os_dfs:
        print("Nenhum arquivo .xlsx encontrado ou processado.")
        return
        
    # Concatena todos os DataFrames em um único
    df_final = pd.concat(todos_os_dfs, ignore_index=True)
    
    # Constrói o caminho completo para o arquivo de saída
    caminho_saida_csv = os.path.join(caminho_base_saida, nome_arquivo_saida)
    
    # Salva o DataFrame final em um arquivo CSV
    df_final.to_csv(caminho_saida_csv, index=False)
    
    print("\n---")
    print(f"Processamento concluído! O arquivo '{caminho_saida_csv}' foi criado com sucesso.")
    print("---")

if __name__ == "__main__":
    # Nomes das subpastas que serão processadas
    pastas_a_processar = ['pasta_1', 'pasta_2', 'pasta_3']
    
    # Caminho para as pastas, usando o diretório atual como base
    caminho_base_entrada = os.path.join(os.getcwd(), 'dados_entrada')
    caminho_base_saida = os.path.join(os.getcwd(), 'dados_saida')
    
    # Nome do arquivo de saída
    nome_arquivo_saida = 'dados_consolidado.csv'
    
    # Executa a função principal
    main(pastas_a_processar, caminho_base_entrada, caminho_base_saida, nome_arquivo_saida)