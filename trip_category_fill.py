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
        sql_delete = "DELETE FROM `trip_category`"
        sql_reset_index = "ALTER TABLE `trip_category` AUTO_INCREMENT = 1"
        cursor.execute(sql_delete)
        conn.commit()
        cursor.execute(sql_reset_index)
        conn.commit()

        nazwy = [
            ['nazwa', 1, 'opis'],
            ['nazwa inna' , 2, 'inny opis']
        ]

        for x in nazwy:
            # Create a new record
            sql = "INSERT INTO `trips` (`trip_name`, `category_id`, `description`) VALUES (%s, %s, %s)"
            cursor.execute(sql, (x[0], x[1], x[2] ))
            conn.commit()
            
finally:
    conn.close()

