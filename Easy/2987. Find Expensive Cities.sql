SELECT city from Listings
GROUP BY city
HAVING AVG(price) > (
    SELECT AVG(price) from Listings
)
ORDER BY city