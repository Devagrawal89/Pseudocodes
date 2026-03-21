'''FUNCTION Rev(n:INTEGER):INTEGER
         DECLARE a : INTEGER 
         DECLARE b : INTEGER
         SET b := 0
         WHILE n>0 LOOP 
               a := n MOD 10 
               n := n/10
               b := b*10 + a
         END WHILE 
         RETURN b 
END FUNCTION 
PRINT Rev(1234)'''
def Rev(n):
    b = 0 
    while n > 0:
        a = n%10
        n = n//10 
        b = b*10 + a
    return b 
print(Rev(1234))



'''PROCEDURE Rev(n:INTEGER)
         DECLARE a : INTEGER 
         DECLARE b : INTEGER
         SET b := 0
         WHILE n>0 LOOP 
               a := n MOD 10 
               n := n/10
               b := b*10 + a
         END WHILE 
         PRINT b 
END PROCEDURE 
CALL Rev(1234)'''
def rev(n):
    b = 0 
    while n>0:
        a = n % 10 
        n = n // 10
        b = b*10 + a 
    print(b)
rev(1234)
