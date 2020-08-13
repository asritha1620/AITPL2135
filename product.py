import mysql.connector
con=mysql.connector.connect(host='18.219.99.141',database="db1",user="root",password='India12345')
c=con.cursor()
def create_table():
   c.execute('create table asr_product(idno varchar(10),name varchar(20),description varchar(10),prize varchar(10))')
def insert_table():
   c.execute("insert into asr_product values('A2S4FD3','lenovo320e notebook','4gb RAM','29k')")
   c.execute("insert into asr_product values('A2S4FD4','dell3567 notebook','3gb RAM','33k')")
   c.execute("insert into asr_product values('A2S4FD5','Redmi Note9 pro','64gb','17k')")
   c.execute("insert into asr_product values('A2S4FD6','Reebok','digital','1000')")
   con.commit()
def select_table():
   c.execute('select * from asr_product')
   data=c.fetchall()
   for row in data:
      print(row)
def delete_row():
   c.execute("delete from asr_product where name='Reebok'")
def update_row():
   c.execute("update asr_product set description='4gb RAM' where idno='A2S4FD4'")
#create_table()
insert_table()
delete_row()
update_row()
select_table()
c.close()
con.close()
#create table asritha_employee (columns:empid,empname,salary,5 rows,perform select,update,delete operations)
#create asritha_person table colum