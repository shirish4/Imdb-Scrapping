import pymysql
EMAIL_ADDRESS='showreminder63@gmail.com'
PASSWORD='rem_show'
receiver_addr=input("Enter receiver's Email id:")
show=input("Enter your shows:")
l=show.split(',')

db = pymysql.connect(
  host="localhost",
  user="root",
  passwd="root",
)
c=db.cursor()
c.execute("CREATE DATABASE IF NOT EXISTS data")
c.execute("USE data")
c.execute("CREATE TABLE IF NOT EXISTS input_info(email_id VARCHAR(255),shows VARCHAR(255))")
#c.execute("SELECT *  FROM input_info")
try:
    c.execute("""INSERT INTO input_info VALUES (%s,%s)""",(receiver_addr,show))
    db.commit()
except:
    db.rollback()
#print(c.rowcount, "record inserted.")