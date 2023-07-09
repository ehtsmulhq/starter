command=" "
print("Enter 'help' For Commands")
started= False
while True:
 command=input(">").lower()
 if command=="start":
     if started:
         print("Car is already Started!!!")
     else:
      started= True
      print("Car Started...")
 elif command=="stop":
     if not started:
         print(" Car is already Stoped!!!")
     else:
      started= False
      print("Car Stoped.")
 elif command=="help" :
    print("'Start' or 'start' to Start the car.\n'Stop' or'stop' to Stop the car.\n'Quit' or 'quit' to end the program.")
 elif command=="quit":
   break
 else :
    print("Invalid Input!!\nInput 'Help' or 'help' to know right Commands.")