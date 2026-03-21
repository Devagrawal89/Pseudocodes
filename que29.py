'''find value of s if n=127
read n
i=0,s=0
Function sample(Integer n)
     While (n>0)
         r=n%10
         p=8^i
         s=s+p*r
         i++
         n=n/10
    end While
return s'''

def sample(n):
    i = 0
    s = 0

    while n > 0:
        r = n % 10
        p = 8 ^ i
        s = s + (p * r)
        i += 1
        n = n // 10   

    return s

n = 127
print(sample(n))