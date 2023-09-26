#Keora James
#9/26/2023
#Calculates travel expenses

budget=int(input("Enter Budget: "))
dest=input("Enter your travel destination: ")
gas=int(input("Enter Gas: "))
food=int(input("Enter Food: "))
hotel=int(input("Enter hotel: "))

expenses= gas+food+hotel

print("----------Travel Expenses---------")
print("Location: ",dest)
print("Initial Budget: ",budget)
print()
print("Gas Cost: ",gas)
print("Food: ",food)
print("Hotel: ",hotel)
print("Remaining Balance: ",budget-expenses)
print()
