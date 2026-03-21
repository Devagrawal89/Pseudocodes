'''INTEGER p,q,r
SET q := 13
FOR EACH p from 1 TO 4
         r = q MOD p
         p = p+5
         q = p+r
END FOR
         r = q/5
         PRINT q,r	
'''
q = 13
for p in range(1, 5):
   r = q % p
   p = p + 5
   q = p + r

r = q / 5
print(q)
print(r)
