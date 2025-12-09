# Databricks notebook source
##Set paths
raw_path = "/Volumes/workspace/default/netflix_volume/netflix_titles.csv"
database = "workspace.default"
bronze_table = "netflix_bronze"




# COMMAND ----------

##Load the CSV
df_raw = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(raw_path)

display(df_raw)




# COMMAND ----------

##Read raw CSV
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {database}")
df_raw.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable(f"{database}.{bronze_table}")



# COMMAND ----------

##Verify
spark.sql(f"SELECT COUNT(*) FROM {database}.{bronze_table}").show()

