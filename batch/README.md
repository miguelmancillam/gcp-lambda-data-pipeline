# Batch Processing Layer

## Overview

This module implements the historical batch processing layer of the
pipeline using Apache Beam executed on Google Cloud Dataflow.

It processes large-scale NYC Yellow Taxi trip data stored in Parquet
format and loads cleaned and transformed results into BigQuery for
analytical consumption.

------------------------------------------------------------------------

## Technologies Used

-   Apache Beam
-   Google Cloud Dataflow
-   Google Cloud Storage
-   BigQuery
-   Python

------------------------------------------------------------------------

## Dataset

-   Source: NYC Taxi and Limousine Commission
-   Format: Parquet
-   Volume: +119 million records
-   Time range: 3 years of monthly historical data (2022--2024)

------------------------------------------------------------------------

## Processing Workflow

1.  Read Parquet files from Cloud Storage\
2.  Perform distributed transformations\
3.  Data cleansing and null normalization\
4.  Schema standardization\
5.  Aggregations and business transformations\
6.  Load processed data into BigQuery

------------------------------------------------------------------------

## Environment Preparation

Create working directory:

``` bash
mkdir my_dataflow_project
cd my_dataflow_project
```

Retrieve pipeline files from Cloud Storage:

``` bash
gsutil cp gs://your-bucket/pipeline.py .
gsutil cp gs://your-bucket/requirements.txt .
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

These steps prepare the execution environment and install all required
dependencies for distributed processing on Cloud Dataflow.

------------------------------------------------------------------------

## General Execution Command (Dataflow)

``` bash
python3 pipeline.py   --input gs://your-bucket/input/*.parquet   --output your-project-id:your_dataset.YellowTaxis   --temp_location gs://your-bucket/temp   --project your-project-id   --region us-central1   --runner DataflowRunner   --staging_location gs://your-bucket/staging   --save_main_session
```

### Parameters Description

-   `--input`: Cloud Storage path containing Parquet files\
-   `--output`: BigQuery table in format `project:dataset.table`\
-   `--temp_location`: Temporary files location for Dataflow\
-   `--project`: GCP project ID\
-   `--region`: Dataflow execution region\
-   `--runner`: Execution engine (DataflowRunner for cloud execution)\
-   `--staging_location`: Staging area for job resources\
-   `--save_main_session`: Required for dependency serialization

------------------------------------------------------------------------

## Yearly Historical Backfill Execution

The ingestion was executed incrementally by year to ensure job stability
and optimized resource utilization.

### 2024 Ingestion

``` bash
python3 pipeline.py   \
--input gs://your-bucket/2024/yellow_tripdata_2024-*.parquet \
--output your-project-id:your_dataset.YellowTaxis \
--runner DataflowRunner \
--region us-central1 \
--temp_location gs://your-bucket/temp \
--staging_location gs://your-bucket/staging \
--save_main_session
```

### 2023 Ingestion

``` bash
python3 pipeline.py \
--input gs://your-bucket/2023/yellow_tripdata_2023-*.parquet \
--output your-project-id:your_dataset.YellowTaxis \
--runner DataflowRunner \
--region us-central1 \
--temp_location gs://your-bucket/temp \
--staging_location gs://your-bucket/staging \
--save_main_session
```

### 2022 Ingestion

``` bash
python3 pipeline.py \
--input gs://your-bucket/2022/yellow_tripdata_2022-*.parquet \
--output your-project-id:your_dataset.YellowTaxis \
--runner DataflowRunner \
--region us-central1 \
--temp_location gs://your-bucket/temp \
--staging_location gs://your-bucket/staging \
--save_main_session
```

------------------------------------------------------------------------

## Key Features

-   Distributed processing at scale
-   Horizontal scalability through Dataflow
-   Fault-tolerant execution
-   Schema validation and normalization
-   Incremental historical backfill strategy
-   Optimized BigQuery loading

------------------------------------------------------------------------

## Output

Structured and optimized tables stored in BigQuery, ready for analytical
queries and dashboard visualization.
