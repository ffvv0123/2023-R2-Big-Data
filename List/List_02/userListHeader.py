# 2023.09.19
# 빅데이터개론
# userListHeader.py
# zip, enumerate 함수를 구현

"""
    myZip function
    parameter: *args 가변인자, 매개변수의 수가 변할 수 있음
    여러 데이터가 합쳐진 형태를 튜플로 리턴 // list가 아니어도 묶을 수 있다
    이때 가장 짧은 길이의 데이터에 맞춤
"""
def myZip(*args):
    min_length = min(len(arg) for arg in args)  # len()은 이전에 구현했으니, 메소드를 바로 사용

    result = []
    for i in range(min_length):
        result.append(tuple(arg[i] for arg in args))

    return result

"""
    myEnumerate function
    parameter: <list> list_a
    여러 데이터가 합쳐진 형태를 리스트로 리턴
"""
def myEnumerate(list_a):
    index = 0
    enumerate_list = []

    for i in list_a:
        enumerate_list.append([index, i])
        index += 1

    return enumerate_list

