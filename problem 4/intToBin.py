def int_to_reverse_binary(num1):
    binary_val = ''
#write your while loop here
    while num1 > 0:
        digit = num1%2
        binary_val = binary_val + str(digit)
        num1 = num1//2

    if binary_val == '':
        binary_val = str(0)

    return binary_val


def string_reverse(input_string): 
    reverse_input = ''
    
    for char in input_string:
        reverse_input = str(char) + reverse_input
    
    return reverse_input

if __name__ == '__main__':
    user_input = int(input())
    
    binary_string = str(int_to_reverse_binary(user_input))
    binary_string = str(string_reverse(binary_string))
    
    print(binary_string)