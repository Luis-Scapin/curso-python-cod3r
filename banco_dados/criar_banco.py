from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='Db@1234#',
    auth_plugin='mysql_native_password'
)

cursor = conexao.cursor()
# CREATE DATABASE IF NOT EXISTS agenda
cursor.execute('CREATE DATABASE agenda')
