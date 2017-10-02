import tkinter
import math
class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        master.minsize(width = 250, height = 300)
        self.num1 = tkinter.DoubleVar()
        self.num2 = tkinter.DoubleVar()
        self.solution = tkinter.DoubleVar()
        self.solution.set(0)
        self.num1.set(0)
        self.num2.set(0)
        self.number1 = tkinter.Entry(master, textvariable = self.num1, bg = "#FFFFFF", width = 20)
        self.number2 = tkinter.Entry(master, textvariable = self.num2, bg = "#FFFFFF", width = 20)
        self.answer = tkinter.Label(master, textvariable = self.solution, bg = "#FFFFFF", width = 40, bd = 2)
        self.add = tkinter.Button(master, text = '+', command = lambda: self.solve("add"), width = 7)
        self.subtract = tkinter.Button(master, text = '-', command = lambda: self.solve("subtract"), width = 7)
        self.divide = tkinter.Button(master, text = '/', command = lambda: self.solve("divide"), width = 7)
        self.multiply = tkinter.Button(master, text = '*', command = lambda: self.solve("multiply"), width = 7)
        self.power = tkinter.Button(master, text = '^', command = lambda: self.solve("power"), width = 7)
        self.log = tkinter.Button(master, text = "log", command = lambda: self.solve("log"), width = 7)
        self.fact = tkinter.Button(master, text = '!', command = lambda: self.solve("fact"), width = 7)
        self.ans = tkinter.Button(master, text = "ans", command = lambda: self.solve("ans"), width = 7)
        self.func = tkinter.Button(master, text = "f(x)", command = lambda: self.solve("func"), width = 7)
        self.number1.grid(row = 0, column = 0)
        self.number2.grid(row = 1, column = 0)
        self.answer.grid(row = 2, column = 0)
        self.power.grid(row = 2, column = 1)
        self.add.grid(row = 0, column = 1)
        self.subtract.grid(row = 0, column = 2)
        self.divide.grid(row = 1, column = 1)
        self.multiply.grid(row = 1, column = 2)
        self.log.grid(row = 2, column = 2)
        self.fact.grid(row = 3, column = 1)
        self.ans.grid(row = 3, column = 2)
        self.func.grid(row = 4, column = 1)
    def solve(self, method):
        if method == "add":
            self.solution.set(self.num1.get() + self.num2.get())
        elif method == "subtract":
            self.solution.set(self.num1.get() - self.num2.get())
        elif method == "divide":
            if self.num2.get() == 0:
                self.solution.set("ERROR: DIVIDE BY ZERO")
            else:    
                self.solution.set(self.num1.get() / self.num2.get())
        elif method == "power":
            self.solution.set(self.num1.get() ** self.num2.get())
        elif method == "ans":
            self.num1.set(self.solution.get())
        elif method == "log":
            if self.num2.get() == 0 and self.num1.get() != 0:
                self.solution.set("ERROR")
            elif self.num2.get() == 1 and self.num1.get() != 1:
                self.solution.set("ERROR")
            elif self.num2.get() == 0 and self.num1.get() == 0:
                self.solution.set("ERROR: UNDEFINED VALUE") 
            else:
                self.solution.set(math.log(self.num1.get(), self.num2.get()))
        elif method == "fact":
            if self.num1.get() >= 0:
                self.solution.set(math.gamma(self.num1.get() + 1))
            else:
                self.solution.set(math.gamma(abs(self.num1.get() - 1)) * -1)
        else:
            self.solution.set(self.num1.get() * self.num2.get())
        if method == "func":
            child = tkinter.Tk()
            Func = FuncCalc(child)
            child.mainloop()
        if self.solution.get() % 1 == 0:
            self.solution.set(math.floor(self.solution.get()))
root = tkinter.Tk()
Calc = Calculator(root)
root.mainloop()
