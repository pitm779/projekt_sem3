import pymysql
import generowanie_tabel


liczba_klientów = 150
liczba_wierszy = 30 #liczba klientów z 2+ wpłatami
liczba_pracowników = 5

gen_imiona_nazwiska_email_addressid = generowanie_tabel.generowanie_imiona_nazwiska_email_addressid(liczba_klientów, liczba_pracowników)
tabela_customers = generowanie_tabel.generowanie_customers(liczba_klientów, gen_imiona_nazwiska_email_addressid)
tabela_cost = generowanie_tabel.generowanie_costs(liczba_klientów)
tabela_trips = generowanie_tabel.generowanie_trips(tabela_cost)
tabela_payment = generowanie_tabel.generowanie_payment(liczba_pracowników, liczba_klientów, liczba_wierszy, tabela_trips)
tabela_staff = generowanie_tabel.generowanie_staff(liczba_klientów, liczba_pracowników, gen_imiona_nazwiska_email_addressid)
tabela_address = generowanie_tabel.generowanie_adresow(liczba_pracowników, liczba_klientów)

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

        sql_reset_index = "ALTER TABLE `trips` AUTO_INCREMENT = 1"
        cursor.execute(sql_reset_index)
        conn.commit()
        
        for i in range(0, len(tabela_trips)):
            sql = "INSERT INTO `trips` (`trip_id`, `category_id`, `trip_name`, `cost_to_client`, `begin_date`, `end_date`, `abroad`, `creation_date`, `description`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (tabela_trips[i][0], tabela_trips[i][1], tabela_trips[i][2], tabela_trips[i][3], tabela_trips[i][4], 
                             tabela_trips[i][5], tabela_trips[i][6], tabela_trips[i][7], tabela_trips[i][8]))

            conn.commit()

        sql_reset_index = "ALTER TABLE `address` AUTO_INCREMENT = 1"
        cursor.execute(sql_reset_index)
        conn.commit()   

        for i in range(0, len(tabela_address)):
            sql = "INSERT INTO `address` (`address`, `postal_code`, `city`) VALUES (%s, %s, %s)"    
            cursor.execute(sql, (tabela_address[i][0], tabela_address[i][1], tabela_address[i][2])) 
            conn.commit()

        sql_reset_index = "ALTER TABLE `customers` AUTO_INCREMENT = 1"
        cursor.execute(sql_reset_index)
        conn.commit()   

        for i in range(0, len(tabela_customers)):
            sql = "INSERT INTO `customers` (`customer_id`, `address_id`, `first_name`, `last_name`, `email`, `phone_number`, `birth_date`, `ICE_number`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (tabela_customers[i][0], tabela_customers[i][1], tabela_customers[i][2], tabela_customers[i][3], tabela_customers[i][4], tabela_customers[i][5], tabela_customers[i][6], tabela_customers[i][7]))
            conn.commit()

        sql_reset_index = "ALTER TABLE `staff` AUTO_INCREMENT = 1"
        cursor.execute(sql_reset_index)
        conn.commit() 

        for i in range(0, len(tabela_staff)):
            sql = "INSERT INTO `staff` (`address_id`, `first_name`, `last_name`, `salary`, `email`, `hire_date`, `birth_date`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (tabela_staff[i][0], tabela_staff[i][1], tabela_staff[i][2], tabela_staff[i][3], tabela_staff[i][4], tabela_staff[i][5], tabela_staff[i][6]))
            conn.commit()

        sql_reset_index = "ALTER TABLE `payment` AUTO_INCREMENT = 1"
        cursor.execute(sql_reset_index)
        conn.commit() 

        for i in range(0, len(tabela_payment)):
            sql = 'INSERT INTO `payment` (`payment_id`, `customer_id`, `staff_id`, `trip_id`, `payment_date`, `amount`, `payment_type`) VALUES (%s, %s, %s, %s, %s, %s, %s)'
            cursor.execute(sql, (tabela_payment[i][0], tabela_payment[i][1], tabela_payment[i][2], tabela_payment[i][3], tabela_payment[i][4], tabela_payment[i][5], tabela_payment[i][6]))
            conn.commit()

        sql_reset_index = "ALTER TABLE `costs` AUTO_INCREMENT = 1"
        cursor.execute(sql_reset_index)
        conn.commit() 

        for i in range(0, len(tabela_cost)):
            sql = 'INSERT INTO `costs` (`trip_id`, `name`, `amount`) VALUES (%s, %s, %s)'
            cursor.execute(sql, (tabela_cost[i][0], tabela_cost[i][1], tabela_cost[i][2]))
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

