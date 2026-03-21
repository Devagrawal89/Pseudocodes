'''
a=4,b=3
Integer ComputeValue(Integer a, Integer b)
    Integer result =1
    While (b>0)
         If(b mod 2 EQUALS 1)
         result = result *a
         a=a*a
         b=b/2
    END While
    return result
END Function'''
def compute_value(a, b):
    result = 1

    while b > 0:
        if b % 2 == 1:
            result = result * a
        a = a * a
        b = b // 2   # integer division

    return result


# Example
a = 4
b = 3

print(compute_value(a, b))