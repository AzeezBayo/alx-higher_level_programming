-- lists all the cities of California in the database hbtn_0d_usa
SELECT id, name FROM cities WHERE state_id=
(
	SELECT id FROM states WHERE id=1
)
ORDER BY id ASC;

