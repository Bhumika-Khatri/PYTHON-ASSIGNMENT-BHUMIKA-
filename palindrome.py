def palindrome(string):
    if string==string[::-1]:
        print("Palindrome")
    else:
        print("not a palindrome")
string=str(input("Enter a string: "))
palindrome(string)