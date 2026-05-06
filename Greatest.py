num1 = int(input("Enter three first Number :"))
num2 = int(input("Enter three second Number :"))
num3 = int(input("Enter three third Number :"))

if(num1 > num2):
    if(num1 > num3):
        print("Greatest number is :", num1)
    else:
        print("Greatest number is :", num3)
elif(num2 > num3):
    print("Greatest number is ", num2)
else:
    print("Greatest number is ", num3)