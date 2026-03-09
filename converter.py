def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


def inches_to_cm(inches):
    return inches * 2.54

def cm_to_inches(cm):
    return cm / 2.54


def pounds_to_kg(pounds):
    return pounds * 0.453592

def kg_to_pounds(kg):
    return kg / 0.453592


def miles_to_km(miles):
    return miles * 1.60934

def km_to_miles(km):
    return km / 1.60934


def main():
    print("==== Measurement Converter ====")
    print("1. Fahrenheit → Celsius")
    print("2. Celsius → Fahrenheit")
    print("3. Inches → Centimeters")
    print("4. Centimeters → Inches")
    print("5. Pounds → Kilograms")
    print("6. Kilograms → Pounds")
    print("7. Miles → Kilometers")
    print("8. Kilometers → Miles")

    choice = int(input("Choose a conversion (1-8): "))
    value = float(input("Enter value: "))

    if choice == 1:
        print("Result:", fahrenheit_to_celsius(value), "°C")

    elif choice == 2:
        print("Result:", celsius_to_fahrenheit(value), "°F")

    elif choice == 3:
        print("Result:", inches_to_cm(value), "cm")

    elif choice == 4:
        print("Result:", cm_to_inches(value), "inches")

    elif choice == 5:
        print("Result:", pounds_to_kg(value), "kg")

    elif choice == 6:
        print("Result:", kg_to_pounds(value), "pounds")

    elif choice == 7:
        print("Result:", miles_to_km(value), "km")

    elif choice == 8:
        print("Result:", km_to_miles(value), "miles")

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
