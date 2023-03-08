def listskills(val, list=[]):
    list.append(val)
    return list

list1 = listskills("nodeJs")
list2 = listskills("java",[])
list3 = listskills("reactJs")
print("%s" % list1)
print("%s" % list2)
print("%s" % list3)