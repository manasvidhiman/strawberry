print("-------------------------------")
print("-------------------------------")
print("Area Calculator 📐")
print("-------------------------------")
print("-------------------------------")

print("            ")
print("             ")






print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")


print("            ")
print("             ")


choice = input("Which shape : 1-5 ? ")

Base = input("Base : ")
Height = input("Height : ")

if choice == "1":
    Area = (float(Base) * float(Height)) / 2
    print("Area of Triangle is : ", Area)

elif choice == "2":
    Area = float(Base) * float(Height)
    print("Area of Rectangle is : ", Area)

elif choice == "3":
    Area = float(Base) * float(Base)
    print("Area of Square is : ", Area)

elif choice == "4":
    import math
    Radius = Base
    Area = math.pi * float(Radius) ** 2
    print("Area of Circle is : ", Area)

elif choice == "5":
    print("Exiting the calculator. Goodbye!")


else:
    print("Invalid choice. Please select a number between 1 and 5.")




