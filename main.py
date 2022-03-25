import sqlite3

conn = sqlite3.connect('Hospital.db')
c = conn.cursor()

# 1 Adding the patients details into table
'''
c.execute("""CREATE TABLE patients_mang(patCode int,
                 name text,
                 phone int,
                 addCity text) """)
print("Table Created")
'''

many_patients = [(1, 'Rohan Patil', 12345678, 'Pune'),
                 (19, 'Sameer Rao', 12345679, 'Mumbai'),
                 (109, 'Peter Parker', 98676532, 'Nasik'),
                 ]
c.executemany("INSERT INTO patients_mang VALUES(?,?,?,?)", many_patients)
# print("Executed Successfully")

c.execute("SELECT * FROM patients_mang")
items = c.fetchall()
for item in items:
    print(items)
conn.commit()
conn.close()
