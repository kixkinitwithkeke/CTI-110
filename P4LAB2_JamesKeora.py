#Keora James
#October 31,2023
#Use for loops

#Get input from user
num1=int(input("Enter an integer: "))
num2=int(input("Enter another integer: "))

if num1 <= num2:
    for item in range(num1,num2+1,5):
        print  (item)

else:
   print("Rerun the program with the first int smaller") 
