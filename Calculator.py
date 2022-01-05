number = int(input("Enter Your First Number To Calculate: "))
number2 = int(input("Enter Your Second Number To Calculate: "))

operators = input("Select The Calculation Type (included: +, -, *, **, /, %, <=, >=): ")

if operators == "+":
    result = int(number) + int(number2)
elif operators == "-":
    result = int(number) - int(number2)
elif operators == "*":
    result = int(number) * int(number2)
elif operators == "**":
    result = int(number) ** int(number2)
elif operators == "/":
    result = int(number) / int(number2)
elif operators == "%":
    result = int(number) % int(number2)
elif operators == "<=":
    result = int(number) <= int(number2)
elif operators == ">=":
    result = int(number) >= int(number2)
else:
    print("Please Enter Your Operator Correctly!! ")

print(result)

