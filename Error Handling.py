import time

try:
    result = 10 / 0
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero")
time.sleep(3)

try:
    result = 5 / 0
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero")
time.sleep(3) #End of the code, made by FireShark224.