# unless explicitly mentioned user input always take it as string

name = input("Enter your name ")
age = int(input("Enter your age "))
marks = int(input("Enter your marks "))

print("Your name is", name)
print("Your age is", age)
print("Your marks is", marks)
print(age + marks)