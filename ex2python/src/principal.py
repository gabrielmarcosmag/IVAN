"""
@autor: Gabriel Marcos Magalhães
Função principal que faz a leitura do banco de dados do aquivo, obtém um banco
de dados e imprime os resultados desejados
"""
import pandas as pd # Importação da biblioteca pandas (manipulação de dataframes)
import os
# Bibliotecas desenvolvidas para o projeto
from saidas import print_results # Impressão dos resultados

def main():
    os.system("clear") # Limpeza do terminal

    # Escolha o arquivo a ser usado (xlsx)
    arq = "../dados/Dados.xlsx"
    # Leitura do arquivo
    df = pd.read_excel(arq, sheet_name='Vendas')
    # Renomeando as colunas
    df.columns = ['marca', 'modelo', 'ano', 'valor', 'mes']

    # Impressão dos resultados
    try:
        print_results(df)
    except:
        print("Não foi possível imprimir os resultados")
        return False

if __name__ == "__main__":
    main()
