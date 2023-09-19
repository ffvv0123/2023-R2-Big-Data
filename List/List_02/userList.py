# 2023.09.19
# 빅데이터개론
# userList.py
# userListHeader의 메소드를 실행

import userListHeader

print()
list_a = [-1,-2,-3,-4,-5]
list_b = ['1','2','3','4','5']
str_a = "abcdefg"

print("list_a:", list_a)
print("list_b:", list_b)
print("str_a:", str_a)
print()

print("Zip list_a and list_b")
print(userListHeader.myZip(list_a, list_b))
print()

print("Zip list_a, list_b and str_a")
print(userListHeader.myZip(list_a, list_b, str_a))
print()

print("Enumterate list_b")
print(userListHeader.myEnumerate(list_b))
print()

## Enumerate and Zip operation
print("Enumerate Zip(list_a, list_b, str_a)")
enumerate_zip_list = userListHeader.myEnumerate(userListHeader.myZip(list_a, list_b, str_a))

for i in enumerate_zip_list:
    print(i[0], i[1])