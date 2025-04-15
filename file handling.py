import time
file = open("g.txt", "r")
content = file.read()
print(content)

file.close()
time.sleep(3)

file = open("g.txt", "w")
file.write("now this is some quality content am i right python?")
file.close()
time.sleep(4)

file = open("g.txt", "a")
file.write("123456789")
file.close
time.sleep(1)

file = open("g.txt", "r")
content = file.read()
print(content)

file.close
time.sleep(2)

file = open("g.txt", "w")
file.truncate()
file.close
time.sleep(6) #End of the code, made by FireShark224.