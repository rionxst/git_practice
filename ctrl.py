class Control:

    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def calculate(self):
        try:
            num1 = float(self.view.le1.text())
            num2 = float(self.view.le2.text())
            operator = self.view.cb.currentText()

            if operator == "+":
                return f'{num1} + {num2} = {self.sum(num1, num2)}'
            elif operator == "-":
                return f'{num1} - {num2} = {self.sub(num1, num2)}'
            elif operator == "*":
                return f'{num1} * {num2} = {self.mul(num1, num2)}'
            elif operator == "/":
                return f'{num1} / {num2} = {self.div(num1, num2)}'
            elif operator == "^":
                return f'{num1} ^ {num2} = {self.pow(num1, num2)}'
            elif operator == "%":
                return f'{num1} % {num2} = {self.mod(num1, num2)}'
            else:
                return "Calculation Error"
        except:
             return "Calculation Error"

    def connectSignals(self):
        self.view.btn1.clicked.connect(lambda:self.view.setDisplay(self.calculate()))
        self.view.btn2.clicked.connect(self.view.clearMessage)

    def sum(self, a, b):
        try:
            return str(a+b)
        except:
            return "Calculation Error"
    
    def sub(self, a, b):
        return a-b
    
    def mul(self, a, b):
        return a*b

    def div(self, a, b):
        try:
            if (b==0):
                raise Exception("Divisor Error")
            
        except Exception as e:
            return e
        
        return a/b

    def pow(self, a, b):
        try:
            if(a==0):
                raise Exception("Base Error")
        except Exception as e:
            return e
    
        return pow(a, b)
    
    def mod(self, a, b):
        try:
            if(b==0):
                raise Exception("Base Error")
        except Exception as e:
            return e
        
        return a%b