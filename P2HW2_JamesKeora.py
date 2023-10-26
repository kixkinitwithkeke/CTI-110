#Keora James
#10/10/23
#Working with Variables 

#Create variables and get user input(6)
module1=float(input("Enter grade for Module 1: "))
module2=float(input("Enter grade for Module 2: "))
module3=float(input("Enter grade for Module 3: "))
module4=float(input("Enter grade for Module 4: "))
module5=float(input("Enter grade for Module 5: "))
module6=float(input("Enter grade for Module 6: "))

#Create an empty list
new_list=[]
#Add to list
new_list.append(module1)
new_list.append(module2)
new_list.append(module3)
new_list.append(module4)
new_list.append(module5)
new_list.append(module6)
#Calculate min/max/sum/average/and assign to variables 
max_value=max(new_list)
min_value=min(new_list)
sum_value=sum(new_list)
average_value=sum_value/len(new_list)
print("------------Results-------------")
#Display info to user use print() statemet 
print("Highest Grade: ", max_value)
print("Lowest Grade: ", min_value)
print("Sum of Grades: ", sum_value)
print(f'Average: {average_value:.2f}')
print("------------------------------------------")