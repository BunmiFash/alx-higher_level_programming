-- List all cities of Carlifornia that can be found in the database
-- Not allowed to use JOIN

SELECT cities.id, cities.name
FROM cities, states
WHERE states.name = "California"
ORDER BY cities.id ASC
