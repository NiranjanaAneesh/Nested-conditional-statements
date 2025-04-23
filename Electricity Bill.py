#Taking inpout from user
UC = int(input("Enter units consumed:"))

#Electricity Bill 
if UC <= 50:
 print("Your electricity Bill will be",(UC*2.60)+25)
 
elif UC <=100:
 print("Your electricity Bill will be",(UC*3.25)+35)

elif UC <=200:
 print("Your electricity Bill will be",(UC*5.26)+45)
  
elif UC >200:
 print("Your electricity Bill will be",(UC*8.45)+75)