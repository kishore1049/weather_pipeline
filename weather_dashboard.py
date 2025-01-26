import streamlit as st
import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect('weather_data.db')
query = "SELECT * FROM weather ORDER BY timestamp DESC LIMIT 10"
data = pd.read_sql(query, conn)

# Streamlit App
st.title("Weather Data Dashboard")
st.write("Latest Weather Data:")
st.dataframe(data)

# Temperature Trend
st.line_chart(data['temperature'])
