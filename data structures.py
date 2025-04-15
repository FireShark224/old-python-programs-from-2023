import time
numbers = [1, 2, 3, 4, 5]
print("Testing...")
time.sleep(3)

print(numbers[0])  
time.sleep(2)

numbers[2] = 10
print(numbers)  
time.sleep(2)

numbers.append(6)
print(numbers)  
time.sleep(2)

numbers.remove(2)
print(numbers)  
time.sleep(2)

length = len(numbers)
print(length) 
time.sleep(4)

numbers = [7, 8, 9, 10]
print (numbers)
time.sleep(2)
numbers.append(11)
print(numbers)
numbers.append(12)
print(numbers)
time.sleep(4)

my_dict = {"name": "Bob", "age": "unknown", "origin": "Poland"}
name = my_dict["name"]
age = my_dict["age"]
origin = my_dict["origin"]
print("First Person")
print("Name:", name)
print("Age:", age)
print("Origin Country:", origin)
print("Next Person")
time.sleep(5)

my_dict= {"name": "Ron", "age": "unknown", "origin": "USA"}
name = my_dict["name"]
age = my_dict["age"]
origin = my_dict["origin"]
print("Second Person")
print("Name:", name)
print("Age:", age)
print("Origin Country:", origin)
print("done")
time.sleep(6) #End of the code, made by FireShark224.