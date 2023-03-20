
#№1
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if not bool(self.stack):
            return True
        else:
            return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)


#№2
check_list_1 = ['(','(','(','(','[','{','}',']',')',')',')',')']
check_list_2 = ['[','(','[',']',')','(','(','(','[','[','[',']',']',']',')',')',')',']','{','(',')','}']
check_list_3 = ['{','{','[','(',')',']','}','}']

check_list_no_1 = ['}','{',')']
check_list_no_2 = ['{','{','[','(',']',')',']','}','}']
check_list_no_3 = ['[','[','{','(',')',')','}',']']

check_lists_balance = [check_list_1, check_list_2, check_list_3, check_list_no_1, check_list_no_2, check_list_no_3]

check_dict = {'(': ')', '[': ']', '{': '}'}


def check_list(check_list):
    if len(check_list) % 2 == 1:
        return f'Несбалансированно'
    else:
        for symbol in check_list:
            if check_dict.get(symbol) != None:
                S.push(symbol)
                print(S.stack)
            else:
                last_symbol = S.peek()
                if check_dict.get(last_symbol) == symbol:
                    S.pop()
                    print(S.stack)
                else:
                    return f'Несбалансированно'

        S.is_empty()
        return f'Cбалансированно'

#Проверка на Сбалансированность
if __name__ == '__main__':
    S = Stack()
    for num in range(len(check_lists_balance)):
        check = check_list(check_lists_balance[num])
        print(check)
        print()



