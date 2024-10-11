'1.'
x = [1, 2, 3, 4, 5]
y = []
z = []
y.append(x.pop(4))
y.append(x.pop(3))
z.append(x.pop(0))
z.append(x.pop(1))
z.append(x.pop())
z.sort()
print (y)
print (z)

'2.'
XInsertion = [1,2,21,33,45,65,12]
print("x without any sorting algrithm",XInsertion)
for i in range(1,len(XInsertion)):
    key = XInsertion[i]
    j = i -1
    while j >=0 and key > XInsertion[j]:
        XInsertion[ j+ 1 ]= XInsertion[j]
        j -= 1
    XInsertion[j+1]= key
print(XInsertion)

XSelection = [1,2,21,33,45,65,12]
for i in range(len(XSelection)):
    min_idx = i
    for j in range ( i + 1,len(XSelection)):
        if XSelection [ min_idx]> XSelection[j]:
            min_idx = j
        XSelection[i], XSelection[min_idx] = XSelection[min_idx] , XSelection[i]
print(XSelection)


