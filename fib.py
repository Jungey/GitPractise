def fib(n):
    a = 0
    b = 1

    while (a<n):
        print (a, end=' ')
        a, b = b, a+b
        print()

# 300 is the branch 3 update
print('The series is as follows:' + fib(300))