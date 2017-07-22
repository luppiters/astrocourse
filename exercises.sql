#adding stars
Insert into Star (kepler_id, t_eff, radius) values
(7115384, 3789, 27.384),
(8106973, 5810, 0.811),
(9391817, 6200, 0.958);

#a messed up table
update Planet
set kepler_name = NULL
where not status = 'CONFIRMED' ;

delete from Planet
where (radius < 0);

#make your own table
CREATE TABLE Planet (
  kepler_id INTEGER NOT NULL,
  koi_name VARCHAR(15) NOT NULL UNIQUE,
  kepler_name VARCHAR(15),
  status VARCHAR(20) NOT NULL,
  radius FLOAT NOT NULL
);

insert into Planet VALUES 
  (6862328,'K00865.01','', 'CANDIDATE',119.021),
  (10187017,'K00082.05','Kepler-102 b','CONFIRMED',5.286),
  (10187017,'K00082.04','Kepler-102 c','CONFIRMED',7.071);
  
#DIY EXOPLANET ARCHIVE
CREATE TABLE Star (
  kepler_id INTEGER PRIMARY KEY,
  t_eff INTEGER NOT NULL,
  radius FLOAT NOT NULL
  );
  
CREATE TABLE Planet (
  kepler_id INTEGER REFERENCES Star (kepler_id),
  koi_name VARCHAR(20) PRIMARY KEY,
  kepler_name VARCHAR(20),
  status VARCHAR(20) NOT NULL,
  period FLOAT,
  radius FLOAT,
  t_eq INTEGER
);

COPY Star FROM 'stars.csv' CSV;
COPY Planet FROM 'planets.csv' CSV;

#star coordinates
TRUNCATE TABLE Star;
ALTER TABLE Star
ADD COLUMN ra FLOAT,
ADD COLUMN decl FLOAT;

COPY Star FROM 'stars_full.csv' CSV;
