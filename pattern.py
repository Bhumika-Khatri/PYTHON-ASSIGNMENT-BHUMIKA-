def pattern(n):
   i = 1
   while i <= n :
      j = n
      while j >= i:
         print("*", end=" ")
         j = j - 1
      print()
      i = i + 1
n = int(input('Enter the number of rows: '))
pattern(n)