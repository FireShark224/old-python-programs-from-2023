print("Testing...")
import time
time.sleep(2)
print("Testing...")
time.sleep(5)
import random

number1 =random.randint(1, 9)
number2 =random.randint(1, 9)
number3 =random.randint(1, 9)

print("Your Numbers Are:", number1, number2, number3)
if number1 == number2 == number3:
    print("Jackpot! You Win!")
else:
    print("No Win For you This time.")
    print("Next!")
time.sleep(5)
number1 =random.randint(1, 9)
number2 =random.randint(1, 9)
number3 =random.randint(1, 9)

print("Your Numbers Again Are:", number1, number2, number3)
if number1 == number2 == number3:
    print("Jackpot! You Win!")
else:
    print("No Win For You this time")
    print("Next!")
    time.sleep(5)
    number1 =random.randint(1, 9)
    number2 =random.randint(1, 9)
    number3 =random.randint(1, 9)

    print("Your Numbers Are:", number1, number2, number3)
    if number1 == number2 == number3:
        print("Jackpot! You Win!")
    else:
        print("No Win For You This Time")
        time.sleep(5) #End of the code, made by FireShark224.