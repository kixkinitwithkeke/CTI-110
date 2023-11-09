#Keora James
#10/10/23
#Working with Variables 

#Create variables and get user input(6)
num_grades=int(input("How many grades will you enter?"))
#Create empty list 
grade_list=[]
for grade in range(num_grades):
    this_grade=int(input("Enter a grade: "))
    while this_grade <0 or this_grade > 100:
        print("Invaild grade entered.")
        this_grade=int(input("Enter a grade: "))
    grade_list.append(this_grade)
    print(f'{this_grade} has been added to the list')
for grade in grade_list:
    print(grade)





      
#make variable average using len and calcuate
gradeav= sum(grade_list)/len(grade_list)




                      
#Calculate min/max/sum/average/and assign to variables 
max_value=max(grade_list)
min_value=min(grade_list)
sum_value=sum(grade_list)
average_value=sum_value/len(grade_list)
print("------------Results-------------")
#Display info to user use print() statemet 
print("Highest Grade: ", max_value)
print("Lowest Grade: ", min_value)
print("Sum of Grades: ", sum_value)
print(f'Average: {average_value:.2f}')
print("------------------------------------------")

