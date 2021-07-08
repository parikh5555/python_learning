  if com[i][0] == 'append':
        myarr.append(int(com[i][1]))
    elif com[i][0] == 'print':
        print (myarr)
    elif com[i][0] == 'insert':
        myarr.insert(int(com[i][1]),(int(com[i][2])))
    elif com[i][0] == 'remove' :
        myarr.remove(int(com[i][1]))
    elif com[i][0] == 'pop':
        myarr.pop()
    elif com[i][0] == 'reverse':
        myarr = list(reversed(myarr))
    elif com[i][0] == 'sort':
        myarr.sort()
