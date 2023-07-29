class Stack:
    def __init__(self):
        self.inside = []

    def is_empty(self) -> bool:
        if len(self.inside) == 0:
            return True
        else:
            return False
        
    def push(self, element):
        self.inside.insert(0, element)

    def pop(self):
        if not self.is_empty():
            return self.inside.pop(0)
        else:
            return "No elements in stack"
    
    def peek(self):
        if not self.is_empty():
            return self.inside[0]
        else:
            return "No elements in stack"
    
    def size(self):
        return len(self.inside)
    
    def balanced_brackets(self):
        bracket_list = []
        for item in self.inside[0]:
            if item in ['[', '(', '{']:
                bracket_list.append(item)
            else:
                if item == ')' and '(' in bracket_list:
                    bracket_list.remove('(')
                elif item == '}' and '{' in bracket_list:
                    bracket_list.remove('{')
                elif item == ']' and '[' in bracket_list:
                    bracket_list.remove('[')
                else:
                    return 'Unbalanced'
        return 'Balanced'


my_stack = Stack()
print(my_stack.is_empty())
my_stack.push('[([])((([[[]]])))]{()}')
print(my_stack.balanced_brackets())
my_stack.push('(((([{}]))))')
print(my_stack.balanced_brackets())
my_stack.push('{{[()]}}')
print(my_stack.balanced_brackets())
my_stack.push('{{[(])]}}')
print(my_stack.balanced_brackets())
my_stack.push('[[{())}]')
print(my_stack.balanced_brackets())
my_stack.push('}{}')
print(my_stack.balanced_brackets())
print(my_stack.inside)
