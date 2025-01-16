import pymysql


conn = pymysql.connect(
    host='127.0.0.1',
    user='user',
    password='12345',
    db='team_03',
    cursorclass=pymysql.cursors.DictCursor
)


try:
    with conn.cursor() as cursor:
        # table reset 
        sql_delete = "DELETE FROM `trip_category`"
        sql_reset_index = "ALTER TABLE `trip_category` AUTO_INCREMENT = 1"
        cursor.execute(sql_delete)
        conn.commit()
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
