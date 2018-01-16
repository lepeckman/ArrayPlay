from __future__ import division


def intarray (strlist):
    intarray = []
    length = len(strlist)
    for i in range(length):
        numinlist = int(strlist[i])
        intarray.append(numinlist)
    return intarray  

def arraysum(intarray):
    length = len(intarray) 
    arraysum = 0
    for i in range(length): 
        element = intarray[i]     
        arraysum = arraysum + element
    return arraysum      

def arraymean(sum, length):
        arraymean = sum / length
        return arraymean

def greatestnum(intarray):
    length = len(intarray) 
    greatestnum = 0
    for i in range(length): 
        element = intarray[i]     
        if element > greatestnum:
            greatestnum = element
    return greatestnum        

def greatestind(intarray):
    length = len(intarray) 
    greatest = 0
    greatestind = []
    for i in range(length): 
        element = intarray[i]     
        if element > greatest:
            greatest = element     
        greatestind = intarray.index(greatest)
    return greatestind    
        

def main():
    textstr = raw_input("Type a list of numbers like the following: 1,2,3    -    ")
    strlist = textstr.split(",")
    convertedArray = intarray(strlist)
    total= arraysum(convertedArray)
    average = arraymean(total, len(convertedArray))
    largestNum = greatestnum(convertedArray)
    largestInd = greatestind(convertedArray)
    
    print(strlist) 
    print(convertedArray)

    print("Sum of numbers in list:")
    print(total)

    print("Mean of numbers in list:")
    print(average)
    
    print("The largest number is:")
    print(largestNum)
    
    print("The index of the largest number is:")
    print(largestInd)
    
    #print(("Your array, ") + str(print(intarray(strlist))) + (", results in a total of ") + str(print(arraysum(intarray(strlist)))) + (", an average of ") + str(print(arraymean(intarray(strlist)))) + (", and a highest value of ") + str(print(highest)) + (" at index ") + str(print(greatestind(intarray(strlist)))))
      
main()







