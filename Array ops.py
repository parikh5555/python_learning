  if com[i][0] == 'append':   #append to last element
        myarr.append(int(com[i][1]))
    elif com[i][0] == 'print':  #Print arr
        print (myarr)
    elif com[i][0] == 'insert':  # Insert element to specific location
        myarr.insert(int(com[i][1]),(int(com[i][2])))
    elif com[i][0] == 'remove' : # Remove array from specific location
        myarr.remove(int(com[i][1]))
    elif com[i][0] == 'pop': #Remove last element
        myarr.pop()
    elif com[i][0] == 'reverse': #Reverse the array
        myarr = list(reversed(myarr))
    elif com[i][0] == 'sort':  # Sort the array
        myarr.sort()
