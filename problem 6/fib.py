def fibonacci(n):
    
    fib_num = 1
    last_num = 0

    if n == 0:
        fib_num = 0
    elif n <= 0:
        fib_num = -1
    else:
        for i in range(n-1):
            set_num = fib_num + last_num
            last_num = fib_num
            fib_num = set_num

    return fib_num

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')