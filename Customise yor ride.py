print("Select your ride")
print("1. Bike")
print("2. Car")

#Take input of number 1 or 2
#select your ride
choice = int(input("Enter your choice:"))

#If user entered 1.
if(choice == 1):  #condition 1 outer if statement 
 print("What type of bike?")
 print("1.Royal enfield\n")
 print("2.Hero Honda\n")

 #Condition for selecting the type of bike
 choice2 = int(input("Enter your choice2:"))
 if(choice2 == 1):  #inner if statement 
  print("You have selected Royal enfield")

 else:
  print("You have selected Hero Honda")

#If user entered 2.
elif(choice == 2): #outer elif statement
   print("What type of car?")
   print("1.Ford\n")
   print("2.Lambo\n")
   choice3 = int(input("Enter your choice3:"))

   if(choice3 == 1):  #inner if statement 
  
 #Condition for selecting the type of car
    print("You have selected Ford")
   else:
    print("You have selected Lambo")

else:  #outer elif statement
 print("wrong choice!")
