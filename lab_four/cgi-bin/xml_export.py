import sqlite3 as sq
import xml.dom.minidom

conn = sq.connect('space_db.db')
cur = conn.cursor()

cur.execute('select * from stars')
stars = cur.fetchall()
cur.execute('select * from supernovas')
supernovas = cur.fetchall()
cur.execute('select * from blackholes')
blackholes = cur.fetchall()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
    <html>
        <head>
            <meta charset = "UTF-8">
            <title>Data</title>
        </head>
        <h1> Data import successful </h1>""")

doc = xml.dom.minidom.Document()

root = doc.createElement('space')
doc.appendChild(root)

stars_list = doc.createElement('stars')
root.appendChild(stars_list)
for star in stars:
    star_elem = doc.createElement('stars')
    star_elem.setAttribute('star_id', str(star[0]))
    star_elem.setAttribute('name_of_star', star[1])
    star_elem.setAttribute('weight', str(star[2]))
    stars_list.appendChild(star_elem)

sn_list = doc.createElement('supernovas')
root.appendChild(sn_list)
for supernova in supernovas:
    sn_elem = doc.createElement('supernovas')
    sn_elem.setAttribute('supernova_id', str(supernova[0]))
    sn_elem.setAttribute('name_of_supernova', supernova[1])
    sn_elem.setAttribute('age', str(supernova[2]))
    sn_list.appendChild(sn_elem)

bh_list = doc.createElement('blackholes')
root.appendChild(bh_list)
for blackhole in blackholes:
    bh_elem = doc.createElement('blackholes')
    bh_elem.setAttribute('bh_id', str(blackhole[0]))
    bh_elem.setAttribute('bh_name', blackhole[1])
    bh_elem.setAttribute('density', str(blackhole[2]))
    bh_elem.setAttribute('star_id', str(blackhole[3]))
    bh_elem.setAttribute('supernova_id', str(blackhole[4]))
    bh_list.appendChild(bh_elem)

with open('D:\\USERS\\DIMA\\PycharmProjects\\lab_four\\book.xml', 'w') as f:
    f.write(doc.toprettyxml())

cur.close()
conn.close()
