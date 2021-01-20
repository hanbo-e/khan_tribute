# why the 3 divisibility rule works
import time


def expand(my_num):
    num_string = str(my_num)[::-1]
    num_length = len(num_string)
    output_string = ""
    for i in range(num_length):
        if i == 0:
            temp1 = num_string[i]
        else:
            nines = i * "9"
            temp1 = f"{num_string[i]}(1 + {nines}) + "
        output_string = temp1 + output_string
    # print(output_string)
    return output_string


def distribute(my_num):
    num_string = str(my_num)[::-1]
    num_length = len(num_string)
    output_string = ""
    for i in range(num_length):
        if i == 0:
            temp1 = num_string[i]
        else:
            nines = i * "9"
            temp1 = f"{num_string[i]} + {num_string[i]} * {nines} + "
        output_string = temp1 + output_string
    # print(output_string)
    return output_string


def rearrange(my_string):
    temp1 = my_string.split(" + ")
    front_string = ""
    end_string = ""
    for number in temp1:
        if "*" in number:
            front_string = front_string + " + " + number
        else:
            end_string = end_string + " + " + number
    output = front_string + end_string
    # print(output)
    return output


INTRO_TEXT = " We can check if a number, like 439 is divisible by three, by adding its digits:\
 4 + 3 + 9, and seeing whether the result, in this case 16, is divisible by three. If you are not\
 sure whether 16 is divisible by three, you can add its digits too: 1 + 6 = 7. Seven is not\
 divisible by three. But why does this work? As explained in Khan Academy, it works because we\
 can break any number, like 439, down in the following manner:\
 439 = 4 * 100 + 3 * 10 + 9 * 1 = 4* (1+99) + 3(1+9) + 9. Using the distributive rule\
 this becomes: 4 + 4(99) + 3 + 3(9) + 9. We can rearrange this to: 4(99) + 3(9) + 4 + 3 + 9\
 Since 9, 99, 999 etc. are all divisible by 3, and all their multiples are\
 divisible by 3, we only need to know if the last three digits (4 + 3 + 9) are also divisible by three\
 To see this for break down in action for integers, please enter a number:\n"

END_TEXT = "So we only need to know whether the sum of the digits of\
 our number of interest is divisible by 3"
if __name__ == "__main__":
    # print(INTRO_TEXT)
    start = input(INTRO_TEXT)
    print(str(start), " = ")
    time.sleep(1)
    my_test = expand(start)
    print(my_test, " = ")
    time.sleep(1)
    my_test = distribute(start)
    print(my_test, " = ")
    time.sleep(1)
    my_test = rearrange(my_test)
    print(my_test)
    time.sleep(1)
    print(END_TEXT)
