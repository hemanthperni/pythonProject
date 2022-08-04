a=10
b=20
c=a+b
print(c)
for number in "2100030800":
    print('Current number',number)
    marks=[10,55,77,56]
    print(type(marks))
    for i in range(len(marks)):
        print('Current marks',marks)
        for num in range(10,20):
            print(num)
        count=0
        while count<5:
            print(count,"is less than 5")
            count=count+1
        else:
            print(count,"is greater than 5")