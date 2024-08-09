def multiples(num,limit):
    for i in range (num ,limit + 1 , num):
        print (i, end = ",")
num = int(input("Enter the number: "))
limit = int(input("Enter the limit: "))
result = multiples(num , limit)