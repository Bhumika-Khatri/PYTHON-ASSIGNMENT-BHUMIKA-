def sum_of_digits(n):
    dig=0
    s=0
    for i in range(n):
        dig=n%10
        n//=10
        s+=dig
    print("Sum of digits is: ",s)
n=int(input("Enter any number: "))  
sum_of_digits(n)