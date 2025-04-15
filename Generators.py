import time

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
time.sleep(3)

def numbergen():
    a, b = 2, 3
    while True:
        yield a
        a, b = b, a + b
time.sleep(3)

fib_gen = fibonacci_generator()

for _ in range(10):
    print(next(fib_gen))

print(next(fib_gen))
print(next(fib_gen))
time.sleep(3)

even_numbers = (x for x in range(10) if x % 2 == 0)

for num in even_numbers:
    print(num)
    time.sleep(1)
    numgen = numbergen()

for _ in range(100) :
    print(next(numgen))

print(next(numgen))
print(next(numgen))
time.sleep(1)

unevennum = (x for x in range(30) if x % 1 == 0)

for num in unevennum:
    print(num)
    time.sleep(1)
    numgen = numbergen()

for _ in range(250) :
    print(next(numgen))

print(next(numgen))
print(next(numgen))
time.sleep(5) #End of the code, made by FireShark224.