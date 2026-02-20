# GCP Lambda Data Pipeline

Scalable Batch and Streaming Data Architecture built on Google Cloud Platform.

---

## 🇺🇸 English Version

### Overview

Designed and implemented a Lambda-style data architecture integrating batch and real-time processing using Google Cloud Platform.

The project processes:

- 3 years of NYC Yellow Taxi historical data (Batch layer)
- Real-time auction events simulation (Streaming layer)

---

### Architecture Components

- Google Cloud Storage – Raw data storage
- Google Cloud Pub/Sub – Event ingestion
- Google Cloud Dataflow – Distributed data processing
- Google BigQuery – Analytical data warehouse
- Apache Beam – ETL logic
- Cloud Run – HTTP event endpoint

---

### Batch Layer (Historical Data)

- 3 years of monthly Parquet datasets
- +119 million records processed
- Data cleansing and schema validation
- Distributed ETL using Apache Beam on Dataflow
- Loaded into BigQuery for analytical queries

---

### Streaming Layer (Real-Time Data)

- Auction events published via Pub/Sub
- Processed in near real-time with Dataflow template
- Stored in BigQuery for live dashboards
- 39,107 events processed

---

### Key Concepts Demonstrated

- Lambda Architecture
- Batch + Streaming integration
- Distributed ETL
- Schema management
- Cloud IAM configuration
- Serverless ingestion
- Scalable data modeling

---

## 🇪🇸 Versión en Español

### Descripción General

Implementación de una arquitectura Lambda en Google Cloud Platform integrando procesamiento batch y en tiempo real.

El proyecto procesa:

- 3 años de datos históricos de taxis NYC (capa batch)
- Eventos simulados de subastas en tiempo real (capa streaming)

---

### Componentes de la Arquitectura

- Cloud Storage – Almacenamiento de datos crudos
- Pub/Sub – Ingesta de eventos
- Dataflow – Procesamiento distribuido
- BigQuery – Data warehouse analítico
- Apache Beam – Lógica ETL
- Cloud Run – Endpoint HTTP para eventos

---

### Capa Batch

- +119 millones de registros
- Transformación y limpieza de datos
- ETL distribuido con Apache Beam
- Carga a BigQuery

---

### Capa Streaming

- Eventos publicados en Pub/Sub
- Procesamiento casi en tiempo real
- Inserción en BigQuery
- 39,107 registros procesados

---

### Enfoque

Arquitectura escalable, tolerante a fallos y alineada con buenas prácticas modernas de ingeniería de datos.
