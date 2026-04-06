import sqlite3
import pandas as pd
import streamlit as st

st.set_page_config(page_title="UberEats DashBoard", layout="wide")
st.title("🍔 Multi-Filter Uber Eats Data")

try:
    conn = sqlite3.connect('ubereats_data.db')
    
    # 1. Fetch available columns
    cols_df = pd.read_sql_query("PRAGMA table_info(restaurants)", conn)
    column_list = [col for col in cols_df['name'].tolist() if col != 'restaurant_id']

    # --- Sidebar Filters ---
    st.sidebar.header("Filter Settings")
    # Allow users to pick which columns they want to filter by
    selected_columns = st.sidebar.multiselect("1. Select Columns to Filter", column_list)

    filters = {}
    for col in selected_columns:
        # Get unique values for each selected column
        val_query = f"SELECT DISTINCT \"{col}\" FROM restaurants WHERE \"{col}\" IS NOT NULL"
        unique_vals = pd.read_sql_query(val_query, conn)[col].tolist()
        
        # User picks specific values for that column
        chosen_vals = st.sidebar.multiselect(f"Values for {col}", unique_vals)
        if chosen_vals:
            filters[col] = chosen_vals

    # --- Dynamic Query Building ---
    query = "SELECT * FROM restaurants"
    params = []

    if filters:
        conditions = []
        for col, values in filters.items():
            # Creates 'column IN (?, ?, ?)' syntax for each filter
            placeholders = ", ".join(["?"] * len(values))
            conditions.append(f"\"{col}\" IN ({placeholders})")
            params.extend(values)
        
        query += " WHERE " + " AND ".join(conditions)

    # --- Display ---
    left, middle, right = st.columns([1, 10, 1])

    with middle:
        df_result = pd.read_sql_query(query, conn, params=params)
        st.write(f"Showing **{len(df_result)}** results")
        st.dataframe(df_result, use_container_width=True)

    conn.close()

except Exception as e:
    st.error(f"Error: {e}")
