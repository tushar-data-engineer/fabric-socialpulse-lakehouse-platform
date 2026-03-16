# 🚀 SocialPulse Lakehouse Platform

![Microsoft Fabric](https://img.shields.io/badge/Microsoft-Fabric-blue)
![Apache Spark](https://img.shields.io/badge/Apache-Spark-orange)
![PySpark](https://img.shields.io/badge/PySpark-Data%20Processing-yellow)
![Architecture](https://img.shields.io/badge/Architecture-Medallion-blueviolet)
![Data Quality](https://img.shields.io/badge/Data%20Quality-Great%20Expectations-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

SocialPulse is an end-to-end data engineering project built using Microsoft Fabric that demonstrates how to design and implement a modern **Lakehouse data pipeline** using **Medallion Architecture (Bronze–Silver–Gold)**.

The platform ingests data from a REST API, stores raw data in the Bronze layer of a Lakehouse, performs data quality validation and transformation using PySpark notebooks, and produces analytics-ready datasets in the Gold layer.

This project simulates a real-world social media analytics pipeline where raw post data is processed and aggregated to generate insights about user activity and engagement trends.

---

# 🏗 Architecture

![Architecture](architecture/fabric_medallion_architecture.png)

The pipeline follows the **Medallion Architecture pattern**.

### Bronze Layer

Raw data is ingested directly from the API and stored as JSON files in the Lakehouse.

### Silver Layer

Data is cleaned, validated, and transformed into structured tables using PySpark notebooks.

### Gold Layer

Curated and aggregated datasets are generated for analytics, dashboards, and reporting.

---

# ⚙️ Pipeline Workflow

REST API
↓
Microsoft Fabric Data Pipeline
↓
Bronze Layer (Raw JSON Files)
↓
Data Quality Validation Notebook
↓
Bronze → Silver Transformation
↓
Silver Tables
↓
Silver → Gold Aggregation
↓
Gold Analytics Tables
↓
Power BI Dashboard

---

# 🧰 Technologies Used

* Microsoft Fabric
* Lakehouse Architecture
* Apache Spark / PySpark
* REST API Data Ingestion
* Great Expectations Data Quality Checks
* SQL Analytics Queries
* Git Version Control

---

# 📁 Repository Structure

```
socialpulse-lakehouse-platform
│
├── fabric
│   ├── pipelines
│   ├── notebooks
│   └── configs
│
├── sql
│
├── tests
│
└── architecture
```

**fabric/**
Contains Microsoft Fabric pipelines, notebooks, and configuration files.

**sql/**
Contains SQL scripts used for analytics and reporting.

**tests/**
Contains data quality validation scripts.

**architecture/**
Contains architecture diagrams and system design visuals.

---

# 📊 Example Analytics Output

The Gold layer provides aggregated analytics datasets such as:

| userId | total_posts |
| ------ | ----------- |
| 1      | 10          |
| 2      | 10          |
| 3      | 10          |

These datasets can be used for:

* user engagement analysis
* activity monitoring
* reporting dashboards

---

# 🎯 Use Case

This project demonstrates how organizations can build scalable data pipelines to ingest, transform, and analyze datasets using a modern Lakehouse architecture.

It highlights key data engineering practices including:

* pipeline orchestration
* automated data quality validation
* layered data architecture
* scalable analytics dataset creation

---

# 🔮 Future Improvements

* Incremental data ingestion using watermark processing
* Real-time streaming ingestion pipelines
* CI/CD integration for pipeline deployment
* Data pipeline monitoring dashboards
* Advanced data quality metrics
