#cars
import mysql.connector
con=mysql.connector.connect(host='18.219.99.141',database="db1",user="root",password='India12345')
c=con.cursor()
def create_table():
   c.execute('create table asr_cars(manufacturer varchar(20),carname varchar(10),prize varchar(20) )')
def insert_table():
   c.execute("insert into asr_cars values('Mercedes Benz','v-class','1.1c')")
   c.execute("insert into asr_cars values('Maruti Suzuki','presso','5.14l')")
   c.execute("insert into asr_cars values('Audi','audiA8','1.56c')")
   c.execute("insert into asr_cars values('Mercedes Benz','GLE','1.25c')")
   c.execute("insert into asr_cars values('Mercedes Benz','GLC','57.75c')")
   con.commit()
def select_table():
   c.execute('select * from asr_cars')
   data=c.fetchall()
   for row in data:
      print(row)
def delete_row():
   c.execute("delete from asr_cars where prize='5.14l'")
def update_row():
   c.execute("update asr_cars set prize='56c' where prize='57.75c'")
#create_table()
insert_table()
update_row()
delete_row()
select_table()
c.close()
con.close()
