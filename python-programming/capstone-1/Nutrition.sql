PRAGMA foregin_keys = ON;

CREATE TABLE IF NOT EXISTS Foodbank (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Food_Name  TEXT NOT NULL,
    Category TEXT Not NULL, 
    Protein REAL,
    Zinc REAL,
    Calcium REAL,
    Vitamin_A REAL, 
    Vitamin_B REAL,
    Iron REAL, 
    Carbs REAL,
    Fiber REAL,
    Fat REAL,
    Energy REAL,
    Benefit TEXT
);

CREATE TABLE IF NOT EXISTS User_log (
    Id INTEGER   PRIMARY KEY AUTOINCREMENT,
    Foodbank_id INTEGER,
    Quantity REAL NOT NULL, 

    FOREIGN KEY (Foodbank_id)
    REFERENCES Foodbank(Id)

 )
 


SELECT FROM foodbank WHERE food = ?, (food_name)

