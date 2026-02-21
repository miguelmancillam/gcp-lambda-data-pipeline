import argparse
import logging
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from datetime import datetime

class DataIngestion:
    def parse_method(self, row):
        def get_value(field):
            if field is None:
                return None
            if isinstance(field, (int, float)):
                return field
            elif isinstance(field, str):
                val = field.strip()
                return val if val and val.lower() != 'null' else None
            elif isinstance(field, datetime):
                return field.isoformat()
            try:
                return field.as_py()
            except Exception:
                return None

        def safe_get(row, key):
            val = get_value(row.get(key))
            if val in ('', 'NULL', 'null'):
                return None
            return val

        return {
            'VendorID': safe_get(row, 'VendorID'),
            'tpep_pickup_datetime': safe_get(row, 'tpep_pickup_datetime'),
            'tpep_dropoff_datetime': safe_get(row, 'tpep_dropoff_datetime'),
            'passenger_count': safe_get(row, 'passenger_count'),
            'trip_distance': safe_get(row, 'trip_distance'),
            'RatecodeID': safe_get(row, 'RatecodeID'),
            'store_and_fwd_flag': safe_get(row, 'store_and_fwd_flag'),
            'PULocationID': safe_get(row, 'PULocationID'),
            'DOLocationID': safe_get(row, 'DOLocationID'),
            'payment_type': safe_get(row, 'payment_type'),
            'fare_amount': safe_get(row, 'fare_amount'),
            'extra': safe_get(row, 'extra'),
            'mta_tax': safe_get(row, 'mta_tax'),
            'tip_amount': safe_get(row, 'tip_amount'),
            'tolls_amount': safe_get(row, 'tolls_amount'),
            'improvement_surcharge': safe_get(row, 'improvement_surcharge'),
            'total_amount': safe_get(row, 'total_amount'),
            'congestion_surcharge': safe_get(row, 'congestion_surcharge'),
            'Airport_fee': safe_get(row, 'Airport_fee')
        }

def run(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', dest='input', required=True)
    parser.add_argument('--output', dest='output', required=True)
    known_args, pipeline_args = parser.parse_known_args(argv)

    data_ingestion = DataIngestion()
    pipeline_options = PipelineOptions(pipeline_args)
    p = beam.Pipeline(options=pipeline_options)

    (p
     | 'ReadParquet' >> beam.io.ReadFromParquet(known_args.input)
     | 'TransformRows' >> beam.Map(lambda row: data_ingestion.parse_method(row))
     | 'WriteToBigQuery' >> beam.io.WriteToBigQuery(
            known_args.output,
            schema={
                'fields': [
                    {'name': 'VendorID', 'type': 'INTEGER'},
                    {'name': 'tpep_pickup_datetime', 'type': 'TIMESTAMP'},
                    {'name': 'tpep_dropoff_datetime', 'type': 'TIMESTAMP'},
                    {'name': 'passenger_count', 'type': 'FLOAT'},
                    {'name': 'trip_distance', 'type': 'FLOAT'},
                    {'name': 'RatecodeID', 'type': 'FLOAT'},
                    {'name': 'store_and_fwd_flag', 'type': 'STRING'},
                    {'name': 'PULocationID', 'type': 'INTEGER'},
                    {'name': 'DOLocationID', 'type': 'INTEGER'},
                    {'name': 'payment_type', 'type': 'INTEGER'},
                    {'name': 'fare_amount', 'type': 'FLOAT'},
                    {'name': 'extra', 'type': 'FLOAT'},
                    {'name': 'mta_tax', 'type': 'FLOAT'},
                    {'name': 'tip_amount', 'type': 'FLOAT'},
                    {'name': 'tolls_amount', 'type': 'FLOAT'},
                    {'name': 'improvement_surcharge', 'type': 'FLOAT'},
                    {'name': 'total_amount', 'type': 'FLOAT'},
                    {'name': 'congestion_surcharge', 'type': 'FLOAT'},
                    {'name': 'Airport_fee', 'type': 'FLOAT'}
                ]
            },
            create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
            write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
        )
     )

    p.run().wait_until_finish()

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    run()
