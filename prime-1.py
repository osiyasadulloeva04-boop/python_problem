

##version 2
for num in range (2,101):
         for  i in range (2,num):
             if num%i==0:
                 break  
         else:
            print (num)
            
 ###version 1
for n in range(1, 101):
    count = 0
    
    
    for d in range(1, n + 1):
        if n % d == 0:
            count += 1
    
    if count == 2:
        print(n)
    
    
    
