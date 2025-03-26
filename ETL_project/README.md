# 🧠 BI WebLog ETL Project

This project processes raw IIS web server logs and transforms them into a clean, queryable data warehouse using a **Star Schema** loaded into **PostgreSQL**. The ETL workflow is orchestrated with **Apache Airflow** and implemented in **Python**.

---

## 📂 Project Structure

/BI-WebLog-ETL-Project │ ├── dags/ # Airflow DAGs │ └── etl_web_logs_dag.py │ ├── scripts/ # ETL logic │ └── log_processing.py │ ├── sql/ # SQL scripts │ └── create_star_schema.sql │ ├── logs/ # (Optional) Sample raw IIS logs │ ├── requirements.txt # Python dependencies └── README.md # This file


---

## 🧪 What It Does

- Reads raw IIS `.log` files
- Parses and cleans log data
- Extracts:
  - Unique IP addresses → Location info (via GeoIP)
  - Dates → Dimensional date info
- Loads into PostgreSQL:
  - Dimension Tables: `dim_time`, `dim_client`, `dim_file`, etc.
  - Fact Table: `fact_web_access`
- All managed and scheduled with Apache Airflow

---

## 🛠️ How to Set Up

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/weblog-etl.git
cd weblog-etl
