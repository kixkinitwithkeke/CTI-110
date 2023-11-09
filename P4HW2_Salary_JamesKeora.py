#Keora James
#11/09/23
#P4HW2-Salary Calculator 
num_employees = 0
total_paid_out= 0

#Get employee name from user
name=input("Enter employee's name: ")
while name !="Done":
  num_employees += 1

  #Get number of hours from user
  hworked=float(input("Enter number of hours worked: "))

  #Get payrate per hour from user
  payrate=float(input("Enter employees's pay rate: "))
  print("-------------------------------------------------------------------------")
  print("Employee's name: "+name)
  #Determine if employee worked more than 40 hours 
  if hworked>40:
    overtime=hworked - 40
  else:overtime=0

  #Calculate reg hours worked 
  if overtime>0:
    reghours=hworked-overtime
  else:reghours=hworked

  #Calculate reg pay 
  regpay=reghours*payrate
  #Calculate overtime hours worked 
  #Calculate overtime pay
  overtimepay=overtime*payrate*1.5
  gross_pay = regpay + overtimepay
  total_paid_out += gross_pay 
  name=input("Enter employee's name: ")


#Display name,payrate,reg hours,overtime hours,reg pay,overtime pay,gross pay
print("------------------------")
print(num_employees, "have been added")
print("The total paid out to all employees is" , total_paid_out)
