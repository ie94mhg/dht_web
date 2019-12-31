import pymysql
import sys

# Open database connection
db = pymysql.connect("versa.dbaremoto.com.mx","raspberry_user","89288-a","raspberry" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
sql = "INSERT INTO rp1_DHT_Data_1 VALUES(now(),1,1)"
cursor.execute(sql)
db.commit();

cursor.execute("SELECT * FROM rp1_DHT_Data_1")
rows = cursor.fetchall()
print ("\nContenido en la base de datos:\n")
for row in rows:
	print("{0} {1} {2}".format(row[0], row[1], row[2]))
# disconnect from server
db.close()
