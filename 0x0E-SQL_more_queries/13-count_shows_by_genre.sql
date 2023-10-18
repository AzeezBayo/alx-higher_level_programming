-- lists all genres from hbtn_0d_tvshows ordered by number of shows linked
SELECT	genres.name
AS 	genre,
COUNT(show_gen.show_id) AS number_of_shows
FROM	tv_genres
AS	genres
INNER JOIN tv_show_genres AS show_gen
ON genres.id = show_gen.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;

