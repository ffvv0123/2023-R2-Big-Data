# 2023.09.19
# 빅데이터개론
# userStackHeader.py
# empty, top, push, size, pop, print 함수를 구현

class Stack:

    ## __init__ 
    ## Attribute: <int> top, <list> data
    ## Stack에서 top은 초기값이 -1, data 리스트는 빈 리스트로 설정
    def __init__(self):
        self.top = -1
        self.data = []

    ## stackEmpty Method
    ## 비어있는 스택의 top은 -1 -> top이 -1인지 아닌지에 따라 True, False 결정
    def stackEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    ## stackTop Method
    ## Stack에서 top 번째 데이터를 리턴, 빈 스택이면 None 리턴
    def stackTop(self):
        if self.stackEmpty() == True:
            return None
        else:
            return self.data[self.top]
    
    ## stackPush Method
    ## Parameter: <type> value
    ## top을 1 증가시키고, 그 위치에 value 삽입
    def stackPush(self, value):
        self.top += 1
        self.data.append(value)
    
    ## stackSize Method
    ## Stack에서 크기를 리턴, 빈 스택이면 None 리턴
    ## 두 가지 방법이 있다
    ## 1. <list>의 len() 메서드를 사용하여 남아있는 data의 개수 반환 // return len(self.data)
    ## 2. top + 1을 리턴
    def stackSize(self):
        if self.stackEmpty() == True:
            return None
        else:
            return self.top + 1
        
    ## stackPop Method
    ## Stack이 비었다면 None 리턴, top의 data를 다른 변수에 저장. 이후에 top번째 데이터를 삭제하고 top을 줄인 후, 저장한 값 리턴
    def stackPop(self):
        if self.stackEmpty() == True:
            return None
        else:
            topStackData = self.data[self.top]
            del self.data[self.top]
            self.top -= 1
            return topStackData

    ## stackPrint Method
    ## Stack이 비었다면 Stack is empty 출력, 아니면 index와 value를 함께 출력
    def stackPrint(self):
        print("=" * 30)

        if self.stackEmpty() == True:
            print("Stack is empty") 
        else:
            print("index\tvalue")
            for i, v in enumerate(self.data):
                if i > self.top:
                    break
                print(i, "\t\b", v)