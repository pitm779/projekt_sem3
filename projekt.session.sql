
WITH kolejne_wycieczki AS (
    SELECT 
        customer_id,
        trip_id,
        LEAD(trip_id) OVER (PARTITION BY customer_id ORDER BY trip_id) AS next_trip_id
    FROM 
        payment
)
SELECT 
    customer_id,
    trip_id AS first_trip_id,
    next_trip_id AS second_trip_id
FROM 
    kolejne_wycieczki
WHERE 
    next_trip_id IS NOT NULL
    AND trip_id <> next_trip_id;


WITH kolejne_wycieczki AS (
    SELECT 
        customer_id,
        trip_id,
        LEAD(trip_id) OVER (PARTITION BY customer_id ORDER BY trip_id) AS next_trip_id
    FROM 
        payment
)
SELECT 
    
    trip_id AS id_wycieczki,
    COUNT(trip_id) AS liczba_powrotów
FROM 
    kolejne_wycieczki
WHERE 
    next_trip_id IS NOT NULL
    AND trip_id <> next_trip_id
GROUP BY trip_id;

SELECT SUM(amount) FROM payment;


SELECT category_id, SUM(suma_klientów) AS liczba_klientów, 
SUM(suma_koszt) as koszty, 
SUM(suma_klientów * trips.cost_to_client) as przychód,
 SUM(suma_klientów * trips.cost_to_client) - SUM(suma_koszt) as dochód FROM trips

LEFT JOIN (SELECT trip_id, SUM(amount) AS suma_klientów FROM payment
            GROUP BY trip_id) AS liczba_klientów
ON trips.trip_id = liczba_klientów.trip_id

LEFT JOIN (SELECT trip_id, SUM(amount) AS suma_koszt FROM costs
            GROUP BY trip_id) AS suma_kosztów
ON trips.trip_id = suma_kosztów.trip_id

GROUP BY category_id;





