def checkInput(string):
    if len(string) == 0:
        return False
    for i in string:
        if not (i >= 'a' and i <= 'z') and not (i >= 'A' and i <= 'Z'):
            return False
    return True

def fullname(first, last):
    if checkInput(first) and checkInput(last):
        return first + " " + last
    return False

if __name__ == "__main__":
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")

    full = fullname(first, last)

    if full is not False:
        print("The full name is: %s" % full)
    else:
        print("Error: Invalid input")
