# 🎬 Netflix Data Engineering + Machine Learning Pipeline (Databricks)

This repository contains an end-to-end *Data Engineering & Machine Learning pipeline* built on *Databricks, following the **Medallion Architecture (Bronze → Silver → Gold)*.  
The project ingests raw Netflix data, cleans and transforms it using Spark, generates analytical datasets, and trains an ML model to classify content as *Movie vs TV Show*.

---

## 🚀 Project Overview

This project demonstrates:

- 🔹 Scalable data ingestion using *Unity Catalog Volumes*  
- 🔹 Delta Lake–based Bronze, Silver, Gold tables  
- 🔹 Analysis-ready datasets for BI dashboards  
- 🔹 A full ML pipeline using *Spark MLlib + TF-IDF*  
- 🔹 Databricks SQL Dashboard with visuals  

---

## 🧱 Pipeline Architecture

### *Medallion Flow*

+--------------------+
|   Kaggle CSV file  |
| netflix_titles.csv |
+---------+----------+
          |
          | Upload
          v
+-------------------------------------------+
|              Unity Catalog Volumes        |
| /Volumes/workspace/default/netflix_volume |
|   - netflix_titles.csv (raw file)         |
+---------------+---------------------------+
                |
                | Notebook 01 (ingest)
                v
          [ Bronze Layer ]
         workspace.default
         netflix_bronze (managed Delta)
                |
                | Notebook 02 (clean/transform)
                v
          [ Silver Layer ]
         workspace.default
         netflix_silver (managed Delta)
                |
   +------------+--------------------+
   |                                 |
   | Notebook 03 (analysis)          | Notebook 05 (ML)
   v                                 v
Databricks SQL / Dashboard       workspace.default.model_netflix
- Charts, filters, dashboard     (model artifacts, predictions, MLflow registry)
        |
        v
 [ Gold Layer / Aggregations ] (optional)
 workspace.default.netflix_gold (managed Delta)
        |
        v
Deliverables:
- Dashboard screenshots
- SQL queries
- GitHub repository

---

## 🔧 Tech Stack

- *Databricks*
- *Apache Spark (PySpark)*
- *Delta Lake*
- *Python*
- *Spark SQL*
- *MLlib*
- *Unity Catalog*
- *MLflow (model tracking)*

---

## 📊 Dashboard

A Databricks SQL dashboard is included with:

- ✔️ Content type distribution (Movies vs TV Shows)  
- ✔️ Top countries producing content  
- ✔️ Release year trends  
- ✔️ Popular genres  
- ✔️ Ratings comparison  

Screenshots are included in the /dashboard folder.

---

## 🤖 Machine Learning

A binary classifier predicts whether a title is a *Movie* or *TV Show*.

*Model:*  
- Logistic Regression  
- TF-IDF vectorization  

*Pipeline:*  
- Text cleaning  
- Tokenization  
- Stopword removal  
- TF-IDF transformation  
- Logistic Regression  

*Performance:*  
- Accuracy: NN% (replace after training)

---

## 📂 Project Structure

```text
databricks-netflix-project/
│── 01_ingest_netflix.py            # Bronze ingestion
│── 02_clean_prepare_netflix.py     # Silver cleaning/transformation
│── 03_analysis_netflix.sql         # Analysis queries / dashboard prep
│── 04_gold_aggregations.sql        # Optional aggregations
│── 05_machine_learning_netflix.py  # ML pipeline
│── dashboard/
│   └── screenshots.png
### 📌 Deliverables

Bronze, Silver, Gold Delta tables

ML model saved under Unity Catalog / MLflow

Dashboard with insights

Full Databricks notebooks

GitHub-friendly project structure

### 📜 License

This project is open-source and available under the MIT License.
