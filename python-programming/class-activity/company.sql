-- SQLite

PRAGMA foreign_keys = ON;


CREATE TABLE Employee (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    First_name TEXT NOT NULL,
    Second_name TEXT NOT NULL,
    Department_id INTEGER,

    FOREIGN KEY (Department_id) REFERENCES Department (Id)

);

CREATE TABLE Department (
    Id INTEGER PRIMARY KEY  AUTOINCREMENT,
    Name TEXT NOT NULL
)

INSERT INTO Department(Name)
VALUES 
    ("Data Science"),
    ("Software"),
    ("Project Management")

INSERT OR IGNORE INTO Employee(First_name,Second_name, Department_Id)
VALUES
    ("John","Chinaman",  1),
    ("mark", "bossman",  2),
    ("mary", "chaplin",  1),
    ("diana", "nilote",  1),
    ("moses", "darungo", 1)


