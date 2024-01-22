s = input("Enter String: ")
print()
print("Replace / Remove")
print("a - Replace")
print("b - Remove")
ans = input()
if ans.lower() == "a":
    print("Replace Using")
    print()
    print("a - Character")
    print("b - Position")
    ans = input()
    if ans.lower() == "a":
        rem = input("Enter character to replace: ")
        add = input("Enter character to replace with: ")
        s = s.replace(rem, add)
        print(f"Your new string is: {s}")
    elif ans.lower() == "b":
        rem = int(input("Enter position of character to remove: "))
        add = input("Enter character to replace with: ")
        s = s.replace(s[rem - 1], add)
        print(f"Your new string is: {s}")
    else:
        print("Option not found, exiting")
        exit()

elif ans.lower() == "b":
    print("Remove Using")
    print()
    print("a - Character")
    print("b - Position")
    ans = input()
    if ans.lower() == "a":
        rem = input("Enter character to remove: ")
        s = s.replace(rem, "")
        print(f"Your new string is: {s}")
    elif ans.lower() == "b":
        rem = int(input("Enter position of character to remove: "))
        s = s.replace(s[rem - 1], "")
        print(f"Your new string is: {s}")
