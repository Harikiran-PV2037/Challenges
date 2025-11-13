
# to find a given number is Armstrong or Not
number= int(input("Enter your number :"))
if number < 0 :
    print("Enter Positive numbers only-")
else:    
    store_val=number
    len_number = len(str(abs(number)))
    
    sum=0
    for i in range(len_number):
        num2 = number % 10
        sum = sum + num2 ** len_number
        number = number // 10
    if sum == store_val:
        print("Armstrong Number") 
    else:
        print("Not Armstrong Number")  


