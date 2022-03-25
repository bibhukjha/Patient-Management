import sqlite3

conn = sqlite3.connect('Hospitals.db')
c = conn.cursor()

# 1 Adding the patients details into table
'''
c.execute("""CREATE TABLE patients_mangm(patCode int PRIMARY KEY,
                 name text,
                 phone int,
                 addCity text) """)
print("Table Created")
'''


insert_query = """INSERT INTO patients_mangm (patCode,name,phone,addCity) VALUES (1,'Rohan gavaskar', 12345678, 'Pune'),
                 (19, 'Sachin Tendulkar', 12345679, 'Mumbai'),
                 (109, 'Peter Parker', 98676532, 'Nasik')"""
c.execute(insert_query)
print('Data of the Patient table are:')
c.execute(''' SELECT rowid,* FROM patients_mangm ''')
items = c.fetchall()
for item in items:
    print(item)
conn.commit()
conn.close()
