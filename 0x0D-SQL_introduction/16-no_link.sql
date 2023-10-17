-- Script to return name and score in desc and only where name has a value
SELECT score, name FROM second_table WHERE name != '' ORDER BY SCORE DESC;
