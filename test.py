
# typecasting of variable
a = str(3)
b = 5
c = 'CAD'
print(a+c)

x = int(2)
y = str(2)
z = float(2)

print(x,y,z)

# print to display variables type
print(type(y))

# assigning multiple values to multiple variables in single line
x, y, z = 5, 6, 9
print(x, y, z)

# assigning single value to multiple variables in single line
x = y = z = 6
print(x, y, z)

# Example for variables being case sensitive and variable cannot be your keyword or have special chars
a3 = 7
print(a3)

A3 = 8
print(A3)

my_name = "Meghana"  # snake case
myName = "Meghana"   # camel case
MyName = "Meghana"   # pascal case

x = "I"
y = "am"
z = "learning python"
print(x,y,z)      # whenever there is a comma, there is a inherent space added in the output
print(x+y+z)     # concatination of strings, prints without spaces. Add is a mathematical operatior if used with numerical data types

# data types

a = [2, 9, 8, "as"]
print(a)

a = 8
b = "Ram"
print(a, b)  # comma allows to print variables of different data type

a = 3
b = 5
print(a+b)  # here plus is a mathematical operator