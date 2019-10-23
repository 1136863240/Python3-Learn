def fib(num1, num2, count = 10):
    if count > 0:
        count = count - 1
        print(num1 + num2)
        fib(num1=num2, num2=num1 + num2, count=count)
    else:
        return

print(1)
print(1)

fib(1, 1)
