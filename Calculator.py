import tkinter
class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        master.minsize(width = 250, height = 300)
        self.p1 = tkinter.DoubleVar()
        self.p2 = tkinter.DoubleVar()
        self.solution = tkinter.DoubleVar()
        self.solution.set(0)
        self.p1.set(0)
        self.p2.set(0)
        self.part1 = tkinter.Entry(master, textvariable = self.p1, bg = "#FFFFFF", width = 20)
        self.part2 = tkinter.Entry(master, textvariable = self.p2, bg = "#FFFFFF", width = 20)
        self.answer = tkinter.Label(master, textvariable = self.solution, bg = "#FFFFFF", width = 40, bd = 2)
        self.part1.grid(row = 0, column = 0)
        self.part2.grid(row = 1, column = 0)
        self.answer.grid(row = 2, column = 0)
        self.add = tkinter.Button(master, text = '+', command = lambda: self.solve("add"), width = 7)
        self.subtract = tkinter.Button(master, text = '-', command = lambda: self.solve("subtract"), width = 7)
        self.divide = tkinter.Button(master, text = '/', command = lambda: self.solve("divide"), width = 7)
        self.multiply = tkinter.Button(master, text = '*', command = lambda: self.solve("multiply"), width = 7)
        self.power = tkinter.Button(master, text = '^', command = lambda: self.solve("power"), width = 7)
        self.power.grid(row = 2, column = 1)
        self.add.grid(row = 0, column = 1)
        self.subtract.grid(row = 0, column = 2)
        self.divide.grid(row = 1, column = 1)
        self.multiply.grid(row = 1, column = 2)
    def solve(self, method):
        if method == "add":
            self.solution.set(self.p1.get() + self.p2.get())
        elif method == "subtract":
            self.solution.set(self.p1.get() - self.p2.get())
        elif method == "divide":
            if self.p2.get() == 0:
                print("ERROR")
            else:    
                self.solution.set(self.p1.get() / self.p2.get())
        elif method == "power":
            self.solution.set(self.p1.get() ** self.p2.get())
        else:
            self.solution.set(self.p1.get() * self.p2.get())
root = tkinter.Tk()
Calc = Calculator(root)
root.mainloop()
