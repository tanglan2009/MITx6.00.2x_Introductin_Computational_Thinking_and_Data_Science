class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []


# s = Stack()
# s.push(54)
# s.push(45)
# s.push("+")

# while not s.is_empty():
#     print s.pop()

# import string
# print string.split('Now is the time', ' ')
#
# import re
# print re.split('([^0-9])', '123+456*/abc')


def eval_postfix(expr):
    import re
    token_list = re.split("([^0-9])", expr)
    print token_list
    stack = Stack()
    for token in token_list:
        if token == '' or token == ' ':
            continue
        if token == '+':
            sum = stack.pop() + stack.pop()
            print sum
            stack.push(sum)
        elif token == '*':
            product = stack.pop() * stack.pop()
            stack.push(product)
        else:
            stack.push(int(token))

    return stack.pop()

print eval_postfix("56 47 +2 *")

# import re
# token_list = re.split("([^0-9])", "1 2 + 3 *")
# print token_list
# s = Stack()
# for token in token_list:
#     if token == '' or token == ' ':
#         continue
#     if token == '+':
#         sum = s.pop() + s.pop()
#         print sum
#         s.push(sum)
#     elif token == '*':
#         product = s.pop()*s.pop()
#         s.push(product)
#     else:
#         s.push(int(token))
# print s.pop()

print eval_postfix("1 + 2*3")
