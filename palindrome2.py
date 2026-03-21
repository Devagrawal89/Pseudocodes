'''FUNCTION Palindrome(num:INTEGER):STRING 
         DECLARE a : INTEGER
         DECLARE b : INTEGER
         DECLARE c : INTEGER
         SET b := 0 
         n := num 
         WHILE num>0
               a := num MOD 10
               b := b*10+a
               num := num/10
        END WHILE 
        IF b == n  THEN 
                 RETURN "Palindrome"
        ELSE 
                 RETURN "Not Palindrome"
        END IF 
END FUNCTION 
PRINT Palindrome(121)'''
def Palindrome(num):
    b = 0 
    n = num 
    while num>0:
        a = num % 10
        b = b*10+a
        num = num//10
    if b == n :
        return "Palindrome"
    else:
        return "Not Palindrome"
print(Palindrome(12132))


'''PROCEDURE Palindrome(num:INTEGER) 
         DECLARE a : INTEGER
         DECLARE b : INTEGER
         DECLARE c : INTEGER
         SET b := 0 
         n := num 
         WHILE num>0
               a := num MOD 10
               b := b*10+a
               num := num/10
        END WHILE 
        IF b == n  THEN 
                PRINT "Palindrome"
        ELSE 
                PRINT "Not Palindrome"
        END IF 
END PROCEDURE
CALL Palindrome(121)'''
def Palindrome(num):
    b = 0 
    n = num 
    while num>0:
        a = num % 10
        b = b*10+a
        num = num//10
    if b == n :
        print("Palindrome")
    else:
        print("Not Palindrome")
Palindrome(121)
