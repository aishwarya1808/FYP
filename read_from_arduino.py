from with_rules_method import average_consumption_calc
import serial
import time
import pymongo
import json
from datetime import datetime
import re



myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test1"]
mycol = mydb["sensor_data"]

ser=serial.Serial('COM12',9600)   
data =[]                       # empty list to store the data
for i in range(5):
    b = ser.readline()         # read a byte string
    string_n = b.decode()  # decode byte string into Unicode  
    string = string_n.rstrip() # remove \n and \r
    l=string.split("=")
    if(l[0]=="No object in sight voltage"):
        str1="No"
    else:
        str1="Yes"
    mydict={"value":l[1] , "date":datetime.today() , "ir":str1}
    
    x = mycol.insert_one(mydict)
    time.sleep(0.1)            # wait (sleep) 0.1 seconds
ser.close()

mycol=mydb["sensor_data"]
myquery={"date":datetime.today() , "ir":"No"}
mydoc = mycol.find(myquery)

val=[]
dat=[]
#val= mycol.find({},{"date":datetime.today() , "ir":"Yes"}).sort('_id',-1).limit(5);
val= mycol.find({},{"value":1 , "ir":"No","_id":0,"ir":0}).sort('_id',-1).limit(15);
    #val.append(x)
for i in val:
    #print(i)
    txt=str(i)
    x=re.findall("[-+]?([0-9]*\.[0-9]+|[0-9]+)",txt)
    a=float("".join(x))
    dat.append(a)
sum1=0.0
#for x in dat:
#    sum1+=x
val1=0
val2=0
val3=0
val1=dat[0]+dat[1]+dat[3]+dat[4]+dat[5]
val2=dat[6]+dat[7]+dat[8]+dat[9]+dat[10]
val3=dat[11]+dat[12]+dat[13]+dat[14]+dat[15]

ans1=average_consumption_calc(val1,5.0)
ans2=average_consumption_calc(val2,5.0)
ans3=average_consumption_calc(val3,5.0)

print("Average consumption between 10AM and 12PM = ",ans1)
print("Average consumption between 2PM and 4PM = ",ans2)
print("Average consumption between 8PM and 10PM = ",ans3)

if(ans1>=ans2 or ans1>=ans3):
    print("Average consumption of light bulb between 10AM and 12PM was at its highest. There was no one around during this period. Usage could be monitored.")
    
elif(ans2>=ans1 or ans2>=ans3):
    print("Average consumption of light bulb between 2PM and 4PM was at its highest. There was no one around during this period. Usage could be monitored.")
    
else:
    print("Average consumption of light bulb between 8PM and 10PM was at its highest. Unused light bulbs could be switched off.")