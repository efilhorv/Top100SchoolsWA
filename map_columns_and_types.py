import mysql.connector

# Configurações de conexão
host = 'localhost'
user = 'root'
password = ''
database = 'WA_OPEN_DATA'

# Tabelas que você deseja mapear
tables = ['rank_school_top100', 'wa_school_list']

# Estabelecer conexão com o servidor MySQL
with mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
) as connection:
    with connection.cursor() as cursor:
        for table in tables:
            print(f"=== Tabela: {table} ===")
            
            # Consulta para obter informações sobre colunas e tipos
            describe_query = f"DESCRIBE {table}"
            
            try:
                cursor.execute(describe_query)
                columns_info = cursor.fetchall()
                
                # Exibir informações sobre colunas e tipos
                for column_info in columns_info:
                    print(column_info)
                
            except mysql.connector.Error as err:
                print(f"Erro ao obter informações para a tabela {table}: {err}")


