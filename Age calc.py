def year(num1, num2):
    return num2 - num1
num1 = int(input("What year were you born? :"))
num2 = int(input("What is the current year? :"))

Your_age= year(num2, num1)
print("Your are" + str(Your_age) + "years.")