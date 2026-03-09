import sqlite3

conn = sqlite3.connect("database.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
email TEXT,
password TEXT
)
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS ocean_data(
id INTEGER PRIMARY KEY AUTOINCREMENT,
location TEXT,
temperature REAL,
species TEXT
)
""")

conn.execute("""INSERT INTO ocean_data (location, temperature, species) VALUES
('Indian Ocean',27.5,'Tuna'),
('Pacific Ocean',26.8,'Dolphin'),
('Atlantic Ocean',24.2,'Blue Whale'),
('Arabian Sea',28.1,'Sardine'),
('Bay of Bengal',29.0,'Hilsa'),
('Southern Ocean',4.5,'Antarctic Krill'),
('Coral Sea',26.3,'Coral Trout'),
('Gulf of Mexico',27.2,'Red Snapper'),
('North Sea',12.6,'Cod'),
('Mediterranean Sea',23.4,'Octopus'),
('Tasman Sea',22.7,'Shark'),
('Caribbean Sea',28.3,'Sea Turtle'),
('Bering Sea',6.1,'Pollock'),
('Baltic Sea',10.4,'Herring'),
('Andaman Sea',28.9,'Clownfish'),
('Philippine Sea',27.6,'Mackerel'),
('Red Sea',30.2,'Reef Fish'),
('Labrador Sea',7.8,'Seal'),
('Weddell Sea',-1.2,'Penguin'),
('South China Sea',28.4,'Grouper'),
('Gulf of Aden',29.1,'Barracuda'),
('Black Sea',15.3,'Anchovy'),
('Sargasso Sea',25.7,'Eel'),
('East China Sea',24.8,'Squid'),
('Sea of Japan',18.6,'Salmon'),
('Hudson Bay',2.5,'Beluga Whale'),
('Barents Sea',5.9,'Arctic Cod'),
('Timor Sea',27.9,'Snapper'),
('Java Sea',28.5,'Flying Fish'),
('Arafura Sea',28.1,'Prawn'),
('Norwegian Sea',8.7,'Minke Whale'),
('Greenland Sea',3.2,'Narwhal'),
('Scotia Sea',2.9,'Antarctic Krill'),
('Chukchi Sea',1.5,'Walrus'),
('Celebes Sea',28.7,'Tuna'),
('Banda Sea',28.2,'Reef Shark'),
('Yellow Sea',20.4,'Jellyfish'),
('Gulf of California',26.5,'Sea Lion'),
('Mozambique Channel',27.8,'Whale Shark'),
('Great Australian Bight',19.3,'Lobster');""")

conn.commit()
conn.close()

print("Database Ready")