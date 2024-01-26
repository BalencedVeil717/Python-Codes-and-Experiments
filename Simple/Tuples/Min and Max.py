# t = []
# n = int(input('Enter number of elements: '))
# for i in range(n):
#     e = int(input(f'Enter element {i+1}: '))
#     t.append(e)
# t = tuple(t)
# max = t[0]
# for i in range(1,len(t)):
#     if (max < t[i]):
#         max = t[i]
# print(max)
import time


def dotX3():
    time.sleep(0.25)
    print(".", end="")
    time.sleep(0.25)
    print(".", end="")
    time.sleep(0.25)
    print(".")
    time.sleep(0.75)


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
print("")
print("a - MINIMUM")
print("b - MAXIMUM")
ans = input(" > ")
print()
if ans.lower() == "a":
    min = t[0]
    for i in range(1, len(t)):
        if min > t[i]:
            min = t[i]
    print("Finding", end="")
    dotX3()
    print(f"[Minimum element = {min}] [Position :", (t.index(min) + 1), "]")
    time.sleep(0.5)
elif ans.lower() == "b":
    max = t[0]
    for i in range(1, len(t)):
        if max < t[i]:
            max = t[i]
    print("Finding", end="")
    dotX3()
    print(f"[Maximum element = {max}] [Position :", (t.index(max) + 1), "]")
    time.sleep(0.5)
else:
    print("Option not found, exiting")
