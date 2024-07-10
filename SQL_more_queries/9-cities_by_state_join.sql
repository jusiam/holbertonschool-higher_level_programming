-- List all cities along with their states
SELECT cities.id, cities.name, states.name
FROM cities
ORDER BY cities.id ASC;