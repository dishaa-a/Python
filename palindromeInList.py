num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

list = [num1, num2, num3, num4]
copy = list.copy()

if(list[: len(list)] == copy[:: -1]):
    print("List is a palindrome")
else:
    print("List is not a palindrome")
