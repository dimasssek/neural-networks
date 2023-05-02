import os
import sqlite3

db_path = 'C:/Users/s0160123/Desktop/lab_four'
db_file = 'db01.db'
full_path = os.path.join(db_path, db_file)
con = sqlite3.connect(full_path)
cur = con.cursor()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
    <html>
        <head>
            <meta charset = "UTF-8">
            <title>Data</title>
        </head>
    <body>""")
print("<h1>Tables Data</h1>")

cur.execute('''SELECT * FROM stars''')
a = cur.fetchall()
print("<table>")
print("<th> id </th>")
print("<th> name </th>")
print("<th> weight </th>")
for i in range(len(a)):
    print("<tr> ")
    for j in range(len(a[i])):
        print("<td> %s </td>" % a[i][j])
    print("</tr>")
print("</table>")

cur.execute('''SELECT * FROM supernovas''')
a = cur.fetchall()
print("<table>")
print("<th> id </th>")
print("<th> name </th>")
print("<th> age </th>")
for i in range(len(a)):
    print("<tr> ")
    for j in range(len(a[i])):
        print("<td> %s </td>" % a[i][j])
    print("</tr>")
print("</table>")

cur.execute('''SELECT * FROM blackholes''')
a = cur.fetchall()
print("<table>")
print("<th> bh_id </th>")
print("<th> name </th>")
print("<th> density </th>")
print("<th> star_id </th>")
print("<th> supernova_id </th>")
for i in range(len(a)):
    print("<tr> ")
    for j in range(len(a[i])):
        print("<td> %s </td>" % a[i][j])
    print("</tr>")
print("</table>")
print("""</body> </html>""")

cur.close()
con.close()