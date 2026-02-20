# Architecture

## Overview

This folder contains the system architecture design and infrastructure overview of the GCP Lambda Data Pipeline.

The project follows a Lambda Architecture pattern combining:

- Batch Processing Layer
- Streaming Processing Layer
- Analytical Storage Layer

---

## High-Level Flow

1. Raw historical data stored in Cloud Storage
2. Batch processing executed using Apache Beam on Dataflow
3. Real-time events published via Pub/Sub
4. Streaming pipeline processes events using Dataflow
5. Processed data stored in BigQuery
6. Data available for analytics and reporting

---

## Technologies Used

- Google Cloud Storage
- Pub/Sub
- Dataflow
- BigQuery
- Apache Beam
- Cloud Run

---

## Design Considerations

- Scalability
- Fault tolerance
- Schema consistency
- Cost efficiency
- Serverless architecture
