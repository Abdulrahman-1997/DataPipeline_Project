# 💱 Exchange Rate ETL Pipeline with Airflow & MongoDB

This project implements a complete **ETL (Extract, Transform, Load)** pipeline that fetches **currency exchange rates** from a public API, processes the data, and stores it into **MongoDB** using **Apache Airflow**.

---

## 🧰 Tech Stack

| Component      | Purpose                                  |
|----------------|-------------------------------------------|
| **Apache Airflow** | Workflow orchestration (ETL automation) |
| **MongoDB**        | Data storage (NoSQL)                   |
| **Docker Compose** | Environment setup (multi-container)    |
| **Power BI**       | Dashboard & reporting (external use)   |
| **Python**         | Scripting and data processing          |

---

## 📊 Use Case

Track and analyze daily **exchange rates** (e.g., USD → other currencies) by pulling them from an API and storing them in MongoDB for further analytics or Power BI integration.

---

## 🏗️ Architecture

```text
[API] → extract.py → transform.py → load.py → [MongoDB]
                                 ↓
                          Orchestrated via Airflow DAG
