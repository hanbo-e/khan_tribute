#why the 3 divisibility rule works

def expand(my_num):
    num_string = str(my_num)[::-1]
    num_length = len(num_string)
    output_string = ''
    for i in range(num_length):
        if i == 0:
            temp1 = num_string[i]
        else:
            nines = i * '9'
            temp1 = f"{num_string[i]}(1 + {nines}) + "
        output_string = temp1 + output_string
    #print(output_string)
    return output_string

#distribute

def distribute(my_num):
    num_string = str(my_num)[::-1]
    num_length = len(num_string)
    output_string = ''
    for i in range(num_length):
        if i == 0:
            temp1 = num_string[i]
        else:
             nines = i * '9'
             temp1 = f"{num_string[i]} + {num_string[i]} * {nines} + "
        output_string = temp1 + output_string
    #print(output_string)
    return output_string

def rearrange(my_string):
    temp1 = my_string.split(' + ')
    front_string = ''
    end_string = ''
    for number in temp1:
        if '*' in number:
            front_string = front_string + ' + ' + number
        else:
            end_string = end_string + ' + ' + number
    output = (front_string + end_string)
    #print(output)
    return output

INTRO_TEXT = "The rule for checking if a number is divisible by three is\
 add all the digits and check if that number is divisible by three.\
 One can keep adding the digits of the result if the answer is not\
 obvious. Why does this work? As explained in Khan Academy, if we\
 know that 9, 99, 999 etc. are all divisible by 3, and that all their\
 multiples are divisible by 3, we can break numbers down in the\
 following manner:\n Please enter a number\n"

END_TEXT = "So we only need to know whether the sum of the digits of\
 our number of interest is divisible by 3"
if __name__ == "__main__":
    #print(INTRO_TEXT)
    start = input(INTRO_TEXT)
    print(str(start), ' = ')
    my_test = expand(start)
    print(my_test)
    my_test = distribute(start)
    print(my_test)
    my_test = rearrange(my_test)
    print(my_test)
    print(END_TEXT)