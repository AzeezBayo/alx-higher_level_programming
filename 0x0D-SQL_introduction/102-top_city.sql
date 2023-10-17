-- display 3 city temp in July and Agu ordered  temp
SELECT city,
    AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7
    or month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

