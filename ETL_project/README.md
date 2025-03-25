# BI WebLog ETL Project

This project processes IIS web server log files, transforms the data, and loads it into a PostgreSQL database using a star schema.

## Structure

- `scripts/log_processing.py` – Python ETL script to parse logs, transform, and load data.
- `sql/create_star_schema.sql` – SQL script to create PostgreSQL star schema tables.
- `dags/etl_web_logs_dag.py` – Airflow DAG to automate the ETL process.
- `requirements.txt` – Python dependencies.
