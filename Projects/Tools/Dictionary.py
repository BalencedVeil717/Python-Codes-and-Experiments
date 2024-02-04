from PyDictionary import PyDictionary
import time

dictionary = PyDictionary()


def dotX3():
    time.sleep(0.25)
    print(".", end="")
    time.sleep(0.25)
    print(".", end="")
    time.sleep(0.25)
    print(".")
    time.sleep(0.75)
    print()


def properPrint(d):
    for topic in d.keys():
        print(f"[ {topic.upper()} ]")
        for ln in d[topic]:
            print("- ", ln.capitalize())
            time.sleep(0.15)
        time.sleep(0.50)
        print()


print("")
print("DICTIONARY")
print("\n")

s = input("Enter Word : ")
print("Finding", end="")
dotX3()
d = dictionary.meaning(s)
properPrint(d)

