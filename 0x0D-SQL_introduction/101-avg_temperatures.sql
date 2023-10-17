-- display the average temp by city orderd by temp
SELECT city,
    AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;

