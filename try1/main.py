import os
import sqlite3
import sqlite3 as sq



db_path = 'C:/Users/s0160123/Desktop/lab_four'
db_file = 'space_db.db'
full_path = os.path.join(db_path, db_file)
conn = sqlite3.connect(full_path)
cur = conn.cursor()
cur.executescript('''DROP TABLE IF EXISTS stars; DROP TABLE IF EXISTS supernovas; DROP TABLE IF EXISTS blackholes''')

cur.execute("""CREATE TABLE IF NOT EXISTS stars (
        star_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_of_star TEXT, 
        weight INTEGER
        )""")

cur.execute("""CREATE TABLE IF NOT EXISTS supernovas (
            supernova_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name_of_supernova TEXT, 
            age INTEGER
            )""")

cur.execute("""CREATE TABLE IF NOT EXISTS blackholes (
            bh_id INTEGER PRIMARY KEY AUTOINCREMENT,
            bh_name TEXT,
            density INTEGER,
            star_id INTEGER,
            supernova_id INTEGER,
            FOREIGN KEY (star_id) REFERENCES stars(star_id),
            FOREIGN KEY (supernova_id) REFERENCES supernovas(supernova_id)
        )""")
conn.commit()
conn.close()


def insert_in_stars(name_of_star, weight):
    conn = sq.connect('space_db.db')
    cur = conn.cursor()
    cur.execute(f"""
        INSERT INTO stars (name_of_star, weight) values ('{name_of_star}','{weight}')
         """)
    conn.commit()
    conn.close()


def insert_in_supernovas(name_of_supernova, age):
    conn = sq.connect('space_db.db')
    cur = conn.cursor()
    cur.execute(f"""
            INSERT INTO supernovas (name_of_supernova, age) values ('{name_of_supernova}','{age}')
             """)
    conn.commit()
    conn.close()


def insert_in_blackholes(bh_name, density, star_id, supernova_id):
    conn = sq.connect('space_db.db')
    cur = conn.cursor()
    cur.execute(f"""
        INSERT INTO blackholes (bh_name, density, star_id, supernova_id) 
        values ('{bh_name}','{density}', '{star_id}', {supernova_id})
         """)
    conn.commit()
    conn.close()


def find_id_by_name_in_stars(name_of_star):
    conn = sq.connect('space_db.db')
    cur = conn.cursor()
    cur.execute(f"""
        SELECT star_id FROM stars st where st.name_of_star = '{name_of_star}'  
         """)
    tmp_for_return = cur.fetchone()
    conn.close()
    return tmp_for_return[0] if tmp_for_return is not None else 'not in base'


def find_id_by_name_in_supernovas(name_of_supernova):
    conn = sq.connect('space_db.db')
    cur = conn.cursor()
    cur.execute(f"""
        SELECT supernova_id FROM supernovas sn where sn.name_of_supernova = '{name_of_supernova}'  
         """)
    tmp_for_return = cur.fetchone()
    conn.close()
    return tmp_for_return[0] if tmp_for_return is not None else 'not in base'


def selects_from_database():
    conn = sq.connect('space_db.db')
    cur = conn.cursor()

    #Запрос на выборку имен черных дыр, имен звезд и возраста связанных с ними сверхновых:
    cur.execute('''SELECT b.bh_name, s.name_of_star, sn.age 
    FROM blackholes b 
    JOIN stars s ON b.star_id = s.star_id 
    JOIN supernovas sn ON b.supernova_id = sn.supernova_id;''')
    print(cur.fetchall())

    #Запрос на выборку имен звезд и черных дыр, у которых общая плотность выше 5:
    cur.execute('''SELECT s.name_of_star, b.bh_name 
    FROM stars s 
    JOIN blackholes b ON s.star_id = b.star_id 
    WHERE s.weight / b.density > 5;''')
    print(cur.fetchall())

    #Запрос на выборку имен звезд, для которых не существует связанных черных дыр:
    cur.execute('''SELECT s.name_of_star 
    FROM stars s 
    LEFT JOIN blackholes b ON s.star_id = b.star_id 
    WHERE b.bh_id IS NULL;''')
    print(cur.fetchall())
    conn.close()


insert_in_stars("Star1", 12)
insert_in_stars("Star2", 6)
insert_in_stars("Star3", 1)
insert_in_supernovas("Supernova1", 0)
insert_in_supernovas("Supernova1", 100)
insert_in_supernovas("Supernova1", 25)
insert_in_blackholes("BH 1", 1000, 1, 2)
insert_in_blackholes("BH 2", 1025, 2, 1)
insert_in_blackholes("BH 3", 100, None, None)
selects_from_database()