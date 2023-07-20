-- List all cities of Carlifornia that can be found in the database
-- Not allowed to use JOIN

SELECT id, name
FROM cities
WHERE state_id = 1
ORDER BY cities.id;
