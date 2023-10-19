-- Script to lists show without genre Comedy in the database
SELECT title FROM tv_shows WHERE id NOT IN ( SELECT DISTINCT show_id FROM tv_show_genres tsg INNER JOIN tv_shows ts ON tsg.show_id = ts.id INNER JOIN tv_genres tg ON tg.id = tsg.genre_id WHERE tg.name
= 'Comedy') ORDER BY title;
