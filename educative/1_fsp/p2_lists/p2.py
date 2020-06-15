#Python Lists

my_list = [0,1,2]

#sublist = list[start_index: end_index]

'''
Start index is INCLUSIVE
End index is EXCLUSIVE
'''

print([1,2]+[3,4])

my_list = [1,2,4,8,10]

for val in my_list:
    print(val)

#input: [1,4,9,10,23]
#output: [1,4,9], [10,23]
def getSublist(my_list):
    my_list = [1,4,9,10,23]
    l1 = my_list[:3]
    l2 = my_list[3:]
    return [l1,l2]

def appendToList():
    my_list = [1,4,9,10,23]
    my_list += [90]
    my_list = my_list.append(90)
    return my_list

def getAverage():
    my_list = [1,4,9,10,23]
    avg = 0 
    for val in my_list:
        avg += val
    avg /= len(my_list)
    return avg

def getAverage():
    my_list = [1,4,9,10,23]
    sum1 = sum(my_list)
    return sum1/len(my_list)

def removeList():
    my_list = [1,4,9,10,23]
    my_list.remove(4)
    my_list.remove(9)
    return my_list

def removeList2():
    my_list = [1,4,9,10,23]
    l2 = [4,9]
    for num in range(len(l2)):
        my_list.remove(l2[num])
    return my_list

def removeList3():
    my_list = [1,4,9,10,23]
    l2 = [4,9]
    my_list.remove(l2[0])
    my_list.remove(l2[1])
    return my_list

def removeList4():
    l1 = [1,4,9,10,23]
    l2 = [4,9]
    for val in l2:
        l1.remove(val)
    return l1

print(removeList2())


