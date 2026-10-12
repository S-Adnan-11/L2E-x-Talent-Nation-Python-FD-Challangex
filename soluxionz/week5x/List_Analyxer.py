def ListAnalyzer():

    # listed = input("Enter list of numberz").split()

    listed = [12, 5, 27, 8, 14]
    minn = listed[0]
    maxx = listed[0]

    total = 0

    
    print (listed)


    for x in listed:
        total += x

        if x < minn:
            minn = x
        if x > maxx:
            maxx = x

    average = (total/len(listed))

    print("min: ", minn)
    print("while max: ", maxx)
    print("Total: ", total)
    print("Average: ", average)

    return listed


ListAnalyzer()