import time

def dotX3():
    time.sleep(0.25)
    print(".", end="")
    time.sleep(0.25)
    print(".", end="")
    time.sleep(0.25)
    print(".")
    time.sleep(0.75)
def getMedian():
    ln = sorted(l)
    if (len(l)%2 == 0):
        mid = len(ln)//2
        median = (ln[mid -1] + ln[mid])//2
        return median
    else:
        mid = (len(ln) + 1)//2
        median = ln[mid - 1]
        return median
    
def getMode():
    mode = l[0]
    for i in range(1,len(l)):
        if (l.count(mode) < l.count(l[i])):
            mode = l[i]
    return mode

print()
print('FIND MEAN/MEDIAN/MODE OF LIST')
print('\n')

print("] List Creation")
print()
n = int(input("Enter number of elements in your list: "))
print()
l = []
print("Note: Please enter numbers only to avoid errors")
print()
for i in range(n):
    e = int(input(f"Enter element {i+1}: "))
    l.append(e)
print()

print('[ Choose Method] : ')
print('a - Mean')
print('b - Median')
print('c - Mode')
print('-'*20)
ans = input(" > ")
print()

if (ans.lower() == 'a'):
    print(' ] MEAN')
    mean = sum(l)/len(l)
    print('Calculating',end='')
    dotX3()
    print(f' - Mean : {mean}')
elif (ans.lower() == 'b'):
    print(' ] MEDIAN')
    median = getMedian()
    print('Calculating',end='')
    dotX3()
    print(f' - Median : {median}')
elif (ans.lower() == 'c'):
    print(' ] MODE')
    mode = getMode()
    print('Calculating',end='')
    dotX3()
    print(f' - Mode : {mode}')

# RESULT
    
# FIND MEAN/MEDIAN/MODE OF LIST


# ] List Creation


# FIND MEAN/MEDIAN/MODE OF LIST


# ] List Creation

# Enter number of elements in your list: 7

# Note: Please enter numbers only to avoid errors

# Enter element 1: 4
# Enter element 2: 45
# Enter element 3: 234
# Enter element 4: 45
# Enter element 5: 4 
# Enter element 6: 4
# Enter element 7: 46

# [ Choose Method] :
# a - Mean
# b - Median
# c - Mode
# --------------------
#  > c

#  ] MODE
# Calculating...
#  - Mode : 4
