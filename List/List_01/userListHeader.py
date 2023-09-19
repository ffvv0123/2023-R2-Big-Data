# 2023.09.18
# 빅데이터개론
# userListHeader.py
# index, remove, len, append, reverse 함수를 직접 구현하고, 이를 통합한 CUI를 구현

"""
    myLen function
    parameter: <list> list
    list의 길이를 리턴
"""
def myLen(list):
    length = 0
    for _ in list:
        length += 1
    
    return length


"""
    myIndex function
    parameter: <list> list, <type> value
    list에서 value의 index를 찾아서 리턴, 값이 없다면 None 리턴
"""
def myIndex(list, value):
    index = 0

    for i in list:
        if i == value:
            return index
        else:
            index += 1

    if index == myLen(list):
        return None    
    

"""
    myReverse function
    parameter: <list> list
    list를 뒤집어서 리턴
"""
def myReverse(list):
    return list[::-1]


"""
    myRemove function
    parameter: <list> list, <type> value
    list에서 value의 index를 찾아서 삭제, 없으면 그대로
"""
def myRemove(list, value):
    index = myIndex(list, value)

    if index != None:
        list = list[0:index] + list[index+1:]

    return list


"""
    myAppend function
    parameter: <list> list, <type> value
    list에서 value를 마지막에 추가
"""
def myAppend(list, value):
    list += [value]

    return list

"""
    myListUI function
    parameter: <list> list
    앞서 구현한 연산을 실행할 수 있는 CUI
"""
def myListUI(list):
    while(True):
        option = int(input("Input option [1: print, 2: reverse, 3: length, 4: index, 5: append, 6: remove, 7: exit]: "))

        if option is 7:
            print("Exit myListUI...")
            break
        elif option is 1:
            print("myList:", list)
        elif option is 2:
            print("Reversed myList:", myReverse(list))
        elif option is 3:
            print("Length of myList:", myLen(list))
        elif option is 4:
            inputValue = int(input("Input value:"))
            print("Index of ", inputValue, "\b:", myIndex(list, inputValue))
        elif option is 5:
            inputValue = int(input("Input value:"))
            list = myAppend(list, inputValue)
            print("Append ", inputValue, "\b at myList:", list)
        elif option is 6:
            inputValue = int(input("Input value:"))
            list = myRemove(list, inputValue)
            print("Remove ", inputValue, "\b at myList:", list)
        else:
            print("Invalid input...")
            continue

        print("-"*90)

        