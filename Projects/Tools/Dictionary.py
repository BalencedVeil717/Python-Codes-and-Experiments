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

def properPrint(d):
    for topic in d.keys():
        print(d[topic])
    
print("")
print("DICTIONARY")
print("\n")

s = input("Enter Word : ")
print("Finding", end="")
dotX3()
d = dictionary.meaning(s)

d = {
    "Noun": [
        "air moving (sometimes with considerable force",
        "a tendency or force that influences events",
        "breath",
        "empty rhetoric or insincere or exaggerated talk",
        "an indication of potential opportunity",
        "a musical instrument in which the sound is produced by an enclosed column of air that is moved by bellows or the human breath",
        "a reflex that expels intestinal gas through the anus",
        "the act of winding or twisting",
    ],
    "Verb": [
        "to move or cause to move in a sinuous, spiral, or circular course",
        "extend in curves and turns",
        "arrange or or coil around",
        "catch the scent of; get wind of",
        "coil the spring of (some mechanical device",
        "form into a wreath",
        "raise or haul up with or as if with mechanical help",
    ],
}
