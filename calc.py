class Calc(object):
    def __init__(self, expr):
        #expr - строка выражения 
        self.expr = expr
        self.dct_operations_priority = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, ')': 3}

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def add(self, a, b):
        return a + b
    def substract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a*b
    def devide(self, a, b):
        if b == 0:
            return 'Деление на 0 невозможно'
            #raise ZeroDivisionError('Деление на 0 невозможно')
        return a/b

    def convert_to_opz(self, string):
        expr = string.split()
        res = ''
        lst = []
        for el in expr:
            if self.is_number(el):
                res += el
                res += ' '
            elif el == '(':
                lst.append(el)
            elif el == ')':
                while len(lst) > 0 and lst[-1] != '(' :
                    a = lst.pop()
                    res += a
                    res += ' '
                    if len(lst) == 0:
                        return 'Некорректно расставлены скобки'
                        #raise ValueError('Некорректно расставлены скобки')
                b = lst.pop() #дб открывающая скобка
            elif el in self.dct_operations_priority:
                while len(lst) > 0 and \
                    self.dct_operations_priority[lst[-1]] != 0 and \
                    self.dct_operations_priority[lst[-1]] != 3 and \
                        ((self.dct_operations_priority[lst[-1]] >= self.dct_operations_priority[el]) or \
                        (el == '*' and self.dct_operations_priority[lst[-1]] == self.dct_operations_priority[el]) or\
                        (el == '/' and self.dct_operations_priority[lst[-1]] == self.dct_operations_priority[el])):
                        a = lst.pop()
                        res += a
                        res += ' '
                lst.append(el)
            else:
                return 'Введен некорректный символ или операция не поддерживается'
                #raise ValueError('Введен некорректный символ или операция не поддерживается')
        while len(lst) > 0:
            a = lst.pop()
            res += a
            res += ' '
        return res

    def __calculate_opz__(self):
        lst = []
        expr = self.convert_to_opz(self.expr)
        expr = expr.split()
        operations_dct = {'+': self.add, '-': self.substract, '*': self.multiply, '/': self.devide}
        for el in expr:
            if el in operations_dct:
                if len(lst) <2:
                    return 'Некорректное выражение, не хватает аргументов для бинарной операции'
                    #raise ValueError('Некорректное выражение, не хватает аргументов для бинарной операции')
                
                b = lst.pop()
                a = lst.pop()
                operation = operations_dct[el]
                lst.append(operation(a,b))
            elif self.is_number(el):
                lst.append(float(el))
            elif el == '(' or el == ')':
                return 'Некорректно расставлены скобки'
                #raise ValueError('Некорректно расставлены скобки')
            else:
                return 'Введен некорректный символ или операция не поддерживается'
                #raise ValueError('Введен некорректный символ или операция не поддерживается')
            
        if len(lst) > 1:
            print('Что-то пошло не так')
        return lst.pop()