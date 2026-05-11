CREATE DATABASE humanitarian_prog_db;

USE humanitarian_prog_db;


CREATE TABLE jurisdiction_hierarchy(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(30) NOT NULL UNIQUE,
    level VARCHAR(20) NOT NULL CHECK (level IN("county","sub_county","village")),
    parent VARCHAR(30) NULL,

    FOREIGN KEY (parent) REFERENCES jurisdiction_hierarchy(name) ON DELETE CASCADE

);

CREATE TABLE village_locations (
    village_id INTEGER PRIMARY KEY AUTOINCREMENT,
    village VARCHAR(30) NOT NULL UNIQUE,
    total_population INTEGER NOT NULL CHECK(total_population >=0),
    
    FOREIGN KEY (village) REFERENCES jurisdiction_hierarchy(name) ON DELETE CASCADE

);

CREATE TABLE beneficiary_partner_data (
    partner_id INTEGER PRIMARY KEY AUTOINCREMENT,
    partner VARCHAR(30) NOT NULL,
    village VARCHAR(30) NOT NULL, 
    beneficiaries INTEGER NOT NULL CHECK(beneficiaries >=0),
    beneficiary_type VARCHAR(30) NOT NULL CHECK(beneficiary_type IN ("individuals","households")),

    FOREIGN KEY (village) REFERENCES village_locations(village) ON DELETE CASCADE

); 


INSERT INTO jurisdiction_hierarchy (name, level, parent), 






