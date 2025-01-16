import pymysql

# Database connection
conn = pymysql.connect(
    host='127.0.0.1',
    user='user',
    password='12345',
    db='team_03',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with conn.cursor() as cursor:
        with open('tabele.sql', "r") as file:
            schema = file.read()

        sql_statements = schema.split(';')

        for statement in sql_statements:
            cursor.execute(statement)

        
        conn.commit()


finally:
    conn.close()

