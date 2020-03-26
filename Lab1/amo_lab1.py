import tkinter as tk
from PIL import Image, ImageTk
from math import sqrt


class Main_Window:

    def __init__(self, root):
        self.root = root
        self.root.title('Menu')
        self.frame = tk.Frame(root)

        self.butnew('Algorithm 1', Algorithm_1)
        self.butnew('Algorithm 2', Algorithm_2)
        self.butnew('Algorithm 3', Algorithm_3)
        self.frame.pack()

    def butnew(self, text, _class,):
        tk.Button(self.frame, text=text, height=6, width=30,
                  command=lambda: self.new_window(_class)).pack()

    def new_window(self, _class):
        self.new = tk.Toplevel(self.root)
        self.app = _class(self.new)


class Algorithm_1:

    def __init__(self, master):
        self.master = master
        self.master.title('Algorithm_1')
        self.master.geometry('600x600')
        self.frame_left = tk.Frame(self.master)
        self.frame_left.pack(side=tk.LEFT)

        # Label
        self.label = tk.Label(self.frame_left,
                              text='Expression')
        self.label.grid(row=0, columnspan=2)

        # Variant
        self.img = ImageTk.PhotoImage(Image.open('pics/task1.png'))
        self.panel = tk.Label(self.frame_left)
        self.panel.image = self.img
        self.panel.configure(image=self.img)
        self.panel.grid(row=1, columnspan=2)

        # Label A
        self.label = tk.Label(self.frame_left,
                              text='Enter A')
        self.label.grid(row=2, column=0, padx=10, pady=20)
        # Entry A
        self.input_a = tk.StringVar()
        self.input_field_a = tk.Entry(self.frame_left,
                                      textvariable=self.input_a)
        self.input_field_a.grid(row=2, column=1, pady=20)

        # Label C
        self.label = tk.Label(self.frame_left,
                              text='Enter B')
        self.label.grid(row=3, column=0, padx=10, pady=20)
        # Entry  C
        self.input_c = tk.StringVar()
        self.input_field_c = tk.Entry(self.frame_left,
                                      textvariable=self.input_c)
        self.input_field_c.grid(row=3, column=1, pady=20)

        # Button Result
        self.button = tk.Button(self.frame_left, text='Result',
                                command=lambda: self.return_result
                                (self.input_a.get(), self.input_c.get()))
        self.button.grid(row=4, column=0, padx=10, pady=20)

        # Result
        self.result = tk.Label(self.frame_left, text=" ")
        self.result.grid(row=4, column=1, padx=10, pady=20)

        # Button Default
        self.button = tk.Button(self.frame_left, text='Default',
                                command=lambda: self.set_default())
        self.button.grid(row=5, column=0, padx=10, pady=20)

        # Right Frame
        self.frame_right = tk.Frame(self.master)
        self.frame_right.pack(side=tk.RIGHT)

        # Label
        self.label = tk.Label(self.frame_right,
                              text='Chart')
        self.label.pack()
        # Variant
        self.img = ImageTk.PhotoImage(Image.open('pics/chart1.png'))
        self.panel = tk.Label(self.frame_right, image=self.img)
        self.panel.pack()

    def return_result(self, a, c):
        try:
            self.result['text'] = self.get_answer(a, c)
        except:
            self.result['text'] = "Enter correct values"

    def get_answer(self, a, c):
        a = float(a)
        c = float(c)
        return sqrt(a+c) + 1/(a+c)

    def set_default(self):
        self.input_field_a.insert(tk.END, '3')
        self.input_field_c.insert(tk.END, '5')


class Algorithm_2:

    def __init__(self, master):
        self.master = master
        self.master.title('Algorithm_2')
        self.master.geometry('700x700')
        self.frame_left = tk.Frame(self.master)
        self.frame_left.pack(side=tk.LEFT)

        # Label Expression
        self.label = tk.Label(self.frame_left,
                              text='Expression')
        self.label.grid(row=0, columnspan=2)

        # Variant
        self.img = ImageTk.PhotoImage(Image.open('pics/task2.png'))
        self.panel = tk.Label(self.frame_left)
        self.panel.image = self.img
        self.panel.configure(image=self.img)
        self.panel.grid(row=1, columnspan=2)

        # Label A
        self.label = tk.Label(self.frame_left,
                              text='Enter A')
        self.label.grid(row=2, column=0, padx=10, pady=20)
        # Entry A
        self.input_a = tk.StringVar()
        self.input_field_a = tk.Entry(self.frame_left,
                                      textvariable=self.input_a)
        self.input_field_a.grid(row=2, column=1, pady=20)

        # Label B
        self.label = tk.Label(self.frame_left,
                              text='Enter B')
        self.label.grid(row=3, column=0, padx=10, pady=20)
        # Entry B
        self.input_b = tk.StringVar()
        self.input_field_b = tk.Entry(self.frame_left,
                                      textvariable=self.input_b)
        self.input_field_b.grid(row=3, column=1, pady=20)

        # Label C
        self.label = tk.Label(self.frame_left,
                              text='Enter C')
        self.label.grid(row=4, column=0, padx=10, pady=20)
        # Entry C
        self.input_c = tk.StringVar()
        self.input_field_c = tk.Entry(self.frame_left,
                                      textvariable=self.input_c)
        self.input_field_c.grid(row=4, column=1, pady=20)

        # Label Result
        self.button = tk.Button(self.frame_left, text='Result',
                                command=lambda: self.return_result
                                (self.input_a.get(), self.input_b.get(),
                                 self.input_c.get()))
        self.button.grid(row=5, column=0, padx=10, pady=20)

        # Result
        self.result = tk.Label(self.frame_left, text=" ")
        self.result.grid(row=5, column=1, padx=10, pady=20)

        # Right Frame
        self.frame_right = tk.Frame(self.master)
        self.frame_right.pack(side=tk.RIGHT)

        # Label Chart
        self.label = tk.Label(self.frame_right,
                              text='Chart')
        self.label.pack()
        # Variant
        self.img = ImageTk.PhotoImage(Image.open('pics/chart2.png'))
        self.panel = tk.Label(self.frame_right, image=self.img)
        self.panel.pack()

        # Button Default
        self.button = tk.Button(self.frame_left, text='Default',
                                command=lambda: self.set_default())
        self.button.grid(row=6, column=0, padx=10, pady=20)

    def return_result(self, a, b, c):
        try:
            self.result['text'] = self.get_answer(a, b, c)
        except:
            self.result['text'] = "Enter correct values"

    def get_answer(self, a, b, c):
        a = float(a)
        b = float(b)
        c = float(c)
        D = b**2 - 4*a*c
        if D < 0:
            return 'None'
        if abs(D) < 0.0001:
            return ('x = {0:.2f}'.format(b / 2))
        x1 = (b - sqrt(D)) / 2
        x2 = (b + sqrt(D)) / 2

        return ('x1 = {}\nx2 = {}'.format(round(x1, 3), round(x2, 3)))

    def set_default(self):
        self.input_field_a.insert(tk.END, '57.567')
        self.input_field_b.insert(tk.END, '11.675')
        self.input_field_c.insert(tk.END, '34.114')


class Algorithm_3:

    def __init__(self, master):
        self.master = master
        self.master.title('Algorithm_3')
        self.master.geometry('900x750')
        self.frame_left = tk.Frame(self.master)
        self.frame_left.pack(side=tk.LEFT)

        # Label Expression
        self.label = tk.Label(self.frame_left,
                              text='Expression')
        self.label.grid(row=0, columnspan=2)

        # Variant
        self.img = ImageTk.PhotoImage(Image.open('pics/task3.png'))
        self.panel = tk.Label(self.frame_left)
        self.panel.image = self.img
        self.panel.configure(image=self.img)
        self.panel.grid(row=1, columnspan=2)

        # Label F
        self.label = tk.Label(self.frame_left,
                              text='Enter F')
        self.label.grid(row=2, column=0, padx=10, pady=20)
        # Entry F
        self.input_f = tk.StringVar()
        self.input_field_f = tk.Entry(self.frame_left,
                                      textvariable=self.input_f)
        self.input_field_f.grid(row=2, column=1, pady=20)

        # Label A
        self.label = tk.Label(self.frame_left,
                              text='Enter A (10 numbers saperated with spaces)')
        self.label.grid(row=3, column=0, padx=10, pady=20)
        # Entry A
        self.input_a = tk.StringVar()
        self.input_field_a = tk.Entry(self.frame_left,
                                      textvariable=self.input_a)
        self.input_field_a.grid(row=3, column=1, pady=20)

        # Label C
        self.label = tk.Label(self.frame_left,
                              text='Enter C (10 numbers saperated with spaces)')
        self.label.grid(row=4, column=0, padx=10, pady=20)
        # Entry C
        self.input_c = tk.StringVar()
        self.input_field_c = tk.Entry(self.frame_left,
                                      textvariable=self.input_c)
        self.input_field_c.grid(row=4, column=1, pady=20)

        # Label G
        self.label = tk.Label(self.frame_left,
                              text='Enter G (10 numbers saperated with spaces)')
        self.label.grid(row=5, column=0, padx=10, pady=20)
        # Entry G
        self.input_g = tk.StringVar()
        self.input_field_g = tk.Entry(self.frame_left,
                                      textvariable=self.input_g)
        self.input_field_g.grid(row=5, column=1, pady=20)

        # Label Result
        self.button = tk.Button(self.frame_left, text='Result',
                                command=lambda: self.return_result
                                (self.input_f.get(), self.input_a.get(),
                                 self.input_c.get(), self.input_g.get()))
        self.button.grid(row=6, column=0, padx=10, pady=20)

        # Result
        self.result = tk.Label(self.frame_left, text=" ")
        self.result.grid(row=6, column=1, padx=10, pady=20)

        # Right Frame
        self.frame_right = tk.Frame(self.master)
        self.frame_right.pack(side=tk.RIGHT)

        # Label Chart
        self.label = tk.Label(self.frame_right,
                              text='Chart')
        self.label.pack()
        # Variant
        self.img = ImageTk.PhotoImage(Image.open('pics/chart3.png'))
        self.panel = tk.Label(self.frame_right, image=self.img)
        self.panel.pack()

        # Button Default
        self.button = tk.Button(self.frame_left, text='Default',
                                command=lambda: self.set_default())
        self.button.grid(row=7, column=0, padx=10, pady=20)

    def return_result(self, f, a, c, g):
        try:
            self.result['text'] = self.get_answer(f, a, c, g)
        except:
            self.result['text'] = "Enter correct values"

    def get_answer(self, f, a, c, g):
        f = float(f)
        a = list(map(float, a.split()))
        c = list(map(float, c.split()))
        g = list(map(float, g.split()))

        for i in range(10):
            f += a[i]**2 + 56*c[i]*f*g[i]
        return 'F = {}'.format(round(f, 3))

    def set_default(self):
        self.input_field_f.insert(tk.END, '3')
        self.input_field_a.insert(tk.END, '1 2 3 4 5 6 7 8 9 0')
        self.input_field_c.insert(tk.END, '3 4 5 6 7 8 9 0 1 2')
        self.input_field_g.insert(tk.END, '6 5 4 3 2 1 0 9 8 7')


app = tk.Tk()

Main_Window(app)

app.mainloop()
