import mysql.connector
con=mysql.connector.connect(host='18.219.99.141',database="db1",user="root",password='India12345')
c=con.cursor()
def create_table():
   c.execute('create table asr_employee(idno varchar(10),name varchar(20),salary varchar(10))')
def insert_table():
   c.execute("insert into asr_employee values('17191231','Asritha',50000)")
   c.execute("insert into asr_employee values('17191232','Avinash',60000)")
   c.execute("insert into asr_employee values('17191233','yamini',70000)")
   c.execute("insert into asr_employee values('17191235','srija',80000)")
   c.execute("insert into asr_employee values('17191236','yamini',70000)")
   con.commit()
def select_table():
   c.execute('select * from asr_employee')
   data=c.fetchall()
   for row in data:
      print(row)
def delete_row():
   c.execute("delete from asr_employee where idno=17191236")
def update_row():
   c.execute("update asr_employee set idno='17191234' where idno='17191235'")
#create_table()
insert_table()
update_row()
delete_row()
select_table()
c.close()
con.close()
