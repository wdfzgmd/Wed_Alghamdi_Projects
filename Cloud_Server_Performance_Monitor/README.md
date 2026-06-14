# Cloud-Ready Server Performance Monitor & Analytics

It is an end-to-end Systems Engineering and Data Analytics project designed to monitor, log, and analyze server infrastructure metrics in real-time.

## Project Overview
This project is utilized as a software-defined monitoring agent that captures critical hardware metrics from an operating system and streams them into a structured data pipeline. Furthermore, it visualizes the system's health using an interactive business intelligence dashboard with real-time alerting mechanisms.

## System Architecture & Workflow
1. **Data Collection (Python):** A continuous background script utilizing the `psutil` library monitors real-time CPU and RAM utilization.
2. **Data Logging (Data Engineering):** Metrics are dynamically appended to a time-series `server_logs.csv` engine, implementing failure-safe flushing mechanisms.
3. **Chaos Simulation (Stress Testing):** A multi-processing Python script simulates high-traffic server spikes to test system resilience and monitor behavior under load.
4. **Analytics & Visualization (Power BI):** An enterprise-grade dashboard aggregates the time-series logs, calculates dynamic metrics using **DAX**, and fires conditional visual alerts when resources hit critical thresholds.

## Tech Stack & Tools
* **Programming Language:** Python 3.12
* **Core Libraries:** `psutil`, `multiprocessing`, `csv`, `time`
* **Analytics Platform:** Microsoft Power BI Desktop (DAX Expressions)
* **Target Cloud Infrastructure (Planned):** AWS (EC2 Instances & RDS Databases)

## Key Metrics Calculated ( using DAX)
* **Average CPU Utilization:** `Avg_CPU = AVERAGE(server_logs[CPU_Usage_Percent])`
* **Max CPU Peak:** `Max_CPU_Peak = MAX(server_logs[CPU_Usage_Percent])`
* **High Load Duration %:** Custom ratio tracking percentage of time where the server load crossed critical limits (>70%).

## How to Run the Project
1. Clone this repository directory.
2. Activate your virtual environment and install dependencies:
   ```bash
   pip install psutil
