'''DECLARE i: INTEGER
READ i
FOR j:= 1 TO 10
        PRINT j*i
END FOR
'''
i = int(input())
for j in range(1, 11):
   print(j * i)
