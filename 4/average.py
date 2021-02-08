def average(list): #Calculate Volume
    try:
        sum = 0
        for i in list:
            if not isinstance(i, float) and not isinstance(i, int):
                return False #Failed input
            sum += i
            
        return round(sum / len(list), 6)

    except:
        return False #Except from divide by zero

if __name__ == "__main__":
    print("Format: 1 2 3 4 5")
    input = input("Enter a list: ")
    try:
        list = [float(x) for x in input.split(" ")]
    except:
        list = []
        
    average = average(list)

    if average is not False:
        print("The average is: %f" % (average))
    else:
        print("Error: Invalid input")
