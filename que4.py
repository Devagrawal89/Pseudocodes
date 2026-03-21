'''INTEGER i,num,fact
READ num
SET fact := 1
FOR i:= num TO 1 STEP -1
        fact := fact*i
END FOR
PRINT fact'''
num = int(input())
fact = 1

for i in range(num, 0, -1):
   fact *= i
print(fact)
