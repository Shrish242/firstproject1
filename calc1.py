#this project is by sagaroaf

def main():
    
    while True:
        menu = (
                "***MENU***\n"
                "1. ADDITION\n"
                "2. SUBTRACTION\n"
                "3. MULTIPLICATION\n"
                "4. DIVISION\n"
                "5. SQUARE\n"
                "6. CUBE\n"
                "7. MODULUS\n"
                "8. EXPONENTIAL\n"
                "9. EXIT\n"
             "Enter your choice: "
)
        choice = int(input(menu))


        if choice == 9:
            break
        else:
            num1 = float(input("Enter the num1 for calculation: "))
            num2 = float(input("Enter the num2 for calculation: "))

        if choice == 1:
            ADD = num1 + num2
            print(f"ADD = {num1} + {num2} = {ADD}\n")
        elif choice == 2:
            SUB = num1 - num2
            print(f"SUB = {num1} - {num2} = {SUB}\n")
        elif choice == 3:
            MUL = num1 * num2
            print(f"MUL = {num1} * {num2} = {MUL}\n")
        elif choice == 4:
            DIV = num1 / num2
            print(f"DIV = {num1} / {num2} = {DIV}\n")
        elif choice == 5:
            SQR1 = num1 * num1
            SQR2 = num2 * num2
            print(f"SQR1 = ({num1})^2 = {SQR1}\n")
            print(f"SQR2 = ({num2})^2 = {SQR2}\n")
        elif choice == 6:
            CUBE1 = num1 * num1 * num1
            CUBE2 = num2 * num2 * num2
            print(f"CUBE1 = ({num1})^3 = {CUBE1}\n")
            print(f"CUBE2 = ({num2})^3 = {CUBE2}\n")
        elif choice == 7:
            MOD = num1 % num2
            print(f"MOD = {num1} % {num2} = {MOD}\n")
        elif choice == 8:
            EXP = num1 ** num2
            print(f"EXP = {num1} ** {num2} = {EXP}\n")

        else:
            print("\n***THANK YOU***\n")
        
        continue_program = input("Do you want to continue the program? (y/n): ")
        if continue_program.lower() == "n":
            break
    print("\n***THANK YOU***\n")

main()
