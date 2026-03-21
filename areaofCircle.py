'''
DECLARE r: INTEGER
DECLARE ar: INTEGER
CONSTANT PI:= 3.14
READ r
ar:= PI*r*r
PRINT ar'''

r = int(input("Enter radius: "))
PI = 3.14
ar = PI * r * r
print(ar)