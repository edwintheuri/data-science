import sqlite3 as s
import re
import streamlit as st
import csv




#loads food names and their corresponding ids into a dictionary for quick lookup

def food_cache(db_access):
    db_access.execute("SELECT name, id FROM foodbank")
    return {row[0]: row[1] for row in db_access.fetchall()}


db_connect = s.connect("nutrition.db")
db_access = db_connect.cursor()

db_access.execute('''
                  CREATE TABLE IF NOT EXISTS foodbank(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL UNIQUE,
                  protein REAL, 
                  iron REAL, 
                  zinc REAL,
                  energy REAL
                  )
                ''')

db_access.execute('''
                  CREATE TABLE IF NOT EXISTS user_logs(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  foodbank_id INTEGER,
                  quantity REAL,

                  FOREIGN KEY (foodbank_id)
                  REFERENCES foodbank(id)
                  )
                ''')


with open("food.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        db_access.execute('''INSERT OR IGNORE INTO foodbank
                          (name,protein,iron,zinc,energy)
                          VALUES (?,?,?,?,?)
                          ''', (
                            row["name"].strip().lower(),
                            float(row["protein"]),
                            float(row["iron"]),
                            float(row["zinc"]),
                            float(row["energy"])
                            )
                            )
    db_connect.commit()

clean_data_store = []
total_protein = 0
total_iron = 0      
total_zinc = 0
total_energy = 0

baseline = {
    "protein": 50,
    "iron": 18,
    "zinc": 11,
    "energy": 2000
}

# parse input data and extract quantity and food name, 

user_data = st.text_input("What foods did you eat? (e.g., '2 eggs, beanrice, ndegurice and 3 slices of bread'):")


if st.button('Analyze'):
    if not user_data:
        st.warning("Please enter the foods you ate before clicking Analyze.")
        st.stop()

    food_id_map = food_cache(db_access)


    split_data = re.split(r",|\band\b", user_data)
     

    for items in split_data:

        items = items.strip().lower()
        if items:
            matching_data = re.match(r"(\d*\.?\d+)?\s*(.*)", items)

            qty = float(matching_data.group(1)) if matching_data.group(1) else 1
            food = matching_data.group(2).lower()

            food_id = food_id_map.get(food) #checks the food name against the cached dictionary food_cache() and retrieves the corresponding id 
        
            

            if food_id:
                clean_data_store.append((qty, food_id))
            
    for qty, food_id in clean_data_store:
        db_access.execute("SELECT protein, iron, zinc, energy FROM foodbank WHERE id = ?", (food_id,))
        nutrition = db_access.fetchone()
        if nutrition:
            protein, iron, zinc, energy = nutrition
            total_protein += protein * qty
            total_iron += iron * qty
            total_zinc += zinc * qty
            total_energy += energy * qty

    st.write("Your Nutrition summary"    )
    st.write(f"Protein:{total_protein}g ")
    st.write(f"Iron   :{total_iron}g ")
    st.write(f"Zinc   :{total_zinc}g ")
    st.write(f"Energy :{total_energy} kj ")


    results = {
        "protein": total_protein,
        "iron": total_iron,
        "zinc": total_zinc,
        "energy": total_energy

    }


    for nutrient, value in results.items():
        if value > baseline[nutrient]:
            st.write(f"The {nutrient} content of your meal is above the recommended level.")
        elif value < baseline[nutrient]:
            st.write(f"The {nutrient} content of your meal is below the recommended level.")
        else:
            st.write(f"The {nutrient} content of your meal is at the recommended level.")
