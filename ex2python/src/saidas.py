"""
@autor: Gabriel Marcos Magalhães
Arquivo onde estão escritas as funções relacionadas a geração de informações de saida
para o usuário
"""
import pandas as pd # Biblioteca pandas (manipulação de dataframes)
import locale # Biblioteca para formatação de milhares e decimais
from funcs import mount_df_month, mount_table_k

def generate_strings(df):
    """
    Função responsável por montar as strings que podem ser impressas na tela ou usadas
    futuramente na geração de um relatório PDF

    Argumentos  df: dataframe com as informações da planilha (dataframe pandas)
    Retorno: True se a operação for realizada com sucesso, False se não for
    """
    try:
        locale.setlocale(locale.LC_ALL, "") # Setup de locale utilizado para trocar , por . e . por ,
        # (a) Qual foi a venda média total que a loja teve no ano de 2019.
        s1 = f'(a) A venda média total que a loja teve no ano de 2019 foi de R$ {locale.format("%1.2f",df.valor.mean())}'

        # (b) Qual foi o desvio padrão das vendas totais da loja no ano de 2019.
        s2 = f'(b) O desvio padrão das vendas totais da loja no ano de 2019 foi de R$ {locale.format("%1.2f",df.valor.std())}'

        # (c) Quantos automóveis apresentaram valor de venda superior ao valor médio?
        s3 = f'(c) Ao todo, {df[df.valor > df.valor.mean()].valor.count()} apresentaram valor de venda superior ao valor médio.'

        # (d) Quantos automóveis Audi A3 forem vendidos no mês de abril?
        s4 = f'(d) Foram vendidos {df[(df.modelo == "A3") & (df.mes == "abril")].mes.count()} automóveis Audi A3 no mês de abril.'

        # (e) Quantos automóveis Audi A4 foram vendidos no mês de dezembro?
        s5 = f'(e) Foram vendidos {df[(df.modelo == "A4") & (df.mes == "dezembro")].mes.count()} automóveis Audi A4 no mês de dezembro.'

        # (f) Preencha a tabela abaixo com a quantidade (Absoluta) de automóveis vendidos no ano de 2019 segmentado pelos modelos A3; A4; A5? (Responda nessa sequência)
        s6 = "(f) Tabela com a quantidade absoluta de automóveis vendidos no ano de 2019 segmentado pelos modelos A3, A4 e A5"
        df_aux = df.groupby(['modelo']).modelo.count()
        s6t = df_aux.to_markdown(tablefmt="github",headers=["Modelo","Frequência Absoluta"])
       
        # (g) Preencha a tabela abaixo com a quantidade em termos percentuais de automóveis vendidos no ano de 2019 segmentado pelos modelos A3; A4; A5? (Responda nessa sequência)
        s7 = "(g) Tabela com a quantidade percentual de automóveis vendidos no ano de 2019 segmentado pelos modelos A3, A4 e A5"
        df_aux = df.groupby(['modelo']).modelo.count()/df.modelo.count()
        s7t = df_aux.to_markdown(tablefmt="github",headers=["Modelo","Frequência Relativa (%)"], floatfmt=".2%")

        dfm = mount_df_month(df)

        # (h) Qual foi o mês com a maior quantidade de vendas no ano?
        s8 = f'(h) O mês com a maior quantidade de vendas no ano foi "{dfm.n_vendas.idxmax()}".'

        # (i) Qual foi o mês em que a loja obteve maior faturamento?
        s9 = f'(i) O mês com a maior faturamento no ano foi "{dfm.total_vendas.idxmax()}".'

        # (j) Preencha a tabela abaixo com as respectivas vendas medias mensais: 
        s10 = f"(j) Tabela com as respectivas vendas medias mensais."
        s10t = dfm['mean_vendas'].to_markdown(index=True,tablefmt="github",headers=["Mês de venda","Valor médio de vendas (R$)"], floatfmt=".2f")

        # (k) Preencha a tabela abaixo com as respectivas vendas medias mensais do primeiro semestre de 2019 (de Janeiro a Julho)
        s11 = f"(k) Tabela com as respectivas vendas medias mensais do primeiro semestre de 2019 por modelo"
        dfm = mount_table_k(df)
        s11t = dfm.to_markdown(index=True,tablefmt="github", floatfmt=".2f")

        # s = [s0,s1,s2,s3,s4,s5,s6,s7,s8,s82]
        s = [s1, s2, s3, s4, s5, s6, s6t, s7, s7t, s8, s9, s10, s10t, s11, s11t]

        return(s)
    except:
        print("Não foi possível gerar as strings")
        return False

def print_results(df):
    """
    Função responsável por imprimir os resultados do período na tela para o usuário

    Argumentos  df: dataframe com as informações da planilha (dataframe pandas)
    Retorno: True se a operação for realizada com sucesso, False se não for
    """
    try:
        infos = generate_strings(df) # Geração das strings com informações a serem escritas
        spc = "\n\n"
        print(spc)
        for info in infos:
            print(info+spc)
        return True
    except:
        print("Não foi possível imprimir os resultados")
        return False
