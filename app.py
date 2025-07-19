import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Face Attendance System", layout="centered")

st.title("📸 Face Recognition Attendance System")
st.write("This page shows today's attendance records.")


# Ensure Attendance folder exists
if not os.path.exists("Attendance"):
    os.makedirs("Attendance")


# Get today's date
date = datetime.now().strftime("%d-%m-%Y")
csv_file_path = f"Attendance/Attendance_{date}.csv"


# Display attendance if exists
if os.path.exists(csv_file_path):
    df = pd.read_csv(csv_file_path)
    st.success(f"Attendance for {date} found.")
    st.dataframe(df.style.highlight_max(axis=0))
else:
    st.warning(f"No attendance data available for {date} yet.")
    st.write("Run your `attendance.py` to record attendance first.")


# Optional: Show attendance history
if st.checkbox("Show all attendance files"):
    attendance_files = [f for f in os.listdir("Attendance") if f.endswith(".csv")]
    if attendance_files:
        selected_file = st.selectbox("Choose a file", attendance_files)
        df = pd.read_csv(f"Attendance/{selected_file}")
        st.write(f"Showing: `{selected_file}`")
        st.dataframe(df.style.highlight_max(axis=0))
    else:
        st.info("No attendance files available yet.")

