-- Databricks notebook source

SELECT type, COUNT(*) AS total
FROM workspace.default.netflix_silver
GROUP BY type
ORDER BY total DESC;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC Titles Added Per Year

-- COMMAND ----------

SELECT YEAR(date_added) AS year_added, COUNT(*) AS total_titles
FROM workspace.default.netflix_silver
WHERE date_added IS NOT NULL
GROUP BY YEAR(date_added)
ORDER BY year_added;

-- COMMAND ----------

SELECT primary_country, COUNT(*) AS total
FROM workspace.default.netflix_silver
WHERE primary_country IS NOT NULL AND primary_country <> 'Unknown'
GROUP BY primary_country
ORDER BY total DESC
LIMIT 10;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC Most Common Ratings (e.g., PG, TV-MA, etc.)

-- COMMAND ----------

SELECT rating, COUNT(*) AS total
FROM workspace.default.netflix_silver
GROUP BY rating
ORDER BY total DESC;

-- COMMAND ----------

SELECT AVG(duration_num) AS avg_movie_duration
FROM workspace.default.netflix_silver
WHERE type = 'Movie' AND duration_num IS NOT NULL;




-- COMMAND ----------

-- MAGIC %md
-- MAGIC Top 10 Genres (from listed_in)

-- COMMAND ----------

WITH exploded AS (
    SELECT explode(split(listed_in, ',')) AS genre
    FROM workspace.default.netflix_silver
)
SELECT trim(genre) AS genre, COUNT(*) AS total
FROM exploded
GROUP BY trim(genre)
ORDER BY total DESC
LIMIT 10;




-- COMMAND ----------

SELECT type, release_year, COUNT(*) AS total
FROM workspace.default.netflix_silver
WHERE release_year IS NOT NULL
GROUP BY type, release_year
ORDER BY release_year ASC, type ASC;


-- COMMAND ----------

-- MAGIC %md
-- MAGIC Most Frequent Directors

-- COMMAND ----------

WITH exploded AS (
    SELECT explode(split(director, ',')) AS dir
    FROM workspace.default.netflix_silver
    WHERE director IS NOT NULL AND director <> ''
)
SELECT trim(dir) AS director, COUNT(*) AS total
FROM exploded
GROUP BY trim(dir)
ORDER BY total DESC
LIMIT 10;
