# #program to find the prime numbers within a lower limit and an upper limit
# print the prime numbers if found in the range
# print -' No prime numbers in the range' if no prime numbers exist in that range



def is_prime(check_num):
    
        if check_num <= 1 :
            return False
        else:    
            for i in range(2,int(check_num//2)+1):
                if check_num % i == 0:
                    return False
            return True
    
lower_limit=int(input("Enter the lower limit : "))
upper_limit=int(input("Enter the upper limit : "))
        
prime_number_found=[]
for num in range(lower_limit,upper_limit+1):
    if is_prime(num) == True :
        prime_number_found.append(num)

if prime_number_found :
     print(f'Prime Numbers Found Between {lower_limit} and {upper_limit} -{prime_number_found}')    
else:
     print(f'No Prime Numbers Found Between {lower_limit} and  {upper_limit} ')           


