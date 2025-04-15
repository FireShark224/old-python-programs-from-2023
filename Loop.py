import time
import random
print("Testing...")
time.sleep(2)
print("Testing...")
time.sleep(1)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for num in numbers:
    print(num)
    time.sleep(1)
    numbers = [random.randint(50, 100), random.randint(50, 100), random.randint(50, 100), random.randint(50, 100), random.randint(50, 100)]
    for num in numbers:
        print(num)
        time.sleep(1)
        count = 1

while count <= 5:
    print(count)
    count += 1

    count = 1

    while count <= 69:
        print(count)
        count += 5 #End of the code, made by FireShark224.