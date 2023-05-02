import cgi
import sqlite3
import os
import back_db as db

db_path = 'C:/Users/s0160123/Desktop/lab_four'
db_file = 'space_db.db'
full_path = os.path.join(db_path, db_file)
con = sqlite3.connect(full_path)
cur = con.cursor()

form = cgi.FieldStorage()
text1 = form.getfirst("Name", "Не задано")
text2 = form.getfirst("Weight", "Не задано")
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
    <html>
        <head>
            <meta charset = "UTF-8">
            <title>Patient handling</title>
        </head>
    <body>""")
print("<h1>Patient handling</h1>")
print("<p>Name: %s</p>"%text1)
print("<p>Weight: %s</p>"%text2)

if text1 == "Не задано" or text2 == "Не задано":
    print("<p> Неправильные данные</p>")
else:
    # db.insert_in_stars(text1, text2)
    a = (text1, text2)
    sql_insert = '''INSERT INTO stars(name_of_star, weight) VALUES(?,?);'''
    cur.execute(sql_insert, a)
    con.commit()
print("""</body> </html>""")

cur.close()
con.close()