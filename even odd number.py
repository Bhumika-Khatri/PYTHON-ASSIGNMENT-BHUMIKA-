def separate(l):
    even=[]
    odd=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd
l=[int(x) for x in input("Enter a list of integers: ").split()]
even, odd = separate(l)
print("Even numbers:", even)
print("Odd numbers:", odd)