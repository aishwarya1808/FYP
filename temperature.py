from with_rules_method import average_consumption_fan_calc
import serial
import time
import pymongo
import json
from datetime import datetime
import re
pwd = "cloudnine"
import smtplib


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test1"]
mycol = mydb["sensor_data_fan"]

ser=serial.Serial('COM9',9600)   
data =[]                       # empty list to store the data
for i in range(5):
    b = ser.readline()         # read a byte string
    string_n = b.decode()  # decode byte string into Unicode  
    string = string_n.rstrip() # remove \n and \r
    l=string.split(" ")
    mydict={"value":l[1] , "date":datetime.today() , "temp":l[0],"ir":l[2]}
    
    x = mycol.insert_one(mydict)
    time.sleep(0.1)            # wait (sleep) 0.1 seconds
ser.close()

mycol=mydb["sensor_data_fan"]
myquery={"date":datetime.today() , "ir":"No"}
mydoc = mycol.find(myquery)

val=[]
val1=[]
dat=[]
dat1=[]
#val= mycol.find({},{"date":datetime.today() , "ir":"Yes"}).sort('_id',-1).limit(5);
#val= mycol.find({},{"value":1 ,"_id":0}).sort('_id',-1).limit(15);
val1=mycol.find({},{"temp":1 ,"_id":0}).sort('_id',-1).limit(15);
    #val.append(x)
for i in val1:
    #print(i)
    txt=str(i)
    x=re.findall("[-+]?([0-9]*\.[0-9]+|[0-9]+)",txt)
    
    dat.append(float("".join(x[0])))
    #print(dat)


val1=0
val2=0
val3=0

val1=dat[0]+dat[1]+dat[2]+dat[3]+dat[4]
val2=dat[5]+dat[6]+dat[7]+dat[8]+dat[9]
val3=dat[10]+dat[11]+dat[12]+dat[13]+dat[14]


ans1=average_consumption_fan_calc(val1,5.0)
ans2=average_consumption_fan_calc(val2,5.0)
ans3=average_consumption_fan_calc(val3,5.0)

print("Average temperature between 10AM and 12PM = ",ans1)
print("Average temperature between 2PM and 4PM = ",ans2)
print("Average temperature between 8PM and 10PM = ",ans3)

server = smtplib.SMTP('64.233.184.108',587)
server.ehlo()
server.starttls()
server.login("aishwarya.sripathy@gmail.com",pwd)

if(int(ans1)>=int(ans2) or int(ans1)>=int(ans3)):
    print("The Fan was working between 10AM and 12PM. The average temperature was at its highest during this period. So 'Consumption was optimum'.")
    
elif(int(ans2)>=int(ans1) or int(ans2)>=int(ans3)):
    print("The Fan was working between 2PM and 4PM. The average temperature was at its highest during this period. So 'Consumption was optimum'.")

else:
    print("The Fan was working between 8PM and 10PM. Recorded average room temperature during this period was low. The usage of fan between 8PM and 5AM could be optimized.")


