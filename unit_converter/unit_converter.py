def show_menu():
    print("=== Unit Converter ===")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Exit")
    print("=====================")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice(1-4): ")
        if choice == "1":
            convert_length()
        elif choice == "2":
            convert_weight()
        elif choice == "3":
            convert_temperature()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def convert_length():
    print("=== Length Converter ===")
    print("1. Convert from meters to feet")
    print("2. Convert from feet to meters")
    print("3. Convert from kilometers to miles")
    print("4. Convert from miles to kilometers")
    print("5. Back to main menu")

    while True:
        print("Enter the number of the conversion you want to perform:")
        choice = input("Enter your choice(1-5): ")
        if choice == "1":
            convert_from_meters_to_feet()
        elif choice == "2":
            convert_from_feet_to_meters()
        elif choice == "3":
            convert_from_kilometers_to_miles()
        elif choice == "4":
            convert_from_miles_to_kilometers()
        elif choice == "5":
            print("Returning to main menu...")
            break   
        else:
            print("Invalid choice. Please try again.")

def convert_from_meters_to_feet():
    meters = float(input("Enter the length in meters: "))
    feet = meters * 3.28084
    print(f"{meters} meters is equal to {feet} feet.")

def convert_from_feet_to_meters():
    feet = float(input("Enter the length in feet: "))
    meters = feet / 3.28084
    print(f"{feet} feet is equal to {meters} meters.")

def convert_from_kilometers_to_miles():
    kilometers = float(input("Enter the length in kilometers: "))
    miles = kilometers / 1.60934
    print(f"{kilometers} kilometers is equal to {miles} miles.")

def convert_from_miles_to_kilometers():
    miles = float(input("Enter the length in miles: "))
    kilometers = miles * 1.60934
    print(f"{miles} miles is equal to {kilometers} kilometers.")

def convert_weight():
    print("=== Weight Converter ===")
    print("1. Convert from kilograms to pounds")
    print("2. Convert from pounds to kilograms") 
    print("3. Back to main menu")

    while True:
        print("Enter the number of the conversion you want to perform:")
        choice = input("Enter your choice(1-3): ")
        if choice == "1":
            convert_from_kilograms_to_pounds()
        elif choice == "2":
            convert_from_pounds_to_kilograms()
        elif choice == "3":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please try again.")  

def convert_from_kilograms_to_pounds():
    kilograms = float(input("Enter the weight in kilograms: "))
    pounds = kilograms * 2.20462
    print(f"{kilograms} kilograms is equal to {pounds} pounds.")

def convert_from_pounds_to_kilograms():
    pounds = float(input("Enter the weight in pounds: "))   
    kilograms = pounds / 2.20462
    print(f"{pounds} pounds is equal to {kilograms} kilograms.")


def convert_temperature():
    print("=== Temperature Converter ===")  
    print("1. Convert from Celsius to Fahrenheit")
    print("2. Convert from Fahrenheit to Celsius")
    print("3. Back to main menu")

    while True:
        print("Enter the number of the conversion you want to perform:")
        choice = input("Enter your choice(1-3): ")
        if choice == "1":
            convert_from_celsius_to_fahrenheit()
        elif choice == "2":
            convert_from_fahrenheit_to_celsius()
        elif choice == "3":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please try again.")  

def convert_from_celsius_to_fahrenheit():
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} Celsius is equal to {round(fahrenheit)} Fahrenheit.")

def convert_from_fahrenheit_to_celsius():
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))  
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} Fahrenheit is equal to {round(celsius)} Celsius.")


if __name__ == "__main__":
    main()



