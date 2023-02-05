  

print("what do you want to do?")
print("a. addition")
print("b. subtraction")
print("c. multiplication")
print("d. division")
print("e. percent")
print("f. exponential")
print("g. simplify")
print("h. press H to end")

choice = input("enter your choice:")

num1 = float(input("enter 1st number:"))
num2 = float(input("enter 2nd number:"))
if choice in ['+' , "add" , "a"]:
        result = (num1) + (num2)
elif choice in ['-' , "sub" , "b"]:
        result = (num1) -(num2)
elif choice in ['*' , "mul" , "c"]:
        result = (num1) * (num2)
elif choice in ['/' , "div" , "d"]:
        result = (num1) / (num2)
elif choice in ['%' , "per" , "e"]:
        result = (num1) % (num2)
elif choice in ['^' , "exp" , "f"]:
        result = (num1) ** (num2)
elif choice in ['g' , 'sim' , ]:
        op1 = input("enter your first operator:")
        op2 = input("enter your second operator:")
        if op1 in ['+'] and op2 in ['-']:
                result = float(num1) + float(num2) - float(num2) 
elif not isinstance(num1, (int, float)):
        raise ValueError("Invalid number \"" + str(num1) + "\"")
elif not isinstance(num2, (int, float)):
        raise ValueError("Invalid number \"" + str(num2) + "\"")
elif choice == '/' and num2 == 0:
        raise ValueError("Division by zero")
elif choice not in ['+', '-', '*', '/' '%' '**']:
        raise ValueError("Invalid operator \"" + choice + "\"")
else:
        result = 'Unknown operator'
print(f'Result is {result}')
print("Thanks for calculation")
