# SHOW TABLES
from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute('SHOW TABLES')

        for i, table in enumerate(cursor, start=1):
            print(f'Tabela {i}: {table[0].decode()}')
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
