def calculator():

    while True:

        print("==============")
        print("Calculator App")
        print("==============")
        print("1) Add ")
        print("2) Subtract ")
        print("3) Multiply ")
        print("4) Divide ")
        print("5) Modulo ")
        print("6) exponent ")
        print("0) Exit")

        choice = int(input("Enter your choice: "))

        if choice in (1,2,3,4,5,6):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please try again.")
                continue
            if choice == 1:
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif choice == 2:
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif choice == 3 :
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif choice == 4:
                if num2 == 0:
                    print("Error, cannot divide by zero.")
                else:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
            elif choice == 5:
                print(f"Result: {num1} % {num2} = {num1 % num2}")
            elif choice == 6:
                print(f"Result: {num1} ** {num2} = {num1 ** num2}")
            elif choice == 0:
                print("Exiting Calculator App. Goodbye!")
            else:
                print("Invalid input. Please enter a valid option (1-6)")
        if choice == 0:
            print("Exiting Calculator App. Goodbye!")
            break
calculator()


