import xml.dom.minidom
import back_db as db

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
    <html>
        <head>
            <meta charset = "UTF-8">
            <title>Data</title>
        </head>
        <h1> Data import successful </h1>""")

doc = xml.dom.minidom.parse('book.xml')
stars = doc.getElementsByTagName('star')
supernovas = doc.getElementsByTagName('supernova')
blackholes = doc.getElementsByTagName('blackhole')

for star in stars:
    db.insert_in_stars(star.getAttribute('name_of_star'), star.getAttribute('weight'))

for supernova in supernovas:
    db.insert_in_supernovas(supernova.getAttribute('name_of_supernova'), supernova.getAttribute('age'))

for blackhole in blackholes:
    db.insert_in_blackholes(blackhole.getAttribute('bh_name'), blackhole.getAttribute('density'),
                            blackhole.getAttribute('star_id'), blackhole.getAttribute('supernova_id'))

