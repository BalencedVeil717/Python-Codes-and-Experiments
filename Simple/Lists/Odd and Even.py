import time


print('')
print("CALCULATE NUMBER OF EVEN AND ODD ELEMENTS IN LIST")
print("\n")

print("] List Creation")
print()
n = int(input("Enter number of elements in your list: "))
l = []
print("Note: Please enter numbers only to avoid errors")
for i in range(n):
    e = int(input(f"Enter element {i+1}: "))
    l.append(e)
print()

time.sleep(0.50)
print("] Calculating", end="")
time.sleep(0.35)
print(".", end="")
time.sleep(0.35)
print(".", end="")
time.sleep(0.35)
print(".")
time.sleep(1)
print()

odd = even = 0
for i in l:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("> Even elements : ", even)
print("> Odd elements : ", odd)

# RESULT

# CALCULATE NUMBER OF EVEN AND ODD ELEMENTS IN LIST



# ] List Creation

# Enter number of elements in your list: 5
# Note: Please enter numbers only to avoid errors
# Enter element 1: 234
# Enter element 2: 554
# Enter element 3: 567
# Enter element 4: 883
# Enter element 5: 235

# ] Calculating...

# > Even elements :  2
# > Odd elements :  3