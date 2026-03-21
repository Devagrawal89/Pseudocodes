'''what value of even counter if number =2630
read nummber
function divisble(number)
    even counter =0, nu,,_remainder= number;
        While(num_remainder)
            digit=num_remainder%10;
            if digit!=0  AND number%digit=0
                even_counter=even_counter+1
            end if
        num_remainder=num_remainder/10
        end while
return even_counter'''

def divisible(number):
    even_counter = 0
    num_remainder = number

    while num_remainder > 0:
        digit = num_remainder % 10

        if digit != 0 and number % digit == 0:
            even_counter += 1

        num_remainder = num_remainder // 10

    return even_counter


number = 2630
print(divisible(number))