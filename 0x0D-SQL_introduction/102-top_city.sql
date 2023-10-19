-- Script to display top 3 of cities temperatures during defined months
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month in (7, 8) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
