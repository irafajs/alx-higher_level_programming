-- Script to return list of genres not linked to tv show Dexter
SELECT name FROM tv_genres WHERE tv_genres.name NOT IN (SELECT tv_genres.name FROM tv_genres INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id INNER JOIN tv_shows on tv_show_genres.show_id = tv_shows.id WHERE tv_shows.title = 'Dexter') ORDER BY name;
