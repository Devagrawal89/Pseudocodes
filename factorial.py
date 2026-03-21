'''INTEGER i,num,fact
READ num
SET fact := 1
SET i := num
WHILE i>0
        fact := fact*i
        DECREMENT i
END WHILE
PRINT fact'''
num = int(input())
fact = 1
i = num
while i > 0:
   fact *= i
   i -= 1
print(fact)
