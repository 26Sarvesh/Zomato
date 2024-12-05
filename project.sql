use project;
select * from zomato_dataset;

-- Qution 1: Retrieve the top 3 cities with the highest number of restaurants in the dataset.

SELECT City, COUNT(RestaurantID) AS Total_Restaurants
FROM zomato_dataset
GROUP BY City
ORDER BY Total_Restaurants DESC
LIMIT 3;


-- Question 2: List all localities with more than 3 restaurants offering table booking.
SELECT Locality, COUNT(RestaurantID) AS Table_Booking_Restaurants
FROM zomato_dataset
WHERE Has_Table_booking = 'Yes'
GROUP BY Locality
HAVING COUNT(RestaurantID) > 3;



-- Question 3: List all restaurants where the rating is greater than the average rating of their respective city.
SELECT RestaurantName, City, Rating
FROM zomato_dataset AS z
WHERE Rating > (SELECT AVG(Rating) FROM zomato_dataset WHERE City = z.City);





-- Question 4: Identify the city with the most diverse cuisine options (count of unique cuisines).
SELECT City, Locality, COUNT(RestaurantID) AS Total_Restaurants
FROM zomato_dataset
GROUP BY City, Locality
ORDER BY Total_Restaurants DESC
LIMIT 1;




-- Question 5: Identify all cities where the average cost for two exceeds 2000.
SELECT City, AVG(Average_Cost_for_two) AS Avg_Cost
FROM zomato_dataset
GROUP BY City
HAVING AVG(Average_Cost_for_two) > 2000;


-- Question 6: Determine the distribution of restaurants by price range across all localities.
SELECT Locality, Price_range, COUNT(RestaurantID) AS Total_Restaurants
FROM zomato_dataset
GROUP BY Locality, Price_range
ORDER BY Locality, Price_range;


-- Question 7: Find the city with the most restaurants delivering now.
SELECT City, COUNT(RestaurantID) AS Delivering_Restaurants
FROM zomato_dataset
WHERE Is_delivering_now = 'Yes'
GROUP BY City
ORDER BY Delivering_Restaurants DESC
LIMIT 10; 


-- Question 8: List all cities where more than 50% of the restaurants have online delivery.
SELECT City,
       (COUNT(CASE WHEN Has_Online_delivery = 'Yes' THEN 1 END) * 100.0 / COUNT(*)) AS Online_Delivery_Percentage
FROM zomato_dataset
GROUP BY City
HAVING Online_Delivery_Percentage > 50;




-- Question 9: Identify restaurants with ratings in the top 10% in their respective cities.
WITH RankedRestaurants AS (
    SELECT RestaurantName, Price_range, Rating,
           RANK() OVER(PARTITION BY Price_range ORDER BY Rating DESC) AS `Rank`
    FROM zomato_dataset
)
SELECT RestaurantName, Price_range, Rating
FROM RankedRestaurants
WHERE `Rank` = 1;



-- Question 10: Find the average cost for two for restaurants serving 'Desserts' in each city.
SELECT City, AVG(Average_Cost_for_two) AS Avg_Cost
FROM zomato_dataset
WHERE Cuisines LIKE '%Desserts%'
GROUP BY City;


-- Question 11: List all restaurants where the cost for two is above the average for their respective locality.
SELECT RestaurantName, Locality, Average_Cost_for_two
FROM zomato_dataset AS z
WHERE Average_Cost_for_two > (
    SELECT AVG(Average_Cost_for_two) 
    FROM zomato_dataset
);



-- Question 12: Retrieve all restaurants with table booking, online delivery, and a rating above 4.
SELECT RestaurantName, City, Rating
FROM zomato_dataset
WHERE Has_Table_booking = 'Yes' AND Has_Online_delivery = 'Yes' AND Rating > 4;



-- Question 13: Calculate the percentage of restaurants in each price range per city.
SELECT City, Price_range, 
       (COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(PARTITION BY City)) AS Percentage
FROM zomato_dataset
GROUP BY City, Price_range;



-- Question 14: Identify the top cuisine for each city based on the number of restaurants serving it.
SELECT City, Cuisines, COUNT(RestaurantID) AS Total_Restaurants
FROM zomato_dataset
GROUP BY City, Cuisines
ORDER BY City, Total_Restaurants DESC;


-- Question 15: List all restaurants where the rating is in the top quartile for their respective price range.
WITH QuartileRating AS (
    SELECT Price_range, RestaurantName, Rating,
           NTILE(4) OVER(PARTITION BY Price_range ORDER BY Rating DESC) AS Quartile
    FROM zomato_dataset
)
SELECT RestaurantName, Price_range, Rating
FROM QuartileRating
WHERE Quartile = 1;


-- Question 16: Identify the city with the highest revenue per vote (Revenue = Average_Cost_for_two * Votes).
SELECT City, SUM(Average_Cost_for_two * Votes) / SUM(Votes) AS Revenue_Per_Vote
FROM zomato_dataset
GROUP BY City
ORDER BY Revenue_Per_Vote DESC
LIMIT 1;





