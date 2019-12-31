import time
import pymysql
import sys
import Adafruit_DHT

<<<<<<< HEAD
sampleFreq = 2 # time in seconds
=======
# Open database connection
db = pymysql.connect("versa.dbaremoto.com.mx","raspberry_user","password","raspberry" )
>>>>>>> d9fadb332fb9d7fb9c2e97cf1ec3dad9e2faf753

# get data from DHT sensor
def getDHTdata():	
	DHT22Sensor = Adafruit_DHT.DHT22
	DHTpin = 17
	hum, temp = Adafruit_DHT.read_retry(DHT22Sensor, DHTpin)
	
	if hum is not None and temp is not None:
		hum = round(hum,1)
		temp = round(temp, 1)
		logData (temp, hum)

# log sensor data on database
def logData (temp, hum):	
    db = pymysql.connect("192.168.1.105","raspberry_user","password","raspberry")
    cursor=db.cursor()
    #cursor.execute("INSERT INTO rp1_DHT_Data_1 values(datetime('now'), (?), (?))", (temp, hum))
    cursor.execute("INSERT INTO rp1_DHT_Data_1 values(now(), (%s), (%s))", (temp, hum))
    db.commit()
    db.close()

# display database data
def displayData():
    db = pymysql.connect("192.168.1.105","raspberry_user","password","raspberry" )
    cursor=db.cursor()
    cursor.execute("SELECT * FROM rp1_DHT_Data_1")
    rows = cursor.fetchall()
    print ("\nContenido en la base de datos:\n")
    for row in rows:
        print("{0} {1} {2}".format(row[0], row[1], row[2]))
    db.close()

# main function
def main():
	for i in range (0,3):
		getDHTdata()
		time.sleep(sampleFreq)
	displayData()
# Execute program 
main()
