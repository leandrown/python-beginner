n = int(input())

sum = 0

while n > 0:
   length = n
   n //= 10
   length %= 10
   sum += length
    
print(sum)
