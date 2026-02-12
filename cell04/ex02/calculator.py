#!/usr/bin/env python3
oper = ["+", "-", "/", "*"]
num1 = int(input("Give me the first number: "))
num2 = int(input("Give me the second number: "))

print("Thank you!")

for i in oper:
    result = eval(f"{num1} {i} {num2}")
    print(f"{num1} {i} {num2} = {result}")
