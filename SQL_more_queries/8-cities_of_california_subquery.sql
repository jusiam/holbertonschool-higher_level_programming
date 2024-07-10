-- Query to list all cities of California without using JOIN
SELECT id, name
FROM cities
WHERE name = 'California'
ORDER BY id ASC;
