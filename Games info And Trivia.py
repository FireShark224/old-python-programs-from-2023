import time
print("Testing...")
time.sleep(2)

my_dict= {"Title": "Half Life 2", "Author": "Valve", "Year": 2004}
Title = my_dict["Title"]
Author = my_dict["Author"]
Year = my_dict["Year"]
print("Info About hl2")
time.sleep(2)

print("Game title:", Title)
print("Author:", Author)
print("Release Year:", Year)
print("This Game Was Also Released in OrangeBox")
print("next")
time.sleep(5)

my_dict= {"Title": "Team Fortress 2", "Author": "Valve", "Year": 2004}
Title = my_dict["Title"]
Author = my_dict["Author"]
Year = my_dict["Year"]
print("Info About tf2")
time.sleep(2)

print("Game Title:", Title)
print("Author:", Author)
print("Release Year:", Year)
print("This Game Was Released in OrangeBox too")
time.sleep(6)

print("Now you will have to input correct info about Cs Source")
time.sleep(4)

Title = input("Enter The Game Title:")
Author = input("Enter The Game Main Author:")
Year = input("Enter The Game Release Year:")
time.sleep(3)

if Title == "Counter Strike Source":
    print("ya guessed this one")
if Author == "Valve" :
    print("ya guessed this one")
if Year == "2004" :
    print("ya guessed this one")

if Title != "Counter Strike Source" :
    print("Wrong")
if Author != "Valve" :
    print("Wrong")
if Year != "2004" :
    print("Wrong")
print("Checking Answers...")  
time.sleep(5)

if Title == "Counter Strike Source" and Author == "Valve" and Year == "2004" :
    print("3 out of 3...  All Answers are correct. Congrats!")
if Title == "Counter Strike Source" and Author == "Valve" and Year != "2004" :
    print("2 out 3... nice")
if Title == "Counter Strike Source" and Year == "2004" and Author != "Valve" :
    print("2 out 3... nice")
if Author == "Valve" and Year == "2004" and Title != "Counter Strike Source" :
    print("2 out 3... nice")
    if Title == "Counter Strike Source" and Author != "Valve" and Year != "2004":
        print("1 out of 3... well it could have been worse")
if Title != "Counter Strike Source" and Author == "Valve" and Year != "2004" :
    print("1 out of 3... well it could have been worse")
if Title != "Counter Strike Source" and Author != "Valve" and Year == "2004" :
    print("1 out of 3... well it could have been worse")

time.sleep(12) #End of the code, made by FireShark224.