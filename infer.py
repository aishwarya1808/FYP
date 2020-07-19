from with_rules_method import average_consumption_calc
from with_rules_method import average_consumption_fan_calc
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
mycol1 = mydb["sensor_data_fan"]

myquery={"date":datetime.today() , "ir":"No"}
mydoc = mycol.find(myquery)

myquery1={"date":datetime.today() , "ir":"No"}
mydoc1 = mycol1.find(myquery1)

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
val1=dat[0]+dat[1]+dat[2]+dat[3]+dat[4]
val2=dat[5]+dat[6]+dat[7]+dat[8]+dat[9]
val3=dat[10]+dat[11]+dat[12]+dat[13]+dat[14]

ans1=average_consumption_calc(val1,5.0)
ans2=average_consumption_calc(val2,5.0)
ans3=average_consumption_calc(val3,5.0)

print("Average consumption between 10AM and 12PM = ",ans1)
print("Average consumption between 2PM and 4PM = ",ans2)
print("Average consumption between 8PM and 10PM = ",ans3)

str1="Average consumption between 10AM and 12PM = "+str(ans1)+"\nAverage consumption between 2PM and 4PM = "+str(ans2)+"\nAverage consumption between 8PM and 10PM = "+str(ans3)
str2=""
if(ans1>=ans2 or ans1>=ans3):
    print("Average consumption of light bulb between 10AM and 12PM was at its highest. There was no one around during this period. Usage could be monitored.")
    str2="\nAverage consumption of light bulb between 10AM and 12PM was at its highest. There was no one around during this period. Usage could be monitored."
    
elif(ans2>=ans1 or ans2>=ans3):
    print("Average consumption of light bulb between 2PM and 4PM was at its highest. There was no one around during this period. Usage could be monitored.")
    str2="\nAverage consumption of light bulb between 2PM and 4PM was at its highest. There was no one around during this period. Usage could be monitored."
    
else:
    print("Average consumption of light bulb between 8PM and 10PM was at its highest. Unused light bulbs could be switched off.")
    str2="\nAverage consumption of light bulb between 8PM and 10PM was at its highest. Unused light bulbs could be switched off."
    
    
dat1=[]    
val1=mycol1.find({},{"temp":1 ,"_id":0}).sort('_id',-1).limit(15);
    #val.append(x)
for i in val1:
    #print(i)
    txt=str(i)
    x=re.findall("[-+]?([0-9]*\.[0-9]+|[0-9]+)",txt)
    dat1.append(float("".join(x[0])))
    #print(dat)


val11=0
val12=0
val13=0

val11=dat1[0]+dat1[1]+dat1[2]+dat1[3]+dat1[4]
val12=dat1[5]+dat1[6]+dat1[7]+dat1[8]+dat1[9]
val13=dat1[10]+dat1[11]+dat1[12]+dat1[13]+dat1[14]


ans11=average_consumption_fan_calc(val11,5.0)
ans12=average_consumption_fan_calc(val12,5.0)
ans13=average_consumption_fan_calc(val13,5.0)

print("Average temperature between 10AM and 12PM = ",ans11)
print("Average temperature between 2PM and 4PM = ",ans12)
print("Average temperature between 8PM and 10PM = ",ans13)    

str4="Average temperature between 10AM and 12PM = "+ans11+"\nAverage temperature between 2PM and 4PM = "+ans12+"\nAverage temperature between 8PM and 10PM = "+ans13

str3=""

if(int(ans1)>=int(ans2) or int(ans1)>=int(ans3)):
    print("The Fan was working between 10AM and 12PM. The average temperature was at its highest during this period. So 'Consumption was optimum'.")
    str3="\nThe Fan was working between 10AM and 12PM. The average temperature was at its highest during this period. So 'Consumption was optimum'."
    
elif(int(ans2)>=int(ans1) or int(ans2)>=int(ans3)):
    print("The Fan was working between 2PM and 4PM. The average temperature was at its highest during this period. So 'Consumption was optimum'.")
    str3="\nThe Fan was working between 2PM and 4PM. The average temperature was at its highest during this period. So 'Consumption was optimum'."
    
else:
    print("The Fan was working between 8PM and 10PM. Recorded average room temperature during this period was low. The usage of fan between 8PM and 5AM could be optimized.")
    str3="\nThe Fan was working between 8PM and 10PM. Recorded average room temperature during this period was low. The usage of fan between 8PM and 5AM could be optimized."

s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("aishwarya.sripathy@gmail.com", "cloudnine") 
  
# message to be sent 
message =str1+str2+str4+str3
  
# sending the mail 
s.sendmail("aishwarya.sripathy@gmail.com", "aishwarya.sripathy@gmail.com", message) 
  
# terminating the session 
s.quit() 
    
    
