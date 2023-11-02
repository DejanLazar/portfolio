class cal:
    def add(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y
    def mult(self, x,y):
        return x*y
    def div(self,x,y):
        if y !=0:
            return x/y
        else:
            return ("You cannot divide by zero")
calc = cal()
while (True):
    try:
        x = float(input('Please enter a value of first number: '))
        y = float(input('Please enter a value of second number: '))
    except ValueError:
        print("You didn't enter a number, please enter it again")
        continue
    op = input("For addition enter +, for substraction enter -, for multiplication enter *," \
                "for division enter /, for end enter &, for new values enter any other key ")
    if op == '+':
        print('The result is: ', calc.add(x,y))
        continue
    elif op == '-':
        print('The result is: ',calc.sub(x,y))
        continue
    elif op == '*':
        print('The result is: ',calc.mult(x,y))
        continue
    elif op == '/':
        print('The result is: ',calc.div(x,y))
        continue
    elif op =='&':
        print("Goodbye")
        break
    else:
        continue