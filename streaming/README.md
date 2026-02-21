# Streaming Processing Layer

## Overview

This module implements a real-time data ingestion architecture using
Google Cloud serverless services.\
The solution captures auction events through an HTTP endpoint deployed
on Cloud Run, publishes them to Pub/Sub, and processes them using a
managed Dataflow template to load data into BigQuery in real time.

This layer complements the batch processing pipeline and forms part of a
hybrid Lambda Architecture.

------------------------------------------------------------------------

## Architecture

External Auction System\
→ Cloud Run (HTTP Endpoint)\
→ Pub/Sub Topic\
→ Dataflow Template (Streaming Mode)\
→ BigQuery\
→ Looker Studio

------------------------------------------------------------------------

## Components

### 1. Cloud Run (Event Ingestion)

-   Exposes an HTTP endpoint.
-   Receives JSON payloads from the auction system.
-   Validates incoming data.
-   Publishes messages to a Pub/Sub topic.
-   Returns HTTP 200 (success) or error codes (400/500).
-   Service account assigned with Pub/Sub Publisher role.

**Files:** - `main.py` - `requirements.txt`

**Dependencies:** - google-cloud-pubsub - functions-framework -
google-cloud-bigquery

------------------------------------------------------------------------

### 2. Pub/Sub (Messaging Layer)

-   Topic used as real-time ingestion buffer.
-   Decouples ingestion from processing.
-   Enables scalable event-driven architecture.
-   Connected to a subscription consumed by Dataflow.

------------------------------------------------------------------------

### 3. Dataflow (Streaming Processing)

Template used: **Pub/Sub Subscription to BigQuery**

Characteristics: - Fully managed service - Auto-scaling - Streaming mode
enabled - Automatic schema mapping - Real-time insertion into BigQuery -
Handles retries for failed messages

No custom Apache Beam pipeline was required for this stage.\
The managed template performs routing and validation.

------------------------------------------------------------------------

## BigQuery Storage

Dataset: `DatosRealTime`\
Table: `DatosTR`

### Table Schema

  Field         Type
  ------------- -----------
  id_cliente    STRING
  cliente       STRING
  genero        STRING
  id_producto   STRING
  producto      STRING
  precio        FLOAT
  cantidad      INTEGER
  monto         FLOAT
  forma_pago    STRING
  fecreg        TIMESTAMP

Data is inserted continuously in real time.

------------------------------------------------------------------------

## Data Volume

-   Records collected: 39,107
-   Storage size: 2.78 MB
-   Collection period: June 29, 2025 -- July 12, 2025

The architecture is designed to scale automatically as volume increases.

------------------------------------------------------------------------

## Monitoring

Dataflow jobs are monitored through the Google Cloud Console:

States: - Created - Running - Failed (if applicable)

BigQuery tables can be validated using SQL queries such as:

SELECT \* FROM `your-project-id.DatosRealTime.DatosTR` LIMIT 100;

------------------------------------------------------------------------

## Key Features

-   Serverless architecture
-   Event-driven processing
-   Real-time data availability
-   Scalable ingestion pipeline
-   Minimal infrastructure management
-   Integrated visualization with Looker Studio

------------------------------------------------------------------------

## Business Value

This streaming architecture enables:

-   Real-time monitoring of auction sales
-   Identification of high-value customers
-   Analysis of product performance
-   Detection of payment method trends
-   Immediate reaction to market behavior

Combined with the batch processing layer, this module forms a complete
hybrid data platform capable of analyzing both historical trends and
real-time behavior.

------------------------------------------------------------------------

## Future Improvements

-   Custom Apache Beam streaming pipeline
-   Data validation and enrichment layer
-   Dead-letter queue implementation
-   Schema evolution handling
-   Automated data quality monitoring
