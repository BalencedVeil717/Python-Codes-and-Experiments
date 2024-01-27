import time


def dotX3():
    time.sleep(0.25)
    print(".", end="")
    time.sleep(0.25)
    print(".", end="")
    time.sleep(0.25)
    print(".")
    time.sleep(0.75)

def getMin():
    min = t[0]
    for i in range(1, len(t)):
        if min > t[i]:
            min = t[i]
    return min

def getMax():
    max = t[0]
    for i in range(1, len(t)):
        if max < t[i]:
            max = t[i]
    return max

            
print('')
print("FINDING MAXIMUM AND MINIMUM ELEMENTS OF TUPLE")
print("\n")

print("] TUPLE CREATION")
print()
t = []
n = int(input("Enter number of elements: "))
for i in range(n):
    e = int(input(f"Enter element {i+1}: "))
    t.append(e)
t = tuple(t)
print("[Minimum / Maximum] :")
print()
print("a - MINIMUM")
print("b - MAXIMUM")
ans = input(" > ")
print()
if ans.lower() == "a":
    min = getMin()
    print("Finding", end="")
    dotX3()
    print(f"[Minimum element = {min}] [Position :", (t.index(min) + 1), "]")
    time.sleep(0.5)
elif ans.lower() == "b":
    max = getMax()
    print("Finding", end="")
    dotX3()
    print(f"[Maximum element = {max}] [Position :", (t.index(max) + 1), "]")
    time.sleep(0.5)
else:
    print("Option not found, exiting")

# RESULT
        
# FINDING MAXIMUM AND MINIMUM ELEMENTS OF TUPLE


# ] TUPLE CREATION

# Enter number of elements: 7
# Enter element 1: 435
# Enter element 2: 6
# Enter element 3: 234
# Enter element 4: 455
# Enter element 5: 76
# Enter element 6: 234
# Enter element 7: 35 
# [Minimum / Maximum] :

# a - MINIMUM
# b - MAXIMUM
#  > b

# Finding...
# [Maximum element = 455] [Position : 4 ]
