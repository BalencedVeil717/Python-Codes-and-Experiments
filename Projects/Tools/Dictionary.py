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

# RESULT

# DICTIONARY


# Enter Word : wind
# Finding...

# [ NOUN ]
# -  Air moving (sometimes with considerable force
# -  A tendency or force that influences events
# -  Breath
# -  Empty rhetoric or insincere or exaggerated talk
# -  An indication of potential opportunity
# -  A musical instrument in which the sound is produced by an enclosed column of air that is moved by bellows or the human breath
# -  A reflex that expels intestinal gas through the anus
# -  The act of winding or twisting

# [ VERB ]
# -  To move or cause to move in a sinuous, spiral, or circular course
# -  Extend in curves and turns
# -  Arrange or or coil around
# -  Catch the scent of; get wind of
# -  Coil the spring of (some mechanical device
# -  Form into a wreath
# -  Raise or haul up with or as if with mechanical help

