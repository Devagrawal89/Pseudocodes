
'''FUNCTION sumofsr(n:INTEGER):REAL
         DECLARE sum : REAL 
         SET sum := 0 
         FOR i:= 1 TO n
                 sum := sum + 1/i
         END FOR
         RETURN sum 
END FUNCTION 
PRINT sumofsr(4)'''
def sumofsr(n):
    sum = 0 
    for i in range(1,n+1):
        sum = sum + 1/i
    return sum 
print(sumofsr(4))



'''PROCEDURE sumofsr(n:INTEGER)
         DECLARE sum : REAL
         SET sum := 0
         FOR i:= 1 TO n
                 sum := sum + 1/i
         END FOR
         PRINT sum
END PROCEDURE
CALL sumofsr(4)'''
def sumofsr(n):
    sum = 0
    for i in range (1,n+1):
        sum = sum + 1/i
    print(sum)
sumofsr(4)