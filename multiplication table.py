def table(n):
    print("Multiplication table for ",n)
    for i in range(1,11):
        print(n,"*",i,"=",n*i)
n=int(input("Enter any number: "))
table(n)