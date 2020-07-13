import re

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    # def peek(self):
    #     if not self.isEmpty():
    #         return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class operator:
    def __init__(self, opr, level):
        self.opr = opr
        self.level = level

def handle_str(str):
    opr_stack = Stack()
    value_stack = Stack()
    for i in str:
        if re.match(r'[0-9]',i):
            str.index(r'/+?/-?/*?//?')
        functions = {'+': opr_stack.push(operator('+',1)),
                     '-': opr_stack.push(operator('-',1)),
                     '*': opr_stack.push(operator('*',2)),
                     '/': opr_stack.push(operator('/',2)),
                     '(': opr_stack.push(operator('(',3)),
                     ')': parenthesis_end(),}

        functions[i]()

def do_operation(string):

    return

def main():
    string = input("请输入需要运算的字符串：")
    result = do_operation(string)
    print("运算结果是：" + result)


if __name__ == '__main__':
    main()
