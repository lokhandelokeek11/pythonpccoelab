def add_complex(a1, a2):
    print("Addition: ", a1 + a2)

def subtract_complex(a1, a2):
    print("Subtraction: ", a1 - a2)

def multiply_complex(a1, a2):
    print("Multiplication: ", a1 * a2)

def divide_complex(a1, a2):
        print("Division: ", a1 / a2)
      

sample1 = float(input("Enter real part of first number: "))
sample2 = float(input("Enter imaginary part of first number: "))
sample3 = float(input("Enter real part of second number: "))
sample4 = float(input("Enter imaginary part of second number: "))

a1 = complex(sample1, sample2)
a2 = complex(sample3, sample4)

print("First complex number is", a1)
print("Second complex number is", a2)

print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
x = int(input("Choose which operation you have to perform : "))
if x  == 1:
    add_complex(a1, a2)
elif x == 2:
    subtract_complex(a1, a2)
elif x == 3:
    multiply_complex(a1, a2)
elif x == 4:
    divide_complex(a1, a2)
else:
    print("Invalid choice")


