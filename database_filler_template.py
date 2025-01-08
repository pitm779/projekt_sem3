import pymysql

conn = pymysql.connect(
    host='giniewicz.it',
    user='team03',
    password='te@mzaoe',
    db='team03',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with conn.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `trip_category` (`category_name`) VALUES (%s)"
        cursor.execute(sql, ('test'))

        conn.commit()

        # Read data from database
        # sql = "SELECT * FROM `trip_category`"
        # cursor.execute(sql)

        # Fetch all rows
        # rows = cursor.fetchall()

        # Print results
        # for row in rows:
            # print(row)
finally:
    conn.close()

