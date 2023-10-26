#Keora James
#10/3/2023
#Use floats and expression to calculate gas cost

#Create input variables
mpg= float(input("Enter the car's mpg: "))
cost_per_gallon= float(input("How much does a gallon of gas cost: "))                 
#Calculate gas cost based off gallons needed & price per gallon
#Calulate for 20 miles, 75 miles, 500 miles
cost_20 = (20/mpg) * cost_per_gallon
cost_75 = (75/mpg) * cost_per_gallon
cost_500 = (500/mpg) * cost_per_gallon
                 
#Output values using f-string & format floats
print(f"{cost_20:.2f} {cost_75:.2f} {cost_500:.2f}")
