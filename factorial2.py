'''
FUNCTION factorial(n:INTEGER)RETURN INTEGER
         DECLARE fact: INTEGER
         SET fact := 1 
         FOR i IN n TO 1 STEP-1
                  fact := fact*i
         END FOR 
         RETURN fact
END FUNCTION 
PRINT factorial(5)'''
def factorial(n):
    fact = 1 
    for i in range(n,1,-1):
        fact = fact*i
    return fact
print(factorial(5))



'''PROCEDURE factorial(n:INTEGER)
          DECLARE fact: INTEGER 
          SET FACT := 1
          FOR i IN n TO 1 STEP-1
                    fact := fact*i
          END FOR
          PRINT fact
END PROCEDURE
CALL(4)'''
def factorial(n):
    fact = 1
    for i in range(n,1,-1):
        fact = fact*i
    print(fact)
factorial(4)
