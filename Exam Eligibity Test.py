#Take input for the student that he/she can attend the exam or not
medical_cause = input("did you have a medical cause Y or N:")

#Take input of the attendance
attend = int(input("enter the attendance of the student:"))

#Checking the user input predicting output accordingly

if medical_cause == 'Y':  #Checking the condition 1
  print("You are allowed")

else:
  if attend>=75:  #Checking the condition 2
    print("Allowed")

  else:
    print('Not Allowed')