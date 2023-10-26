#Keora James
#10/5/2023
#Dictioaries

#Get input from user
name=input("Enter your name: ")
hair=input("Enter your hair color: ")
eye=input("Enter your eye color: ")
height=float(input("Enter your height as a decimal:"))
age=int(input("Enter your age: "))
food=input("What's your favorite food: ")


#Create a dictionary
my_dict = {"Name":name,"Hair_Color":hair,"Eye_Color":eye,"Height":height,"Age":age,"Food":food}

#Get values using the key 
print(f"{my_dict['Name']} is a {my_dict['Height']} tall student with {my_dict['Hair_Color']} hair and {my_dict['Eye_Color']}.They are {my_dict['Age']} and their favorite food is {my_dict['Food']}.")