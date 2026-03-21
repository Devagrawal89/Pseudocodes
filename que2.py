'''DECLARE num : INTEGER
DECLARE sum : INTEGER
SET sum := 0
READ num
FOR i:= 1 TO num
        sum := sum+i
END FOR
PRINT sum'''
num = int(input())
sum_val = 0

for i in range(1, num + 1):
   sum_val += i

print(sum_val)
