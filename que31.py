'''
what's the output for n=42
Integer CountBits(Integer n)
    Integer count =0
        While(n>0)
            count=count+(n mod 2)
            n=n/2
        END While
    return count
END function
'''

def countBits(n):
    count = 0
    while n > 0:
        count += n % 2
        n = n // 2
    return count

print(countBits(42))