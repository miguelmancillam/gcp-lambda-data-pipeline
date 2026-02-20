# Streaming Processing Layer

## Description

This module simulates real-time auction events and processes them using a streaming pipeline.

Events are published to Pub/Sub and processed with Apache Beam running on Dataflow in streaming mode.

---

## Streaming Flow

1. Auction event generated
2. Event published to Pub/Sub topic
3. Dataflow streaming pipeline consumes events
4. Transformations applied
5. Data written to BigQuery

---

## Events Processed

- 39,107 simulated auction events
- Near real-time ingestion
- Structured JSON schema

---

## Key Concepts Demonstrated

- Real-time ingestion
- Event-driven architecture
- Streaming ETL
- Windowing and processing logic
- Fault tolerance
