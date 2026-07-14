arrNum = [5, 7, 10, 15, 20]

arrNum[0] = 1
print(arrNum)  # Output: [1, 7, 10, 15, 20]

arrNum = [1, 2, 3, 4, [5, "test", True]]

print(arrNum[4][1])  # Output: test

print(arrNum[-1][2])  # Output: True

# add
arrNum.append(100) # add to end
print(arrNum)  # Output: [1, 2, 3, 4, [5, 'test', True], 100]

arrNum.insert(2, 50) # isert on index 
print(arrNum)  # Output: [1, 2, 50, 3, 4, [5, 'test', True], 100]

arrNum2 = [3, 1, 2, 5, 4]

arrNum2.sort() # sort the list

print(arrNum2)  # Output: [1, 2, 3, 4, 5]

arrNum2.reverse() # sort the list

print(arrNum2)  # Output: [5, 4, 3, 2, 1]

arrNum2.pop() # remove last element

arrNum2.remove(3) # remove element with value 3

print(arrNum2)  # Output: [5, 4, 2, 1]

arrNum2.clear() # remove all elements

print(len(arrNum2))

#for and arr

arrNum3 = [1, 2, 3, 4, 5]

for i in arrNum3:
    res = i * 2
    print(res)

# split text and any first letter do with hight regeister

test = 'one, two, three, four, five'

arrTextNum = test.split(', ')

for i in arrTextNum:
    arrTextNum = i.capitalize()
    print(arrTextNum)