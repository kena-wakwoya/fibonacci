# displaying n-th terms of fibonnaci sequence in python
# i will try to display the fibonacci sequence using recursion. 


def recurFibonacci(n):
    if n <= 1:
        return n
    else:
        return (recurFibonacci(n-1) + recurFibonacci(n-2))
nth_terms = int(input("How many terms u want to display? "))

if nth_terms <=0:
    print('input should be +ve number')
else:
    print("list of the first " + str(nth_terms) + " fibonacci sequence!")
    for i in range(nth_terms):
        print(recurFibonacci(i), end = ",")





