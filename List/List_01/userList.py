# 2023.09.18
# 빅데이터개론
# userList.py
# userListHeader의 메소드를 실행

import userListHeader   # userListHeader에는 Main에서 실행될 연산이 포함

## Main ##

myList = [1, 2, 3, 4, 5, 6, 7]

print()
print("myList:", myList)
print("Reversed myList:",userListHeader.myReverse(myList))

print()
print("Length of myList:", userListHeader.myLen(myList))

print()
print("Index of 1:", userListHeader.myIndex(myList, 1))
print("Index of 3:",userListHeader.myIndex(myList, 3))
print("Index of 7:",userListHeader.myIndex(myList, 7))
print("Index of 30:",userListHeader.myIndex(myList, 30))

print()
myList = userListHeader.myRemove(myList, 30)
print("Remove 30 at myList:", myList)
myList = userListHeader.myRemove(myList, 3)
print("Remove 3 at myList:", myList)

print()
myList = userListHeader.myAppend(myList, 30)
print("Append 30 at myList:", myList)

print("Execute myListUI...")
userListHeader.myListUI(myList)