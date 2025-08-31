'''Task 1:Write a function that takes two arguments, 145 and 'o', and
uses the `format` function to return a formatted string. Print the
result. Try to identify the representation used.'''
print("Task 2")
def convert(value,code):
    print(format(value,code))

convert(145,'o')
#decimal number 145 is converted into octal form. 'o' is a format specifier for octal representation

'''Task 2: In a village, there is a circular pond with a radius of 84 meters.
Calculate the area of the pond using the formula: Circle Area = π r^2. (Use the value 3.14 for π) 
Bonus Question: If there is exactly
1.4 liters of water in a square meter, what is the total amount of
water in the pond? Print the answer without any decimal point in
it. Hint: Circle Area = π r^2 Water in the pond = Pond Area
Water per Square Meter'''

radius=84
pond_area=3.14*radius*radius
print(f"The area of the pond is {int(pond_area)}")
#Bonus
water_per_sq=1.4
total_water=pond_area*water_per_sq
print(f"Total amount of water is {int(total_water)}")

'''Task 3:If you cross a 490meterlong street in 7 minutes, calculate your
speed in meters per second. Print the answer without any decimal
point in it. Hint: Speed = Distance / Time'''
dist=490
time=7*60
speed=dist/time
print(f"The speed is {round(speed)}")