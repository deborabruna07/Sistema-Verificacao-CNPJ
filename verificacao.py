import requests
import pandas as pd
from db import criar_view_inativos, obter_clientes

def consultar_api(cnpj):
    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
    
    try:
       resp = requests.get(url, timeout=10)
       if resp.status_code == 200:
            dados = resp.json()
            return dados.get("situacao")
       else:
           return "ERRO_HTTP"
    except:
        return "ERRO_CONEXAO"


def verificar_clientes():
    clientes = obter_clientes()
    ids_inativos = []

    for cliente in clientes:

        cnpj = cliente["cnpj"].replace(".", "").replace("/", "").replace("-", "")

        status_receita = consultar_api(cnpj)

        print(f"{cliente['razaosocial']} → {status_receita}")

     
        if status_receita != "ATIVA":
            ids_inativos.append(cliente["id"])

    criar_view_inativos(ids_inativos)



def verificar_e_atualizar_excel(caminho):

    df = pd.read_excel(caminho)

    df_ativos = []    
    df_inativos = []   

    for _, cliente in df.iterrows():
        cnpj = str(cliente["CNPJ"]).strip()


        if cnpj == "" or pd.isna(cnpj):
            continue

        situacao = consultar_api(cnpj)

        print(f"{cliente['RAZAOSOCIAL']} → {situacao}")

        if situacao == "ATIVA":
            df_ativos.append(cliente)
        else:
            df_inativos.append(cliente)

    df_ativos = pd.DataFrame(df_ativos)
    df_inativos = pd.DataFrame(df_inativos)

    df_ativos.to_excel("excel/clientes_ativos.xlsx", index=False)
    df_inativos.to_excel("excel/clientes_inativos.xlsx", index=False)

    print("\nArquivos gerados com sucesso:")
    print("- clientes_ativos.xlsx")
    print("- clientes_inativos.xlsx")

        