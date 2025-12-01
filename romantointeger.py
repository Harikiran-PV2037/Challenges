    # a function is defined to retrieve the values of each character
def value_check(digit):
    if digit == 'I':
        return 1  
    elif digit == 'V':
        return 5
    elif digit == 'X':
         return 10
    elif digit == 'L':
         return 50
    elif digit == 'C':
         return 100
    elif digit == 'D':
         return 500
    elif digit == 'M':
         return 1000
    else :
         return -1
    
   

while True :
    inp_str= input("Enter your roman number :")
    roman_num = inp_str.upper()
    result = 0
    # length of string is calculated
    len_str=len(roman_num)
    i=0
    while i <len_str :
            # value of ith character is stored into digit_left
            digit_left = value_check(roman_num[i])
                        
            if i+1< len_str:
                # value of i+1 th character is stored into digit_right
                digit_right = value_check(roman_num[i+1])
                

                if digit_left >= digit_right :
                    result = result + digit_left
                else :
                    result = result + digit_right - digit_left
                    i = i + 1
            else:
                result = result + digit_left
            i = i + 1
    if result <= 0:
            print(f'Invalid Roman number {inp_str} ')
            break
    else:
            print(f'Integer value for {inp_str} is {result}')

