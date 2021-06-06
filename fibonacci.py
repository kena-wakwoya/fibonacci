# displaying the nth term of fibonnaci using python


# ask for the number of terms u want to list 
nth_term = int(input("enter number of terms?"))

# the first two terms 0,1
n1,n2 = 0,1
count= 0
if nth_term <=0:
    print('enter +ve number')
elif nth_term==1:
    print("list of the first " + str(nth_term) + " fibonacci sequence!")
    print(n1)
else:
    print("list of the first " + str(nth_term) + " fibonacci sequence!")
    while count < nth_term:
        print(n1, end = ', ')
        nth = n1 + n2

        n1 = n2
        n2 = nth

        count +=1


