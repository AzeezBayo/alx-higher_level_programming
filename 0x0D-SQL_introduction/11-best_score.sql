-- list all records of table second_table
-- displays scores >= 10 and names 
SELECT `score`,
    `name`
FROM second_table
WHERE score >= 10
ORDER BY `score` DESC;

