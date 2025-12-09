# Databricks notebook source


# COMMAND ----------

df = spark.table("workspace.default.netflix_silver")
display(df)


# COMMAND ----------

data = df.select(
    "type",
    "description",
    "listed_in",
    "primary_country"
).na.drop()


# COMMAND ----------

from pyspark.ml.feature import StringIndexer

label_indexer = StringIndexer(
    inputCol="type",
    outputCol="label"
)


# COMMAND ----------

from pyspark.ml.feature import Tokenizer, StopWordsRemover, HashingTF, IDF

tokenizer = Tokenizer(inputCol="description", outputCol="words")
remover = StopWordsRemover(inputCol="words", outputCol="filtered")
hashingTF = HashingTF(inputCol="filtered", outputCol="rawFeatures")
idf = IDF(inputCol="rawFeatures", outputCol="features")


# COMMAND ----------

from pyspark.ml.classification import LogisticRegression

lr = LogisticRegression(featuresCol="features", labelCol="label")


# COMMAND ----------

from pyspark.ml import Pipeline

pipeline = Pipeline(stages=[
    label_indexer,
    tokenizer,
    remover,
    hashingTF,
    idf,
    lr
])


# COMMAND ----------

train_data, test_data = data.randomSplit([0.7, 0.3], seed=42)


# COMMAND ----------

model = pipeline.fit(train_data)


# COMMAND ----------

predictions = model.transform(test_data)
display(predictions.select("type", "probability", "prediction"))


# COMMAND ----------

from pyspark.ml.evaluation import MulticlassClassificationEvaluator

evaluator = MulticlassClassificationEvaluator(
    labelCol="label", 
    predictionCol="prediction", 
    metricName="accuracy"
)

accuracy = evaluator.evaluate(predictions)
print("Accuracy:", accuracy)
