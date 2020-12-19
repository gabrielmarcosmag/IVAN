"""
@autor: Gabriel Marcos Magalhães
Arquivo onde estão escritas as funções relacionadas a geração de novos dataframes
a partir de tratamentos no dataframe original
"""
import pandas as pd # Biblioteca pandas (manipulação de dataframes)

def mount_df_month(df):
    """
    Função responsável por montar um dataframe com as informações mensais de venda

    Argumentos  df: dataframe com as informações da planilha (dataframe pandas)
    Retorno: Dataframe pandas com as seguintes informações:
    | Mês | Venda média no mês | Faturamento total no mês | Número de vendas no mês |
    """
    df_aux = df.groupby(['mes'])
    data_month = {}
    meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
    for mes in meses:
        data_month[mes] = [df_aux.get_group(mes).valor.mean(),df_aux.get_group(mes).valor.sum(),df_aux.get_group(mes).valor.count()]

    df2 = pd.DataFrame.from_dict(data_month,orient='index',columns=['mean_vendas','total_vendas','n_vendas'])
    return(df2)

def mount_table_k(df):
    """
    Função responsável por montar a tabela de vendas medias mensais do primeiro semestre
    de 2019 por modelo

    Argumentos  df: dataframe com as informações da planilha (dataframe pandas)
    Retorno: Tabela de vendas medias mensais do primeiro semestre
    de 2019 por modelo (dataframe pandas)
    """
    df_aux = df.groupby(['mes','modelo']).valor.mean()
    data_month = {}
    meses = ['janeiro','fevereiro','março','abril','maio','junho','julho']
    modelos = ['A3','A4','A5']
    df2 = pd.DataFrame(meses)
    for mod in modelos:
        aux = []
        for mes in meses:
            try: 
                data_month[mes] = df_aux[mes,mod]
            except:
                data_month[mes] = 0.0
            aux.append(data_month[mes])
        df2[mod] = aux

    df2 = df2.set_index(df2.columns[0]).transpose()
    return(df2)