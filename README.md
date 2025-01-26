# Weather Data ETL Pipeline

This project demonstrates an ETL (Extract, Transform, Load) pipeline that fetches weather data from the **Weatherstack API**, processes it, and stores it in a CSV file for analysis. The pipeline extracts the current weather information such as temperature and weather description for a specified city, then appends it to a report with a timestamp.

## Features
- Fetches real-time weather data for a specified city (default is London).
- Processes the fetched data to extract relevant weather information.
- Saves the processed data to a CSV file (`weather_report.csv`).
- Data is appended with a timestamp after each pipeline run.

## Requirements
- Python 3.x
- `requests` library

You can install the required library by running:

```bash
pip install requests
