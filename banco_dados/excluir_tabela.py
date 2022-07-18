# DROP TABLE emails
from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

drop_emails = """
    DROP TABLE IF EXISTS emails
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(drop_emails)
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
