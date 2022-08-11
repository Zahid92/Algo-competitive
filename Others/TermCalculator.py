class Calculator:
    operator = []
    nums = []
    res = 0

    def get_precedence(self, ch):
        if ch == '+' or ch == '-':
            return 1
        return 2

    def is_operator(self, ch):
        return ch == '+' or ch == '-' or ch == '*' or ch == '/'

    def process_operator(self, op):
        a, b, r = 0, 0, 0
        if len(self.nums) > 0:
            a = self.nums.pop()
        else:
            print("aError")
            return
        if len(self.nums) > 0:
            b = self.nums.pop()
        else:
            print("bError")
            return
        if op == '*':
            r = a * b
        elif op == '/':
            r = a / b
        elif op == '+':
            r = a + b
        elif op == '-':
            r = a - b
        else:
            print("Invalid Operator")
            return
        self.nums.append(r)
        return

    def process_input(self, s):
        k = ""
        for i in s:
            if i.isnumeric():
                k += i
            else:
                if len(k):
                    self.nums.append(int(k))
                    k = ""
                if self.is_operator(i):
                    if len(self.operator) == 0 or self.get_precedence(i) > self.get_precedence(self.operator[-1]):
                        self.operator.append(i)
                    else:
                        while len(self.operator) > 0 and self.get_precedence(i) <= self.get_precedence(
                                self.operator[-1]):
                            to_process = self.operator[-1]
                            self.operator.pop()
                            self.process_operator(to_process)

                    self.operator.append(i)

                elif i == '(':
                    self.operator.append(i)
                elif i == ')':
                    while len(self.operator) > 0 and self.is_operator(self.operator[-1]):
                        to_process = self.operator[-1]
                        self.operator.pop()
                        self.process_operator(to_process)

                    if len(self.operator) > 0 and self.operator[-1] == '(':
                        self.operator.pop()
                    else:
                        print("Error: unbalanced parenthesis.")
        while len(self.operator) > 0 and self.is_operator(self.operator[-1]):
            to_process = self.operator[-1]
            self.operator.pop()
            self.process_operator(to_process)
        return self.nums[-1]


if __name__ == '__main__':
    n = input("Enter the expression :")
    n += "."
    k = Calculator()
    result = k.process_input(n)
    print(result)
