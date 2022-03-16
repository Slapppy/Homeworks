import re


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()


def append_tags(open_file, list_):
    with open(open_file, 'r') as file:
        f = file.read()
        tags = re.findall(r'<[^>]+>', f)
        for a in tags:
            list_.append(a)


def HTMLCheck(newfile):
    stack = Stack()
    list1 = []
    append_tags(newfile, list1)
    index = 0
    for ch in list1:
        if ch == '<div>':
            stack.push(ch)
        elif ch == '</div>':
            if stack.is_empty():
                return False
            else:
                stack.pop()
        if ch == '<p>':
            stack.push(ch)
        elif ch == '</p>':
            if stack.is_empty():
                return False
            else:
                stack.pop()
        if ch == '<h1>':
            stack.push(ch)
        elif ch == '</h1>':
            if stack.is_empty():
                return False
            else:
                stack.pop()
        index += 1

    return stack.is_empty()


print(HTMLCheck('test.html'))
