-- Script to lists all Cities in a given database
SELECT cities.id, cities.name, states.name from cities JOIN states WHERE cities.state_id = states.id ORDER BY cities.id ASC;
