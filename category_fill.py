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
        # table reset 

        sql_reset_index = "ALTER TABLE `trip_category` AUTO_INCREMENT = 1"
        cursor.execute(sql_reset_index)
        conn.commit()

        nazwy = ['Przygoda', 'Historyczna', 'Familijna', 'Duchowa', 'Sportowa', 'Kulturowa']

        for x in nazwy:
            # Create a new record
            sql = "INSERT INTO `trip_category` (`category_name`) VALUES (%s)"
            cursor.execute(sql, (x))
            conn.commit()

finally:
    conn.close()
