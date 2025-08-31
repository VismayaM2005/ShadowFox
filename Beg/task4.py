'''1. Write a program to determine the BMI Category based on user input.
Ask the user to:
Enter height in meters
Enter weight in kilograms
Calculate BMI using the formula: BMI = weight / (height)2
Use the following categories:
If BMI is 30 or greater, print "Obesity"
If BMI is between 25 and 29, print "Overweight"
If BMI is between 18.5 and 25, print "Normal"
If BMI is less than 18.5, print "Underweight"'''

height=float(input("Enter the height in meters: "))
weight=float(input("Enter the weight in kilograms: "))

bmi=weight / (height**2)
print("Task 4")

if bmi >= 30:
    print("Obesity")
elif 25 <= bmi < 30:
    print("Overweight")
elif 18.5 <= bmi < 25:
    print("Normal")
else:
    print("Underweight")


'''Write a program to determine which country a city belongs to. Given
list of cities per country:Ask the user to enter a city name and print the corresponding country.'''

Australia=["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE=["Dubai","Abu Dhabi","Sharjah","Ajman"]
India=["Mumbai","Banglore","Chennai","Delhi"]

city=input("Enter a city")

if city in Australia:
    print(f"{city} is in Austrailia")

elif city in UAE:
    print(f"{city} is in UAE")

elif city in India:
    print(f"{city} is in India")

else:
    print("Sorry the city does not exist in the list")


'''Write a program to check if two cities belong to the same country.
Ask the user to enter two cities and print whether they belong to the
same country or not.'''

city1=input("Enter the  first city")
city2=input("Enter the  second city")

if (city1 in Australia and city2 in Australia) or (city1 in UAE and city2 in UAE) or (city1 in India and city2 in India):
    print("Both cities are in the same country")
else:
    print("They don't belong to the same country")