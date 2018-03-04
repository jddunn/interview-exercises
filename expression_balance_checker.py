
class Stack():

    def __init__(self, items=[]):
        self.items = items

    def push(self, val):
        self.items.append(val)

    def pop(self):
        top_val = self.items[len(self.items)-1]
        self.items = self.items[:-1]
        return top_val

    def is_empty(self):
        return self.items == []


def char_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1

    if balanced and s.is_empty():
        return True
    else:
        return False

def matches(open, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)

res = char_checker("{}())(")
print(res)