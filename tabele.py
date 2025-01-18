import pymysql

# Database connection
conn = pymysql.connect(
    host='giniewicz.it',
    user='team03',
    password='te@mzaoe',
    db='team03',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with conn.cursor() as cursor:
        with open('tabele.sql', "r") as file:
            schema = file.read()

        sql_statements = schema.split(';')

        for statement in sql_statements:
            statement = statement.strip()
            if statement:
                cursor.execute(statement)

        
        conn.commit()

finally:
    conn.close()