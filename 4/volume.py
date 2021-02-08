def volume(length): #Calculate Volume
    try:
        length = float(length)
        if length > 0:
            return round(length**3, 6)
        else:
            raise TypeError
    except:
        return -1 #Returns -1 on failed input

if __name__ == "__main__":
    input = input("Enter a number: ")
    volume = volume(input)

    if volume > 0:
        print("The volume is: %f" % (volume))
    else:
        print("Error: Invalid input")
