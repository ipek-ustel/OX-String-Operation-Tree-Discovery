def OX_to_tree(L):

    groups = []
    n = 0
    while n <= (len(L[0])):
        groups.append([])
        n += 1
    
    for word in L:
        if "o" not in word:
            groups[0] += [word]
        else:
            i = word.count("o")
            groups[i] += [word]
        
    subtree = []

    def checkifnotin(x, liste):
        for elem in liste:
            if type(elem) == str:
                if x == elem:
                    return False
            elif type(elem) == list:
                if x == elem[0]:
                    return False
        return True


    def subtreemaker(upperlist, lowerlist):
        for b in upperlist:
            listb = []
            listb.append(b)
            for a in lowerlist[::-1]:                       
                if type(a) == list:
                    if onediff(b, a[0]) and child(b, a[0]):
                        if checkifnotin(a[0], listb):
                            listb.append(a)
                            lowerlist.remove(a)
                if type(a) == str:
                    if onediff(b, a) and child(b, a):
                        if checkifnotin(a, listb):
                                listb.append(a)
                                lowerlist.remove(a)
            subtree.append(listb)

    def onediff(w1, w2):
        if w1.count("o") == w2.count("o") + 1:
            return True
        else: 
            return False
    
    def child(w1, w2):
        same = 0
        for i in range(len(w1)):
            if w1[i] == w2[i]:
                same += 1
        if same == len(w1)-1:
            return True
        else:
            return False
    
        
    for i in range(1, len(groups)):
        if subtree == [] and groups[i-1] != [] and groups[i] != []:
            subtreemaker(groups[i], groups[i-1])
        elif subtree == [] and groups[i-1] != [] and groups[i] == []:    
            return groups[i-1][0]
        elif subtree != [] and groups[i] != []:
            subtreemaker(groups[i], subtree)



    def helper(liste):
        result = []
        for a in liste:                            
            if type(a) == list and len(a) == 1:
                result.extend(a)
            elif type(a) == list and len(a) > 1:
                newa = [a[0]]
                for i in range(1,len(a)):
                    if type(a[i]) == list and len(a[i]) > 1:
                        newa.append(helper(a[i]))
                    elif type(a[i]) == list and len(a[i]) == 1:
                        newa.extend(a[i])
                    elif type(a[i]) == str:
                        newa.append(a[i])
                result.append(newa)
            elif type(a) != list:
                result.append(a)
        return result
    
    
    
    
    return helper(subtree[0])


