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
mycol1 = mydb["sensor_data_fan"]

myquery1={"date":datetime.today() , "ir":"No"}
mydoc1 = mycol1.find(myquery1)

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

val11=(dat1[0]+dat1[1]+dat1[2]+dat1[3]+dat1[4])
val12=(dat1[5]+dat1[6]+dat1[7]+dat1[8]+dat1[9])
val13=(dat1[10]+dat1[11]+dat1[12]+dat1[13]+dat1[14])


ans11=average_consumption_fan_calc(val11,5.0)
ans12=average_consumption_fan_calc(val12,5.0)
ans13=average_consumption_fan_calc(val13,5.0)

print("Average temperature between 10AM and 12PM = ",ans11)
print("Average temperature between 2PM and 4PM = ",ans12)
print("Average temperature between 8PM and 10PM = ",ans13)    

str4="Average temperature between 10AM and 12PM = "+str(ans11)+" C\nAverage temperature between 2PM and 4PM = "+str(ans12)+" C\nAverage temperature between 8PM and 10PM = "+str(ans13)+" C"

str3=""

if(int(ans11)>=int(ans12) or int(ans11)>=int(ans13)):
    print("The Fan was working between 10AM and 12PM. The average temperature was at its highest during this period. So 'Consumption was optimum'.")
    str3="\nThe Fan was working between 10AM and 12PM. The average temperature was at its highest during this period. So 'Consumption was optimum'."
    
elif(int(ans12)>=int(ans11) or int(ans12)>=int(ans13)):
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
message="Subject: Consumption Stats.\n\n"
message+=str4+"\nInference:"+str3
  
# sending the mail 
s.sendmail("aishwarya.sripathy@gmail.com", "aishwarya.sripathy@gmail.com", message) 
  
# terminating the session 
s.quit() 
    
    