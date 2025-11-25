import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def conectar_banco():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_DATABASE")
    )


def obter_clientes():
    db = conectar_banco()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT id, razaosocial, cnpj, status_sistema
        FROM clientes
        WHERE status_sistema = 'ATIVO'
    """)

    resultados = cursor.fetchall()
    cursor.close()
    db.close()
    return resultados


def criar_view_inativos(lista_ids):
    if not lista_ids:
        print("\nNenhum cliente inativo encontrado. VIEW não será alterada.")
        return

    ids_str = ", ".join(str(i) for i in lista_ids)

    sql = f"""
    CREATE OR REPLACE VIEW view_clientes_inativos AS
    SELECT id, razaosocial, cnpj FROM clientes
    WHERE id IN ({ids_str});
    """

    db = conectar_banco()
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

    print("\nVIEW criada/atualizada com sucesso!")
