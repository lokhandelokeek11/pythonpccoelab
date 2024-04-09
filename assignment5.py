def maximum(*args):
    maxnum = num[0]
   
    for i in num:
        if maxnum<i:
            maxnum = i
    print("Maximum value is",maxnum)
   
def minimum(*args):
    minnum = numbers[0]
   
    for i in numbers:
        if minnum>i:
            minnum = i
   
    print("Minimum value is",minnum)
   
def mean(*args):
    a = 0
    for i in num:
        a = a + i
    mean = a / n
   
    print("Mean value is ",mean)
   
numbers = ()

n = int(input("Enter total numbers:"))

for i in range(n):
    print("Enter number ",i+1,":",end=" ")
    x = int(input())
    numbers = numbers + (x)
   
maximum(numbers)
minimum(numbers)
meanvalues(numbers)
