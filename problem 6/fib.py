def fibonacci(n):
    
    fib_num = 1
    last_num = 0

    for i in range(n):
        fib_num = fib_num + last_num
        last_num = fib_num

        print(fib_num)
        

    return fib_num

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')