import tkinter
import math
class FuncCalc:
    def __init__(self, master):
        self.master = master
        self.master.title("Function Calculator")
        master.minsize(width = 250, height = 300)
        self.eqtn = tkinter.StringVar()
        self.x1 = tkinter.DoubleVar()
        self.x2 = tkinter.DoubleVar()
        self.x3 = tkinter.DoubleVar()
        self.x4 = tkinter.DoubleVar()
        self.x5 = tkinter.DoubleVar()
        self.x6 = tkinter.DoubleVar()
        self.x7 = tkinter.DoubleVar()
        self.x8 = tkinter.DoubleVar()
        self.x9 = tkinter.DoubleVar()
        self.x10 = tkinter.DoubleVar()
        self.y1 = tkinter.DoubleVar()
        self.y2 = tkinter.DoubleVar()
        self.y3 = tkinter.DoubleVar()
        self.y4 = tkinter.DoubleVar()
        self.y5 = tkinter.DoubleVar()
        self.y6 = tkinter.DoubleVar()
        self.y7 = tkinter.DoubleVar()
        self.y8 = tkinter.DoubleVar()
        self.y9 = tkinter.DoubleVar()
        self.y10 = tkinter.DoubleVar()
        self.eqtn.set("x")
        self.input1 = tkinter.Label(master, textvariable = self.x1, bg = "#FFFFFF", width = 7)
        self.input2 = tkinter.Label(master, textvariable = self.x2, bg = "#FFFFFF", width = 7)
        self.input3 = tkinter.Label(master, textvariable = self.x3, bg = "#FFFFFF", width = 7)
        self.input4 = tkinter.Label(master, textvariable = self.x4, bg = "#FFFFFF", width = 7)
        self.input5 = tkinter.Label(master, textvariable = self.x5, bg = "#FFFFFF", width = 7)
        self.input6 = tkinter.Label(master, textvariable = self.x6, bg = "#FFFFFF", width = 7)
        self.input7 = tkinter.Label(master, textvariable = self.x7, bg = "#FFFFFF", width = 7)
        self.input8 = tkinter.Label(master, textvariable = self.x8, bg = "#FFFFFF", width = 7)
        self.input9 = tkinter.Label(master, textvariable = self.x9, bg = "#FFFFFF", width = 7)
        self.input10 = tkinter.Label(master, textvariable = self.x10, bg = "#FFFFFF", width = 7)
        self.output1 = tkinter.Label(master, textvariable = self.y1, bg = "#FFFFFF", width = 7)
        self.output2 = tkinter.Label(master, textvariable = self.y2, bg = "#FFFFFF", width = 7)
        self.output3 = tkinter.Label(master, textvariable = self.y3, bg = "#FFFFFF", width = 7)
        self.output4 = tkinter.Label(master, textvariable = self.y4, bg = "#FFFFFF", width = 7)
        self.output5 = tkinter.Label(master, textvariable = self.y5, bg = "#FFFFFF", width = 7)
        self.output6 = tkinter.Label(master, textvariable = self.y6, bg = "#FFFFFF", width = 7)
        self.output7 = tkinter.Label(master, textvariable = self.y7, bg = "#FFFFFF", width = 7)
        self.output8 = tkinter.Label(master, textvariable = self.y8, bg = "#FFFFFF", width = 7)
        self.output9 = tkinter.Label(master, textvariable = self.y9, bg = "#FFFFFF", width = 7)
        self.output10 = tkinter.Label(master, textvariable = self.y10, bg = "#FFFFFF", width = 7)
        self.input1.grid(column = 0, row = 1)
        self.input2.grid(column = 0, row = 2)
        self.input3.grid(column = 0, row = 3)
        self.input4.grid(column = 0, row = 4)
        self.input5.grid(column = 0, row = 5)
        self.input6.grid(column = 0, row = 6)
        self.input7.grid(column = 0, row = 7)
        self.input8.grid(column = 0, row = 8)
        self.input9.grid(column = 0, row = 9)
        self.input10.grid(column = 0, row = 10)
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
