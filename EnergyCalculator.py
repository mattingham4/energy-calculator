from tkinter import *
from tkinter import messagebox


class Appliance:
    def __init__(self, hours, watts, rate):
        self.hours = hours
        self.watts = watts
        self.rate = rate

    def calc(self, hours, watts, rate):
        global costlabel
        costlabel.grid_forget()

        if not hours or not watts or not rate:
            messagebox.showwarning("Warning!", "Please enter a number in each box.")
            costlabel = Label(root, text="Directions:\n"
                                         "Enter each value in\n"
                                         "the entry boxes in the\n"
                                         "units specified\n", relief=GROOVE, bg='beige', fg='#767575', bd=3, padx=0,
                              pady=0, justify=LEFT)
            costlabel.grid(row=3, column=1, rowspan=3, columnspan=1, sticky=W + E + N)

        elif not rate.isdigit() or not hours.isdigit() or not rate.isdigit:
            messagebox.showwarning("Warning!", "Please enter a number in each box.")
            costlabel = Label(root, text="Directions:\n"
                                         "Enter each value in\n"
                                         "the entry boxes in the\n"
                                         "units specified\n", relief=GROOVE, bg='beige', fg='#767575', bd=3, padx=0,
                              pady=0, justify=LEFT)
            costlabel.grid(row=3, column=1, rowspan=3, columnspan=1, sticky=W + E + N)

        else:
            cost = (float(hours) * float(watts)/1000 * float(rate))/100
            costlabel = Label(root, text="Your energy cost is:\n\n $" + str("{:.3f}".format(cost)),   relief=GROOVE, bg='beige', bd=3, padx=0,
                              pady=0, justify=LEFT)
            costlabel.grid(row=3, column=1, rowspan=3, columnspan=1, sticky=W + E + N)


def clear():
    global costlabel
    enterrate.delete(0, END)
    enterwatt.delete(0, END)
    enterhours.delete(0, END)
    costlabel.grid_forget()
    costlabel = Label(root, text="Directions:\n"
                                 "Enter each value in\n"
                                 "the entry boxes in the\n"
                                 "units specified\n", relief=GROOVE, bg='beige', fg='#767575', bd=3, padx=0, pady=0,
                      justify=LEFT)
    costlabel.grid(row=3, column=1, rowspan=3, columnspan=1, sticky=W + E + N)


root = Tk()
root.title("Energy Calculator")

ratelabel = Label(root, text="Enter your energy rate:", padx=2, pady=10, anchor=W)
enterrate = Entry(root)
unit1label = Label(root, text="¢/kWhr", anchor='e')
wattlabel = Label(root, text="Enter your machine's wattage:     ", padx=0, pady=10)
enterwatt = Entry(root)
unit2label = Label(root, text="W")
hourslabel = Label(root, text="Enter your running hours:", padx=0, pady=10)
enterhours = Entry(root)
unit3label = Label(root, text="hours")
costlabel = Label(root, text="Directions:\n"
                             "Enter each value in\n"
                             "the entry boxes in the\n"
                             "units specified\n",  relief=GROOVE, bg='beige', fg='#767575', bd=3, padx=0, pady=0, justify=LEFT)

ratelabel.grid(row=0, column=0, sticky=W)
enterrate.grid(row=0, column=1, sticky=E)
unit1label.grid(row=0, column=2, stick=W)
wattlabel.grid(row=1, column=0, sticky=W)
enterwatt.grid(row=1, column=1, sticky=E)
unit2label.grid(row=1, column=2, sticky=W)
hourslabel.grid(row=2, column=0, sticky=W)
enterhours.grid(row=2, column=1, sticky=E)
unit3label.grid(row=2, column=2, sticky=W)
costlabel.grid(row=3, column=1, rowspan=3, columnspan=1, sticky=W+E+N)

calcbutton = Button(root, text="Calculate", width=10, command=lambda: Appliance.calc(0, enterhours.get(),
                                                                           enterwatt.get(), enterrate.get()))
calcbutton.grid(row=3, column=0, columnspan=1, sticky=W, pady=10, padx=5)

clearbutton = Button(root, text="Clear", width=10, command=clear)
clearbutton.grid(row=4, column=0, columnspan=1, sticky=W, pady=10, padx=5)

exitbutton = Button(root, text="Exit", width=10, command=root.destroy)
exitbutton.grid(row=5, column=0, columnspan=1, sticky=W, pady=10, padx=5)

root.mainloop()
