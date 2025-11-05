/* Antoine Laldjee-Deroubaix : Premières requêtes SQL */

SELECT DISTINCT genre
FROM GENRE;
/*25 */

SELECT lname
FROM DIRECTORS
WHERE fname = 'Chantal';
/*13 */

SELECT name, year
FROM MOVIE
WHERE name like '%war%';
/*2946 */

SELECT count(*)
FROM MOVIE
WHERE year = 2005;
/*62456 */

SELECT COUNT(*), year
FROM MOVIE
GROUP BY year
ORDER BY COUNT(*) DESC

/* 2005, 2004, 2006 */

SELECT MAX(nb_roles) AS max_roles
FROM (
    SELECT pid, COUNT(DISTINCT role) AS nb_roles
    FROM CASTS
    GROUP BY pid
) AS sous_requete;

/* 428 */
