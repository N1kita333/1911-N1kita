import sqlite3

connection = sqlite3.connect("database.s13", 5)
cur = connection.cursor()

#cur.execute("create table users (id int primary key not null, login text, password text);")
#cur.execute("insert into users (id, login, password) values (2, 'nikita', 'admin');")
cur.execute("select login, password from users;")
connection.commit()
res = cur.fetchall()
print(res)


#print(connection)
#print(cur)

connection.close()
