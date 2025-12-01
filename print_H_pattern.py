for row in range(0,7):
    if row<7:
        print('*',end='')
    n= (7 // 2)+1
    for col in range(1, n): 

            # Condition for the middleValues 
            if row != n-1:

                # Three spaces 
                print(" ", end = " ")
                
            else:
                print(" " + '*', end = "")
                
    if row < 7: 
            
            print(" " + '*', end = "") 
           
    print()

