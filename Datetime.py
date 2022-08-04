import datetime
import time
print(time.time())
print(time.asctime(time.localtime(time.time())))
datetime_object =datetime.datetime.now()
print(datetime_object)
import calendar
s= calendar.prcal(2023)
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("select operation.")
print("1.Add")
print("2.subtract")
if choice in ('1','2','3','4'):
    num1=int(input("Enter First number: "))
    num2=int(input("Enter second number: "))
    if choice==1
        print("add",add(num1,num2))
        elif choice