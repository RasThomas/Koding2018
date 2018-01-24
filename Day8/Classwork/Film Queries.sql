--SELECT * FROM genre

--SELECT * FROM film LIMIT 10

--SELECT * FROM film WHERE releaseYear = 1996

--SELECT * FROM film WHERE title = "Taxi Driver"

--SELECT * FROM film WHERE title LIKE "%dead%" AND releaseYear =1996 ORDER BY releaseYear DESC

--SELECT film.title AND genre.genreName FROM film JOIN filmgenre AND genre ON film.filmID = filmgenre.filmID AND filmgenre, genre.genreID = filmgenre.genreID

--SELECT * FROM film WHERE title = "Crumb"

--SELECT * FROM  filmgenre WHERE filmID = 32	

--SELECT * FROM genre WHERE genreID = 7

SELECT * FROM film WHERE filmID IN (32, 48, 75, 115, 119)

--SELECT f.title AS Title, f.releaseYear AS "Release Year", h.genreName AS Genre FROM filmgenre g JOIN film f ON g.filmID = f.filmID JOIN genre h ON h.genreID = g.genreID WHERE h.genreName = "Documentary"