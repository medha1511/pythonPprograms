# no is prime or not

'''num=int(input("enter no"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("no is not prime")
            
    else:
        print("prime")'''


a=int(input("enter lim"))
for i in range(0,a+1):
    if i>1:
        for j in range(2,i):
            if i%2==0:
                break
        else:
            print(i)

'''a=int(input("Enter limit"))

for i in range(2,a+1):
    if(i==2 or i==3 or i==5):
        print(i)
    elif(i%2==0 or i%3==0 or i%5==0):
        continue
    else:
        print(i)'''
            
        


        
        
