def year(num1, num2):
    return (num2 - num1)
name = input("What is your name? :")    
num1 = int(input("What year were you born? :"))
import datetime
x = datetime.datetime.now() 
num2 = int(x.year)

Your_age= year(num2, num1)
print(name, ",you are" + str(Your_age) + "years.")