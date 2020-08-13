#persons
import mysql.connector
con=mysql.connector.connect(host='18.219.99.141',database="db1",user="root",password='India12345')
c=con.cursor()
def create_table():
   c.execute('create table asr_person(name varchar(10),dob varchar(20),address varchar(10),pannum varchar(20))')
def insert_table():
   c.execute("insert into asr_person values('asritha',16-06-00,'213-15A','FYHJY2345Y')")
   c.execute("insert into asr_person values('divya',17-07-00,'214-73B','FAYDH2564D')")
   c.execute("insert into asr_person values('yamini',18-08-00,'234-34C','FSJHD2457F')")
   c.execute("insert into asr_person values('srija',19-09-00,'324-43D','FSHYE2463G')")
   c.execute("insert into asr_person values('nandu',20-10-00,'344-67F','FSDFG2343G')")
   con.commit()
def select_table():
   c.execute('select * from asr_person')
   data=c.fetchall()
   for row in data:
      print(row)
def delete_row():
   c.execute("delete from asr_person where name='divya'")
def update_row():
   c.execute("update asr_person set address='231-25H' where name='asritha'")
#create_table()
insert_table()
delete_row()
update_row()
select_table()
c.close()
con.close()
