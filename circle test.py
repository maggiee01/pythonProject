# Area of the rectangle & perimeter

length = int(input("Enter length of a rectangle: "))
breadth = int(input("Enter breadth of a rectangle: "))
area = length * breadth
perimeter = 2*(length + breadth)
print(f"Area of a rectangle is {area} square meters and perimeter is {perimeter} meters") #f-string is string formatting


# Perimeter of a triangle
side_a = int(input("Enter side A of a triangle in meters: "))
side_b = int(input("Enter side B of a triangle in meters: "))
side_c = int(input("Enter side C of a triangle in meters: "))
perimeter = side_a + side_b + side_c
print(f"Perimeter of the triangle is: {perimeter} meters")


#weekly and monthly salary
work_hours = float(input("Enter the number of hours you work daily: "))
rate_per_hour = float(input("Enter the rates you are paid per hour: "))
weekly_salary = 5 * work_hours * rate_per_hour
monthly_salary = 4 * weekly_salary  #optimization
print(f"Your weekly and monthly salaries are {weekly_salary} and {monthly_salary} rupees")

#man's age in seconds and assuming he lives for 100 years, seconds remaining in his life

age = int(input("Enter your age: "))
age_in_seconds = age * 365 * 24 * 3600
remaining_age = (100 - age) * 365 * 24 * 3600
print(f"Age of the person in seconds is {age_in_seconds} and assuming he would live for 100 years, the remaining seconds of his life are {remaining_age}")

#Assignment operators are =, +=, -= etc
#arthemetic operators are +, -, *, %, \
#comparison operators are >, <, >=, <=, ==, !=
#logical operators are and, or, not

a = 9.8
b = 10
print(a == b)
