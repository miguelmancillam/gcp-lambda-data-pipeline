# Batch Processing Layer

## Overview

This module implements the historical batch processing layer of the
pipeline using Apache Beam executed on Google Cloud Dataflow.

It processes large-scale historical taxi trip data in Parquet format and
loads cleaned results into BigQuery.

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
-   Time range: 3 years of monthly data

------------------------------------------------------------------------

## Processing Workflow

1.  Read Parquet files from Cloud Storage\
2.  Perform distributed transformations\
3.  Data cleansing and validation\
4.  Schema normalization\
5.  Aggregation and business transformations\
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

These steps prepared the execution environment and installed all
required dependencies for distributed processing on Cloud Dataflow.

------------------------------------------------------------------------

## Execution Example

``` bash
python pipeline.py \
  --runner=DataflowRunner \
  --project=your-project-id \
  --region=us-central1 \
  --temp_location=gs://your-bucket/temp \
  --staging_location=gs://your-bucket/staging
```

------------------------------------------------------------------------

## Key Features

-   Distributed processing
-   Horizontal scalability
-   Fault tolerance
-   Schema validation
-   Error handling
-   Optimized BigQuery loading

------------------------------------------------------------------------

## Output

Structured and optimized tables in BigQuery ready for analytical queries
and dashboard consumption.

