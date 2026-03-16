# SocialPulse Lakehouse Platform

SocialPulse is an end-to-end data engineering project built using Microsoft Fabric that demonstrates how to design and implement a modern data lakehouse pipeline using Medallion Architecture.

The platform ingests data from a REST API, stores raw data in the Bronze layer of a Lakehouse, performs data quality validation and transformation using PySpark notebooks, and produces analytics-ready datasets in the Gold layer.

This project simulates a real-world social media analytics pipeline where raw post data is processed and aggregated to generate insights about user activity.

## Architecture

The pipeline follows the Medallion Architecture pattern.

Bronze Layer
Raw data is ingested from the source API and stored as JSON files in the Lakehouse.

Silver Layer
Data is cleaned, validated, and transformed into structured tables.

Gold Layer
Aggregated datasets are created for analytics and reporting.

## Pipeline Workflow

REST API
↓
Microsoft Fabric Data Pipeline
↓
Bronze Layer (Raw JSON Files)
↓
Data Quality Validation Notebook
↓
Bronze to Silver Transformation
↓
Silver Tables
↓
Silver to Gold Aggregation
↓
Gold Analytics Tables
↓
Power BI Dashboard

## Technologies Used

Microsoft Fabric
Lakehouse Architecture
Apache Spark / PySpark
REST API Data Ingestion
Great Expectations Data Quality Checks
SQL Analytics Queries
Git Version Control

## Repository Structure

fabric/
Contains Fabric pipelines, notebooks, and configuration files.

sql/
Contains analytics SQL queries used for reporting.

tests/
Contains data quality validation tests.

architecture/
Contains pipeline architecture diagrams.

## Use Case

This project demonstrates how organizations can build scalable data pipelines to ingest, transform, and analyze large datasets using a Lakehouse architecture.

It highlights core data engineering practices including pipeline orchestration, data validation, layered data modeling, and analytics-ready dataset creation.

## Future Improvements

Incremental data ingestion using watermark processing
Real-time streaming ingestion pipelines
CI/CD integration for pipeline deployment
Advanced data quality monitoring dashboards
