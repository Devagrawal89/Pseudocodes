'''
INTEGER value,n
SET value:= 32,n:=1
WHILE value GREATER THAN OR EQUAL TO n LOOP
                    value<-value>>1
END LOOP
PRINT value '''
value = 32
n = 1
while value >= n:
   value = value >> 1
print(value)

