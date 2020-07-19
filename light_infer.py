from with_rules_method import average_consumption_calc
import serial
import time
import pymongo
import json
from datetime import datetime
import re
import smtplib 

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test1"]
mycol = mydb["sensor_data"]

myquery={"date":datetime.today() , "ir":"No"}
mydoc = mycol.find(myquery)

val=[]
dat=[]
txt=""
#val= mycol.find({},{"date":datetime.today() , "ir":"Yes"}).sort('_id',-1).limit(5);
val= mycol.find({},{"value":1,"_id":0}).sort('_id',-1).limit(15);
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
val1=(dat[0]+dat[1]+dat[2]+dat[3]+dat[4])
val2=(dat[5]+dat[6]+dat[7]+dat[8]+dat[9])
val3=(dat[10]+dat[11]+dat[12]+dat[13]+dat[14])

ans1=average_consumption_calc(val1,5.0)
ans2=average_consumption_calc(val2,5.0)
ans3=average_consumption_calc(val3,5.0)


vol1=(ans1/1024.0)*5000
cur1=(vol1-2500)/66
watt1=((vol1*cur1))/100000

vol2=(ans2/1024.0)*5000
cur2=(vol2-2500)/66
watt2=((vol2*cur2))/100000

vol3=(ans3/1024.0)*5000
cur3=(vol3-2500)/66
watt3=((vol3*cur3))/100000

print("Average consumption between 10AM and 12PM = ",watt1)
print(" watt")
print("Average consumption between 2PM and 4PM = ",watt2)
print(" watt")
print("Average consumption between 8PM and 10PM = ",watt3)
print(" watt")
print("\n Inference: ")
str1="Average consumption between 10AM and 12PM = "+str(watt1)+" watt\nAverage consumption between 2PM and 4PM = "+str(watt2)+" watt\nAverage consumption between 8PM and 10PM = "+str(watt3)+" watt"
str2=""
if(watt1>=watt2 or watt1>=watt3):
    print("Average consumption of light bulb between 10AM and 12PM was at its highest. There was no one around during this period. Usage could be monitored.")
    str2="\nAverage consumption of light bulb between 10AM and 12PM was at its highest. There was no one around during this period. Usage could be monitored."
    
elif(watt2>=watt1 or watt2>=watt3):
    print("Average consumption of light bulb between 2PM and 4PM was at its highest. There was no one around during this period. Usage could be monitored.")
    str2="\nAverage consumption of light bulb between 2PM and 4PM was at its highest. There was no one around during this period. Usage could be monitored."
    
else:
    print("Average consumption of light bulb between 8PM and 10PM was at its highest. Unused light bulbs could be switched off.")
    str2="\nAverage consumption of light bulb between 8PM and 10PM was at its highest. Unused light bulbs could be switched off."
    
    
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("aishwarya.sripathy@gmail.com", "cloudnine") 
  
# message to be sent 
message="Subject: Consumption stats\n\n"
message+=str1+"\nINFERENCE: \n"+str2
  
# sending the mail 
s.sendmail("aishwarya.sripathy@gmail.com", "aishwarya.sripathy@gmail.com", message) 
  
# terminating the session 
s.quit() 
    
    
