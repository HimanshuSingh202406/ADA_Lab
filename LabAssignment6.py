def Duplicate(list1):

    uniqueList = []
    duplicateList = []

    for i in list1:
        if i not in uniqueList:
            uniqueList.append(i)
        elif i not in duplicateList:
            duplicateList.append(i)

    print(duplicateList)



List1 = [11, 44, 11, 2, 3, 6, 5, 1, 1, 44, 5, 6, 6, 8, 9, 9]
Duplicate(List1)
