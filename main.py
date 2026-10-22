
import random


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input! Please enter a number.")


def calculator():
    print("\n--- Basic Calculator ---")
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")

    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Choose operation (1-4): ")

    if choice == "1":
        print("Result:", a + b)
    elif choice == "2":
        print("Result:", a - b)
    elif choice == "3":
        print("Result:", a * b)
    elif choice == "4":
        if b == 0:
            print("Error: Cannot divide by zero!")
        else:
            print("Result:", a / b)
    else:
        print("Invalid operation!")


def unit_converter():
    print("\n--- Unit Converter ---")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")

    choice = input("Choose conversion (1-2): ")

    if choice == "1":
        km = get_number("Enter kilometers: ")
        print("Miles:", round(km * 0.621371, 2))
    elif choice == "2":
        celsius = get_number("Enter temperature in Celsius: ")
        fahrenheit = (celsius * 9 / 5) + 32
        print("Fahrenheit:", round(fahrenheit, 2))
    else:
        print("Invalid conversion!")


def currency_converter():
    print("\n--- Currency Converter ---")
    print("1. INR to USD")
    print("2. USD to INR")
    print("Note: Example rate only, not a live exchange rate.")

    choice = input("Choose conversion (1-2): ")
    amount = get_number("Enter amount: ")

    example_rate = 0.012  # Example rate: 1 INR = 0.012 USD

    if amount < 0:
        print("Amount cannot be negative!")
    elif choice == "1":
        print("Approximate USD:", round(amount * example_rate, 2))
    elif choice == "2":
        print("Approximate INR:", round(amount / example_rate, 2))
    else:
        print("Invalid conversion!")


def main():
    while True:
        print("\n===== Interactive Calculator & Unit Converter =====")
        print("1. Basic Calculator")
        print("2. Unit Converter")
        print("3. Currency Converter")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            calculator()
        elif choice == "2":
            unit_converter()
        elif choice == "3":
            currency_converter()
        elif choice == "4":
            print("Thank you for using the application!")
            break
        else:
            print("Invalid choice! Please select 1-4.")


if __name__ == "__main__":
    main()
