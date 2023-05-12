import math

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def exponent(num1, num2):
    return num1 ** num2

def square_root(num):
    return math.sqrt(num)

def calculate_area_rectangle(length, width):
    return length * width

def calculate_volume_cube(length, width, height):
    return length * width * height

def calculate_volume_sphere(radius):
    return (4/3) * math.pi * radius ** 3

def calculate_volume_cylinder(radius, height):
    return math.pi * radius ** 2 * height

while True:
    print("Simple Calculator")
    print("1. Perform arithmetic operations")
    print("2. Calculate area or volume of shapes")

    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        print("Enter two numbers:")

        num1 = float(input("Number 1: "))
        num2 = float(input("Number 2: "))

        print("Select an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Square Root")

        operation_choice = int(input("Enter your choice (1-6): "))

        if operation_choice == 1:
            result = add(num1, num2)
            operation = "+"
        elif operation_choice == 2:
            result = subtract(num1, num2)
            operation = "-"
        elif operation_choice == 3:
            result = multiply(num1, num2)
            operation = "*"
        elif operation_choice == 4:
            result = divide(num1, num2)
            operation = "/"
        elif operation_choice == 5:
            result = exponent(num1, num2)
            operation = "**"
        elif operation_choice == 6:
            result = square_root(num1)
            operation = "√"    
        else:
            print("Invalid choice!")
            continue

        print("Result: {} {} {} = {}".format(num1, operation, num2, result))

    elif choice == 2:
        print("Select a shape:")
        print("1. Rectangle")
        print("2. Cube")
        print("3. Sphere")
        print("4. Cylinder")

        shape_choice = int(input("Enter your choice (1-4): "))

        if shape_choice == 1:
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            area = calculate_area_rectangle(length, width)
            print("Area of the rectangle: {}".format(area))
        elif shape_choice == 2:
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            height = float(input("Enter the height: "))
            volume = calculate_volume_cube(length, width, height)
            print("Volume of the cube: {}".format(volume))
        elif shape_choice == 3:
            radius = float(input("Enter the radius: "))
            volume = calculate_volume_sphere(radius)
            print("Volume of the sphere: {}".format(volume))
        elif shape_choice == 4:
            radius = float(input("Enter the radius: "))
            height = float(input("Enter the height: "))
            volume = calculate_volume_cylinder(radius, height)
            print("Volume of the cylinder: {}".format(volume))
        else:
            print("Invalid choice!")
            continue

    else:
        print("Invalid choice!")
        continue

    restart = input("Do you want to perform another calculation? (y/n): ")
    if restart.lower() != "y":
        break
