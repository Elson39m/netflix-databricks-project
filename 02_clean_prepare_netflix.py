# Databricks notebook source
##Load Bronze Table
df = spark.table("workspace.default.netflix_bronze")
display(df)



# COMMAND ----------

##Drop Duplicates
from pyspark.sql.functions import trim, to_date, expr, split, regexp_extract

# Remove duplicates
df = df.dropDuplicates()

# Fill nulls
df = df.fillna({
    "country": "Unknown",
    "rating": "Unknown",
    "duration": "Unknown"
})

# Clean date
df = df.withColumn("date_added_clean", trim(df["date_added"]))
df = df.withColumn(
    "date_added",
    expr("try_to_date(date_added_clean, 'MMMM d, yyyy')")
)
df = df.drop("date_added_clean")

# Clean release_year
df = df.withColumn(
    "release_year",
    expr("try_cast(release_year AS int)")
)

# Clean duration
df = df.withColumn(
    "duration_num",
    expr("try_cast(regexp_extract(duration, '(\\\\d+)', 1) AS int)")
)

# Primary country
df = df.withColumn("primary_country", trim(split(df.country, ",")[0]))

display(df)



# COMMAND ----------

##CREATING THE SILVER TABLE PROPERLY
df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.default.netflix_silver")



# COMMAND ----------

##VERIFY SILVER TABLE EXISTS
spark.sql("SHOW TABLES IN workspace.default").show()




# COMMAND ----------

spark.sql("SELECT COUNT(*) FROM workspace.default.netflix_silver").show()




# COMMAND ----------




# COMMAND ----------





# COMMAND ----------







# COMMAND ----------







# COMMAND ----------




# COMMAND ----------




