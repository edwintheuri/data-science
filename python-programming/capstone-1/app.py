import sqlite3 as s
import re
import streamlit as st

def mapper(db_access, food):

    db_access.execute("SELECT id FROM foodbank WHERE name = ?", (food,)) 
    fetch_data = db_access.fetchone()
    if fetch_data:
        return fetch_data[0]
    return None

db_connect = s.connect("nutrition.db")

db_access = db_connect.cursor()

db_access.execute('''
                  CREATE TABLE IF NOT EXISTS foodbank(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL UNIQUE,
                  protein REAL, 
                  zinc REAL, 
                  iron REAL,
                  energy REAL
                  )
                ''')

db_access.execute('''
                  CREATE TABLE IF NOT EXISTS user_logs(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  foodbank_id REAL,
                  quantity REAL,

                  FOREIGN KEY (foodbank_id)
                  REFERENCES foodbank(id)
                  )
                ''')

clean_data_store = []
user_data = st.text_input("What did you eat today ? ")

if st.button('Analyze'):
    split_data = re.split(r",|\band\b", user_data)
     

    for items in split_data:

        items = items.strip().lower()
        if items:
            matching_data = re.match(r"(\d+)?\s*(.*)", items)

            qty = matching_data.group(1) if matching_data.group(1) else 1
            food = matching_data.group(2).lower()

            food_id = mapper(db_access, food) 

            if food_id:
                clean_data_store.append((qty, food))
                
st.write(clean_data_store)




