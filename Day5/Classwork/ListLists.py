
listL = [1, ['a','b',['c', 'd', 'e', ['a','b',['c', 'd', 'e', 'f']]]], 'ni', 0.576]

listList = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

for i in range(0, len(listL)):
    if(isinstance(listL[i], list)):
        for j in range(0, len(listL[i])):
            print(listL[i][j])

    else:
        print(listL[i])

def listing(testList):
    for i in range(0, len(testList)):
        if(isinstance(testList[i],list)):
            listing(testList[i])
        else:
            print(testList[i])

listing(listL)
