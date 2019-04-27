from tkinter import *
import datetime
now = datetime.datetime.now()
seconds = now.second
def main():
    # Main()
    my_window = Tk()
    my_window.title('MadLimb')
    my_window.configure(width=500, height=500, background="#9F9F9F")
    my_window.resizable(0, 0)


    def Ze_Warudo():
        Label(my_window, text="Enter a number", font="none 12 bold", bg="#9F9F9F").grid(row=8, column=0, sticky=E)
        x = Entry(my_window, width=30, bg="White")
        x.grid(row=9, column=0, sticky=E)
        Label(my_window, text="Enter a number", font="none 12 bold", bg="#9F9F9F").grid(row=10, column=0, sticky=E)
        y = Entry(my_window, width=30, bg="White")
        y.grid(row=11, column=0, sticky=E)

        def a():
            sum = float(x.get()) + float(y.get())
            Label(my_window, text=sum, font="none 12 bold", bg="#9F9F9F").grid(row=13, column=0, sticky=E)

        Button(my_window, text="Add", width=6, command=lambda: a()).grid(row=12, column=0, sticky=E)

    def Star_Platinum():
        Label(my_window, text="Enter a number", font="none 12 bold", bg="#9F9F9F").grid(row=8, column=0, sticky=E)
        x = Entry(my_window, width=30, bg="White")
        x.grid(row=9, column=0, sticky=E)
        Label(my_window, text="Enter a number", font="none 12 bold", bg="#9F9F9F").grid(row=10, column=0, sticky=E)
        y = Entry(my_window, width=30, bg="White")
        y.grid(row=11, column=0, sticky=E)

        def a():
            sub = float(x.get()) - float(y.get())
            Label(my_window, text=sub, font="none 12 bold", bg="#9F9F9F").grid(row=13, column=0, sticky=E)

        Button(my_window, text="Subtract", width=6, command=lambda: a()).grid(row=12, column=0, sticky=E)

    def Crazy_Diamond():
        Label(my_window, text="Enter a number", font="none 12 bold", bg="#9F9F9F").grid(row=8, column=0, sticky=E)
        x = Entry(my_window, width=30, bg="White")
        x.grid(row=9, column=0, sticky=E)
        Label(my_window, text="Enter a number", font="none 12 bold", bg="#9F9F9F").grid(row=10, column=0, sticky=E)
        y = Entry(my_window, width=30, bg="White")
        y.grid(row=11, column=0, sticky=E)

        def a():
            mult = float(x.get()) * float(y.get())
            Label(my_window, text=mult, font="none 12 bold", bg="#9F9F9F").grid(row=13, column=0, sticky=E)

        Button(my_window, text="Multiply", width=6, command=lambda: a()).grid(row=12, column=0, sticky=E)

    def Hamon():
        Label(my_window, text="Enter a number", font="none 12 bold", bg="#9F9F9F").grid(row=8, column=0, sticky=E)
        x = Entry(my_window, width=30, bg="White")
        x.grid(row=9, column=0, sticky=E)
        Label(my_window, text="Enter a number", font="none 12 bold", bg="#9F9F9F").grid(row=10, column=0, sticky=E)
        y = Entry(my_window, width=30, bg="White")
        y.grid(row=11, column=0, sticky=E)

        def a():
            zero = y.get()
            if zero != "0":
                div = float(x.get()) / float(y.get())
                Label(my_window, text=div, font="none 12 bold", bg="#9F9F9F").grid(row=13, column=0, sticky=E)
            else:
                my_window.destroy()

        Button(my_window, text="Divide", width=6, command=lambda: a()).grid(row=12, column=0, sticky=E)

    Button(my_window, text="Add", width=6, command=lambda: Ze_Warudo()).grid(row=1, column=0, sticky=E)
    Button(my_window, text="Subtract", width=6, command=lambda: Star_Platinum()).grid(row=2, column=0, sticky=E)
    Button(my_window, text="Multiply", width=6, command=lambda: Crazy_Diamond()).grid(row=3, column=0, sticky=E)
    Button(my_window, text="Divide", width=6, command=lambda: Hamon()).grid(row=4, column=0, sticky=E)

        # Alt+f4
    def close_window():
        close_window = my_window.destroy()
        exit()

    Button(my_window, text="Gold Experience Requiem", width=20, command=close_window).grid(row=21, column=0, sticky=E)

    # Killer Queen

    def killer_queen():
        my_window.destroy()
        exec(open("CalculatorGUI.pyw").read(), globals())
    label = Label(my_window, text=str(seconds))
    Button(my_window, text="Killer Queen", width=10, command=lambda: killer_queen()).grid(row=20, column=0, sticky=E)
    label.pack

    my_window.mainloop()


main()

