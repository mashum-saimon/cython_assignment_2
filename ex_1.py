# Write a Python function to generate the Fibonacci sequence up to a specified number n. Where
# n=100
def fib(num):
    if(num<0):
        print("Invalid number")
    else:
        a=0
        b=1

        print(a)
        print(b)

        for i in range(2,num):
            c=a+b
            a=b
            b=c
            if(c<=num):
                print(c)
            else:
                break
num=int(input("Enter the number till you want to see in fibonacci series : "))
fib(num)