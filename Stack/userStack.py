# 2023.09.19
# 빅데이터개론
# userStack.py
# userStackHeader의 메소드를 실행

import userStackHead

stack = userStackHead.Stack()

print()
print("Initiate stack")
stack.stackPrint()
print("Size of stack:", stack.stackSize())
print("Top of stack:", stack.stackTop())
print()

print("push 1, 2, and 3")
stack.stackPush(1)
stack.stackPush(2)
stack.stackPush(3)

stack.stackPrint()
print("Size of stack:", stack.stackSize())
print("Top of stack:", stack.stackTop())
print()

print("pop 2 times")
pop1 = stack.stackPop()
print("First pop:", pop1)
pop2 = stack.stackPop()
print("Second pop:", pop2)

stack.stackPrint()
print("Size of stack:", stack.stackSize())
print("Top of stack:", stack.stackTop())
print()

print("push 5, 7, and 10")
stack.stackPush(5)
stack.stackPush(7)
stack.stackPush(10)

stack.stackPrint()
print("Size of stack:", stack.stackSize())
print("Top of stack:", stack.stackTop())
print()

print("pop 5 times")
pop1 = stack.stackPop()
print("First pop:", pop1)
pop2 = stack.stackPop()
print("Second pop:", pop2)
pop3 = stack.stackPop()
print("Third pop:", pop3)
pop4 = stack.stackPop()
print("Fourth pop:", pop4)
pop5 = stack.stackPop()
print("Fifth pop:", pop5)

stack.stackPrint()
print("Size of stack:", stack.stackSize())
print("Top of stack:", stack.stackTop())
print()