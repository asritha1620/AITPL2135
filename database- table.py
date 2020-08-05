import sqlite3
a=sqlite3.connect('as1.db')
c=a.cursor()
try:
    c.execute("create table employee(id integer PRIMARY KEY,mname text,lname text)")
except:
    pass
some = [('asritha', 'mallineni'), ('avinash', 'iyer'),('yamini', 'bollineni')]
c.executemany("insert into employee (mname,lname) values(?,?)",some)
a.commit()
c.execute('select * from employee')
print(c.fetchall())
c.close()
a.close()

