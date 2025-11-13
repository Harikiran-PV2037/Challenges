number= int(input("Enter your number :"))
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

#Armstrong numbers in a range given by user

number_range= int(input("Enter your range:"))
print("Armstrong Numbers in your number range are :")
for i in range(number_range+1):
    store_val=i
    len_number = len(str(abs(i)))
    sum=0
    check_number=i
    for j in range(len_number):
        num2 = store_val % 10
        sum = sum + num2 ** len_number
        store_val = store_val // 10
    if sum == check_number:
        print(check_number) 
    


