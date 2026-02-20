# Batch Processing Layer

## Description

This module processes historical data using a distributed ETL pipeline built with Apache Beam and executed on Google Cloud Dataflow.

The batch layer processes 3 years of NYC Yellow Taxi trip data stored in Parquet format.

---

## Dataset

- Source: NYC Taxi and Limousine Commission
- Format: Parquet
- Records processed: +119 million
- Time range: 3 years of monthly data

---

## Processing Steps

1. Read Parquet files from Cloud Storage
2. Data cleansing and validation
3. Schema normalization
4. Aggregation and transformation
5. Load into BigQuery

---

## Key Features

- Distributed processing
- Parallel execution
- Schema validation
- Error handling
- Optimized BigQuery loading

---

## Output

Cleaned and transformed tables in BigQuery ready for analytical queries.
