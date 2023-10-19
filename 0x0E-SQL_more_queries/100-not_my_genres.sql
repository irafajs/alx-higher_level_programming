-- Script to return list of genres not linked to tv show Dexter
SELECT name FROM tv_genres WHERE  id NOT IN (SELECT genre_id FROM tv_show_genres WHERE show_id = 8) ORDER BY name;
