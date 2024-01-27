import time


def dotX3():
    time.sleep(0.25)
    print(".", end="")
    time.sleep(0.25)
    print(".", end="")
    time.sleep(0.25)
    print(".")
    time.sleep(0.75)

print('')
print("REMOVING AND REPLACING CHARACTERS OF STRING")
print("\n")

s = input("Enter Message : ")
print("")
print("[Replace / Remove] :")
print("")
print("a - REPLACE")
print("b - REMOVE")

ans = input(" > ")
print("")

if ans.lower() == "a":
    print("Replace Using :")
    print("")
    print("a - Character")
    print("b - Position")

    ans = input(" >> ")
    print("")

    if ans.lower() == "a":
        rem = input("Character to replace : ")
        add = input("Replace with : ")
        print("Replacing", end="")
        dotX3()
        s = s.replace(rem, add)
        print(f"Your new message is : {s}")
        time.sleep(0.5)
    elif ans.lower() == "b":
        rem = int(input("Position of character to replace : "))
        add = input("Replace with : ")
        print("Replacing", end="")
        dotX3()
        s = s.replace(s[rem - 1], add)
        print(f"Your new message is : {s}")
        time.sleep(0.5)
    else:
        print("Option not found, exiting")
        exit()

elif ans.lower() == "b":
    print("Remove Using :")
    print("")
    print("a - Character")
    print("b - Position")
    ans = input(" >> ")
    print("")

    if ans.lower() == "a":
        rem = input("Character to remove : ")
        print("Removing", end="")
        dotX3()
        s = s.replace(rem, "")
        print(f"Your new message is : {s}")
        time.sleep(0.5)
    elif ans.lower() == "b":
        rem = int(input("Position of character to remove : "))
        print("Removing", end="")
        dotX3()
        s = s.replace(s[rem - 1], "")
        print(f"Your new message is : {s}")
        time.sleep(0.5)
else:
    print("Option not found, exiting")
    exit()

# RESULT
    
# REMOVING AND REPLACING CHARACTERS OF STRING


# Enter Message : happr human!

# [Replace / Remove] :

# a - REPLACE
# b - REMOVE
#  > a

# Replace Using :

# a - Character
# b - Position
#  >> a

# Character to replace : r
# Replace with : y
# Replacing...
# Your new message is : happy human!
