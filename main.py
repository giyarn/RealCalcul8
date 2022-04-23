import math
from tkinter import*
from PIL import ImageTk,Image
from math import*
from tkinter import messagebox
from tkinter import ttk

window = Tk()
window.geometry('840x500')
window.resizable(False,False)
global counter
counter = 1

def arithmetic():
    global  counter
    if counter < 5:
        arithmetic_window = Toplevel()
        arithmetic_window.title("Arithmetic Sequence")
        arithmetic_window.resizable(False, False)
        arithmetic_window.geometry('840x500')

        global arithmetic_image
        arithmetic_image = PhotoImage(file='numbers/arithmetic bg.png')
        arithmetic_canvas = Canvas(arithmetic_window, width=800, height=500)
        arithmetic_canvas.pack(fill='both', expand=True)
        arithmetic_canvas.create_image(0, 0, image=arithmetic_image, anchor=NW)
        arithmetic_canvas.create_text(650, 30, text="Number Sequence", font=("Lemonade Stand", 30))

        arithmetic_canvas.create_text(260,90,text="Enter the sequence", font=("Lemonade Stand", 15))

        def arith_calculate():
            valid = 0
            if entry1.get() != " ":
                try:
                    a1 = float(entry1.get())
                    valid = 1
                except ValueError as e:
                    messagebox.showinfo("Value Error", "Input must be a number")
                    entry1.delete(0,END)
                    entry1.focus()
                if valid == 1:
                    nq_term1ans_label.configure(text=a1)
            if entry2.get() != " ":
                try:
                    d = float(entry2.get()) - float(entry1.get())
                    valid = 1
                except ValueError as e:
                    messagebox.showinfo("Value Error", "Input must be a number")
                    entry2.delete(0,END)
                    entry2.focus()
                if entry3.get() != "":
                    try:
                        a3 = float(entry3.get())
                    except ValueError as e:
                        messagebox.showinfo("Value Error", "Input must be a number")
                        entry3.delete(0, END)
                        entry3.focus()
                if entry4.get() != "":
                    try:
                        a4 = float(entry4.get())
                        valid = 1
                    except ValueError as e:
                        messagebox.showinfo("Value Error", "Input must be a number")
                        entry4.delete(0, END)
                        entry4.focus()
                if entry5.get() != "":
                    try:
                        a5 = float(entry5.get())
                        valid = 1
                    except ValueError as e:
                        messagebox.showinfo("Value Error", "Input must be a number")
                        entry5.delete(0, END)
                        entry5.focus()
                #if float(entry2.get()) - float(entry1.get()) != float(entry3.get()) - float(entry2.get()) and float(entry5.get()) - float(entry4.get()) != float(entry4.get()) - float(entry3.get()):
                   messagebox.showinfo("Error", "this is not a Aritmetic sequence")
                    entry1.delete(0, END)
                    entry2.delete(0, END)
                    entry3.delete(0, END)
                    entry4.delete(0, END)
                    entry5.delete(0, END)
                    nq_n_entry.delete(0, END)
                    entry1.focus()
                    entry2.focus()
                    entry4.focus()
                    entry3.focus()
                    entry5.focus()
                    nq_n_entry.focus()
                else:
                    if valid == 1:
                        nq_dans_label.configure(text=d)

            if nq_n_entry.get() != "":
                valid =0
                try:
                    n = float(nq_n_entry.get())
                    valid = 1
                except ValueError as e:
                    messagebox.showinfo("Value Error", "Input must be a number")
                    nq_n_entry.delete(0,END)
                    nq_n_entry.focus()

                if valid == 1:
                    an = a1 + (n-1)*d
                    sn = (n/2)*((2*a1) + ((n-1)*d))
                    nq_anansw_label.configure(text=an)
                    nq_snansw_label.configure(text=sn)



        #term1
        nq_term1_label = Label(arithmetic_window,text="a₁:", font=("Give Away",20),bg="#FEFAEE")
        nq_term1label_window = arithmetic_canvas.create_window(200,350,window=nq_term1_label)
        nq_term1ans_label = Label(arithmetic_window,text=" ",font=("Give Away",20))
        n1_term1entry_window = arithmetic_canvas.create_window(260,350,window=nq_term1ans_label)
        arithmetic_canvas.create_text(375, 350, text="---first term", font=("Give Away", 17))
        #commondiff
        nq_d_label = Label(arithmetic_window,text="d:", font=("Give Away",20),bg="#FEFAEE")
        nq_dlabel_window = arithmetic_canvas.create_window(200,300,window=nq_d_label)
        nq_dans_label = Label(arithmetic_window,text=" ",font=("Give Away",20))
        n1_dlabel_window = arithmetic_canvas.create_window(260,300,window=nq_dans_label)
        arithmetic_canvas.create_text(420, 300, text="---common difference", font=("Give Away", 17))
        #nth
        nq_n_label = Label(arithmetic_window,text="n:", font=("Give Away",20),bg="#FEFAEE")
        nq_nlabel_window = arithmetic_canvas.create_window(200,250,window=nq_n_label)
        nq_n_entry = Entry(arithmetic_window,borderwidth=3,width=6,font=("Give Away",20))
        n1_nentry_window = arithmetic_canvas.create_window(260,250,window=nq_n_entry)
        arithmetic_canvas.create_text(410,250,text="----number of terms",font=("Give Away",17))
        #an
        nq_an_label = Label(arithmetic_window,text="an:", font=("Give Away",20),bg="#FEFAEE")
        nq_anlabel_window = arithmetic_canvas.create_window(200,400,window=nq_an_label)
        nq_anansw_label = Label(arithmetic_window,text=" ",font=("Give Away",20))
        nq_anlabel_window = arithmetic_canvas.create_window(260,400,window=nq_anansw_label)
        arithmetic_canvas.create_text(375, 400, text="---nth term", font=("Give Away", 17))
        #sn
        nq_sn_label = Label(arithmetic_window,text="Sn:", font=("Give Away",20),bg="#FEFAEE")
        nq_snlabel_window = arithmetic_canvas.create_window(200,450,window=nq_sn_label)
        nq_snansw_label = Label(arithmetic_window,text=" ",font=("Give Away",20))
        n1_snlabel_window = arithmetic_canvas.create_window(260,450,window=nq_snansw_label)
        arithmetic_canvas.create_text(430, 450, text="---sum of all the terms", font=("Give Away", 17))
        #entryboxes

        entry1 = Entry(arithmetic_window,borderwidth=3,width=3, font=("Give Away",20))
        entry1_window= arithmetic_canvas.create_window(220,150,window=entry1)
        entry2 = Entry(arithmetic_window, borderwidth=3, width=3, font=("Give Away", 20))
        entry2_window = arithmetic_canvas.create_window(280, 150, window=entry2)
        entry3 = Entry(arithmetic_window, borderwidth=3, width=3, font=("Give Away", 20))
        entry3_window = arithmetic_canvas.create_window(340, 150, window=entry3)
        entry4 = Entry(arithmetic_window, borderwidth=3, width=3, font=("Give Away", 20))
        entry4_window = arithmetic_canvas.create_window(400, 150, window=entry4)
        entry5 = Entry(arithmetic_window, borderwidth=3, width=3, font=("Give Away", 20))
        entry5_window = arithmetic_canvas.create_window(460, 150, window=entry5)
        arithmetic_canvas.create_text(490, 150, text=". . . . . . . . . . . .", font=("Give Away", 23))
        #buttoncalcul8
        abutton_calcul8 = Button(arithmetic_window, text="Calcul8",bg="#f2cd2f", font=("Lemonade Stand", 10), borderwidth=10,command=arith_calculate)
        arithmetic_canvas.create_window(640,440,window=abutton_calcul8)
        abutton_clear = Button(arithmetic_window, text="Clear", bg="red", font=("Lemonade Stand", 10),borderwidth=10)
        arithmetic_canvas.create_window(730, 440, window=abutton_clear)




        counter +=1
    else:
        messagebox.showinfo("Error","A Window is running")
        counter -=1


def perimeter():
    global counter
    if counter < 5:
        perimeter_window = Toplevel()
        perimeter_window.title("Perimeter")
        perimeter_window.resizable(False,False)
        perimeter_window.geometry('840x500')

        global perimeter_image
        perimeter_image = PhotoImage(file='numbers/perimeterbg.png')
        perimeter_canvas = Canvas(perimeter_window, width=800, height=500)
        perimeter_canvas.pack(fill='both', expand=True)
        perimeter_canvas.create_image(0, 0, image=perimeter_image, anchor=NW)
        perimeter_canvas.create_text(370, 50, text="Perimeter", font=("Lemonade Stand", 30))

        def per_clear():
            P_entry_box1.delete(0,END)
            P_entry_box2.delete(0, END)
            P_entry_box3.delete(0, END)
            perimeter_answer_label.configure(text = " ")
        def per_calculate(shape):
            if shape == "triangle":
                if P_entry_box1.get() != " ":
                    valid = 0
                    try:
                        A = float(P_entry_box1.get())
                        valid = 1
                    except ValueError as e:
                        messagebox.showinfo("Value Error", "PLease input a Number")
                        P_entry_box1.delete(0, END)
                        P_entry_box1.focus()
                if P_entry_box1.get() != " " and valid == 1:
                    try:
                        B = float(P_entry_box2.get())
                        valid = 2
                    except ValueError as e:
                        messagebox.showinfo("Value Error", "PLease input a Number")
                        P_entry_box2.delete(0, END)
                        P_entry_box2.focus()
                if P_entry_box1.get() != " " and valid == 2:
                    try:
                        C = float(P_entry_box3.get())
                        valid = 3
                    except ValueError as e:
                        messagebox.showinfo("Value Error", "PLease input a Number")
                        P_entry_box3.delete(0, END)
                        P_entry_box3.focus()
                if valid == 3:
                    total = A + B + C
                    total = round(total, 2)
                    perimeter_answer_label.configure(text=total)

            if shape == "square":
                if P_entry_box1.get() != " ":
                    valid =0
                    try:
                        s = float(P_entry_box1.get())
                        valid = 1
                    except ValueError as e:
                        messagebox.showinfo("Value Error", "PLease input a Number")
                        P_entry_box1.delete(0, END)
                        P_entry_box1.focus()
                if valid == 1:
                    total = 4*s
                    total = round(total, 2)
                    perimeter_answer_label.configure(text=total)

            if shape == "rectangle":
                if P_entry_box1.get() != " ":
                    valid=0
                    try:
                        l = float(P_entry_box1.get())
                        valid = 1
                    except ValueError as e:
                        messagebox.showinfo("Value Error", "PLease input a Number")
                        P_entry_box1.delete(0, END)
                        P_entry_box1.focus()
                if P_entry_box1.get() != " " and valid == 1:
                    try:
                        w = float(P_entry_box2.get())
                        valid = 2
                    except ValueError as e:
                        messagebox.showinfo("Value Error", "PLease input a Number")
                        P_entry_box2.delete(0, END)
                        P_entry_box2.focus()
                if valid == 2:
                    total = (2*l) + (2*w)
                    total = round(total, 2)
                    perimeter_answer_label.configure(text=total)

            if shape == "circle":
                if P_entry_box1.get() != " ":
                    valid = 0
                    try:
                        r = float(P_entry_box1.get())
                        valid = 1
                    except ValueError as e:
                        messagebox.showinfo("Value Error", "PLease input a Number")
                        P_entry_box1.delete(0, END)
                        P_entry_box1.focus()
                if valid == 1:
                    total = 2*3.14*r
                    total = round(total,2)
                    perimeter_answer_label.configure(text=total)

        def per_operation(event):
            global per_shape_name
            global per_shape

            if (perimeter_combo.get()=="Triangle"):
                per_shape_name = "triangle"
                per_shape_label.configure(text="Triangle")
                per_shape = PhotoImage(file='numbers/ptriangle.png')
                plabel = Label(perimeter_canvas,image=per_shape)
                perimeter_canvas.create_window(680,230,window=plabel)
                per_formula_label.configure(text="Formula: A + B + C")

                P_entry_box1_label.configure(text="A:")
                P_entry_box1.configure(state=NORMAL)
                P_entry_box1_label.configure(font=("Lemonade Stand", 20))
                P_entry_box2_label.configure(font=("Lemonade Stand", 20))
                P_entry_box3_label.configure(font=("Lemonade Stand", 20))
                P_entry_box2_label.configure(text="B:")
                P_entry_box2.configure(state=NORMAL)
                P_entry_box3_label.configure(text="C:")
                P_entry_box3.configure(state=NORMAL)

                per_button_calcul8.configure(state=NORMAL)



            elif (perimeter_combo.get()=="Square"):
                per_shape_name = "square"
                per_shape_label.configure(text="Square")
                per_shape = PhotoImage(file='numbers/psquare.png')
                plabel = Label(perimeter_canvas,image=per_shape)
                perimeter_canvas.create_window(680,230,window=plabel)
                per_formula_label.configure(text="Formula: 4 x S")

                P_entry_box1_label.configure(text="S:")
                P_entry_box1_label.configure(font=("Lemonade Stand", 20))
                P_entry_box1.configure(state=NORMAL)
                P_entry_box2.configure(state=DISABLED)
                P_entry_box2_label.configure(text="                                                     ")
                P_entry_box2_label.configure(font=("Lemonade Stand", 35))
                P_entry_box3.configure(state=DISABLED)
                P_entry_box3_label.configure(text="                                                     ")
                P_entry_box3_label.configure(font=("Lemonade Stand", 35))
                per_button_calcul8.configure(state=NORMAL)

            elif (perimeter_combo.get()=="Rectangle"):
                per_shape_name = "rectangle"
                per_shape_label.configure(text="Rectangle")
                per_shape = PhotoImage(file='numbers/prect.png')
                plabel = Label(perimeter_canvas,image=per_shape)
                perimeter_canvas.create_window(680,230,window=plabel)
                per_formula_label.configure(text="Formula: 2l + 2w")

                P_entry_box1_label.configure(text="L:")
                P_entry_box1.configure(state=NORMAL)
                P_entry_box1_label.configure(font=("Lemonade Stand", 20))
                P_entry_box2_label.configure(text="W:")
                P_entry_box2.configure(state=NORMAL)
                P_entry_box3.configure(state=DISABLED)
                P_entry_box2_label.configure(font=("Lemonade Stand", 20))
                P_entry_box3_label.configure(text="                                                     ")
                P_entry_box3_label.configure(font=("Lemonade Stand", 35))
                per_button_calcul8.configure(state=NORMAL)

            elif (perimeter_combo.get()=="Circle"):
                per_shape_name = "circle"
                per_shape_label.configure(text="Circle")
                per_shape = PhotoImage(file='numbers/circle.png')
                plabel = Label(perimeter_canvas,image=per_shape)
                perimeter_canvas.create_window(680,245,window=plabel)
                per_formula_label.configure(text="Formula: 2πr")

                P_entry_box1_label.configure(text="r:")
                P_entry_box1.configure(state=NORMAL)
                P_entry_box1_label.configure(font=("Lemonade Stand", 20))
                P_entry_box2.configure(state=DISABLED)
                P_entry_box2_label.configure(text="                                                     ")
                P_entry_box2_label.configure(font=("Lemonade Stand", 35))
                P_entry_box3.configure(state=DISABLED)
                P_entry_box3_label.configure(text="                                                     ")
                P_entry_box3_label.configure(font=("Lemonade Stand", 35))
                per_button_calcul8.configure(state=NORMAL)

            elif (perimeter_combo.get() == "Select Shape"):
                per_button_calcul8.configure(state=DISABLED)
                per_formula_label.configure(text="Select a Shape!")
                P_entry_box1_label.configure(text="                                                     ")
                P_entry_box2_label.configure(text="                                                     ")
                P_entry_box3_label.configure(text="                                                     ")
                P_entry_box1_label.configure(font=("Lemonade Stand", 35))
                P_entry_box2_label.configure(font=("Lemonade Stand", 35))
                P_entry_box3_label.configure(font=("Lemonade Stand", 35))
                P_entry_box1.configure(state=DISABLED)
                P_entry_box2.configure(state=DISABLED)
                P_entry_box3.configure(state=DISABLED)


        perimeter_combo = ttk.Combobox(perimeter_window, font=("Lemonade Stand", 15), width=15, state="readonly")
        perimeter_combo['values'] = ("Select Shape", "Triangle", "Square", "Rectangle", "Circle")
        perimeter_combo.current(0)
        perimeter_canvas.create_text(140, 130, text="Select a shape:", font=("Lemonade Stand", 15))
        perimeter_combo.bind('<<ComboboxSelected>>', per_operation)
        perimeter_canvas.create_window(300, 130, window=perimeter_combo)

        per_shape_label = Label(perimeter_window,text=" Shape ", font=("Papaya sunrise",20))
        perimeter_canvas.create_window(590,110,window=per_shape_label)

        per_formula_label = Label(perimeter_window, text=" Select a Shape!!! ", font=("Quick Pencil", 30),bg="#ACD0C2")
        perimeter_canvas.create_window(230, 190, window=per_formula_label)

        perimeter_label = Label(perimeter_canvas, text="Perimeter:", font=("Lemonade Stand", 20),bg="#ACD0C2")
        perimeter_label_window = perimeter_canvas.create_window(140, 450, window=perimeter_label)
        perimeter_answer_label = Label(perimeter_canvas, text="   ", font=("Lemonade Stand", 20),bg="#ACD0C2")
        perimeter_answer_window = perimeter_canvas.create_window(260, 450, window=perimeter_answer_label)

        per_button_calcul8 = Button(perimeter_window, text="Calcul8", font=("Lemonade Stand", 10), bg="#f2cd2f", borderwidth=10, state=DISABLED, command=lambda : per_calculate(per_shape_name))
        perimeter_canvas.create_window(620, 430, window=per_button_calcul8)

        button_pclear = Button(perimeter_window, text="Clear", font=("Lemonade Stand", 10), bg="red", borderwidth=10,command=per_clear)
        perimeter_canvas.create_window(690, 430, window=button_pclear)

        P_entry_box1 = Entry(perimeter_window,font=("Lemonade Stand", 20), borderwidth=5, width=8)
        P_entry_box1_window = perimeter_canvas.create_window(270,240,window=P_entry_box1)
        P_entry_box1_label = Label(perimeter_window,font=("Lemonade Stand", 35),text="                                                     ",state=DISABLED,bg="#ACD0C2")
        P_entry_box1_label_wind = perimeter_canvas.create_window(150,240,window=P_entry_box1_label)

        P_entry_box2 = Entry(perimeter_window,font=("Lemonade Stand", 20), borderwidth=5, width=8)
        P_entry_box2_window = perimeter_canvas.create_window(270,295,window=P_entry_box2)
        P_entry_box2_label = Label(perimeter_window,font=("Lemonade Stand", 35),text="                                                     ",state=DISABLED,bg="#ACD0C2")
        P_entry_box2_label_wind = perimeter_canvas.create_window(150,295,window=P_entry_box2_label)

        P_entry_box3 = Entry(perimeter_window,font=("Lemonade Stand", 20), borderwidth=5, width=8)
        P_entry_box3_window = perimeter_canvas.create_window(270,360,window=P_entry_box3)
        P_entry_box3_label = Label(perimeter_window,font=("Lemonade Stand", 35),text="                                                     ",state=DISABLED,bg="#ACD0C2")
        P_entry_box3_label_wind = perimeter_canvas.create_window(150,360,window=P_entry_box3_label)
        counter +=1
    else:
        messagebox.showinfo("Error","A window is running")


def area():
    global counter
    counter = 1
    if counter < 5:
        area_window = Toplevel()
        area_window.title("Area")
        area_window.resizable(False,False)
        area_window.geometry('840x500')

        global area_image
        area_image = PhotoImage(file='numbers/areabg.png')
        area_canvas = Canvas(area_window, width=800, height=500)
        area_canvas.pack(fill='both', expand=True)
        area_canvas.create_image(0, 0, image=area_image, anchor=NW)
        area_canvas.create_text(750, 70, text="Area", font=("Lemonade Stand", 30))

        global shape_name
        global shape
        #global entry_box_1_window
        #global entry_box_1
        #global entrybox1_label
        #global entrybox1_label_window
        #global entry_box_2
        #global entry_box_2_window
        #global entrybox2_label
        #global entrybox2_label_window

        def clear():
            entry_box_1.delete(0,END)
            entry_box_2.delete(0,END)
            area_answer_label.configure(text= " ")
        def calculate(shape):
            valid = 0
            global shape_name
            if shape == "triangle":
                if entry_box_1.get() != " ":
                    try:
                        b = float(entry_box_1.get())
                        valid = 1
                    except ValueError as e:
                        messagebox.showinfo("Value Error","Input must be a number")
                        entry_box_1.delete(0,END)
                        entry_box_1.focus()
                if entry_box_1.get() != " " and valid == 1:
                    try:
                        h = float(entry_box_2.get())
                        valid = 2
                    except ValueError as e:
                        messagebox.showinfo("Value Error", "Input must be a number")
                        entry_box_2.delete(0, END)
                        entry_box_2.focus()
                if valid == 2:
                    a = (b * h) / 2
                    a = round(a,2)
                    area_answer_label.configure(text=a)

            if shape == "square":
                if entry_box_1.get() != " ":
                    try:
                        s = float(entry_box_1.get())
                        valid = 1
                    except ValueError as e:
                        messagebox.showinfo("Value Error","Input must be a number")
                        entry_box_1.delete(0,END)
                        entry_box_1.focus()
                    if valid == 1:
                        a = s * s
                        a = round(a, 2)
                        area_answer_label.configure(text=a)

            if shape == "rectangle":
                if entry_box_1.get() != " ":
                    try:
                        l = float(entry_box_1.get())
                        valid = 1
                    except ValueError as e:
                        messagebox.showinfo("Value Error","Input must be a number")
                        entry_box_1.delete(0,END)
                        entry_box_1.focus()
                    if entry_box_1.get() != " " and valid == 1:
                        try:
                            w = float(entry_box_2.get())
                            valid = 2
                        except ValueError as e:
                            messagebox.showinfo("Value Error", "Input must be a number")
                            entry_box_2.delete(0, END)
                            entry_box_2.focus()
                    if valid == 2:
                        a = l * w
                        a = round(a, 2)
                        area_answer_label.configure(text=a)

            if shape == "circle":
                if entry_box_1.get() != " ":
                    try:
                        r = float(entry_box_1.get())
                        valid=1
                    except ValueError as e:
                        messagebox.showinfo("Value Error", "Input must be a number")
                        entry_box_1.delete(0, END)
                        entry_box_1.focus()
                    if valid == 1:
                        a = 3.14 * (r * r)
                        a = round(a, 2)
                        area_answer_label.configure(text=a)
        def Operation(event):
            global shape_name
            global shape
            #global entry_box_1_window
            #global entry_box_1
            #global entrybox1_label
            #global entrybox1_label_window
            #global entry_box_2
            #global entry_box_2_window
            #global entrybox2_label
            #global entrybox2_label_window


            if (combo.get()=="Triangle"):
                shape_name = "triangle"
                shape_label.configure(text="Triangle")
                shape = PhotoImage(file='numbers/triangle.png')
                tlabel = Label(area_canvas,image=shape)
                area_canvas.create_window(230,230,window=tlabel)
                formula_label.configure(text="Formula: (1/2) (b x h)")

                #base
                entrybox1_label.configure(text="Base:")
                entry_box_1.configure(state=NORMAL)

                #height
                entrybox2_label.configure(text="Height")
                entry_box_2.configure(state=NORMAL)
                entrybox2_label_window = area_canvas.create_window(545, 350, window=entrybox2_label)
                button_calcul8.configure(state=NORMAL)

            elif (combo.get()=="Square"):
                shape_name = 'square'
                shape_label.configure(text="Square")
                shape = PhotoImage(file='numbers/square.png')
                tlabel = Label(area_canvas,image=shape)
                area_canvas.create_window(230, 230, window=tlabel)
                formula_label.configure(text="Formula: S²")

                entrybox1_label.configure(text="Side")
                entry_box_1.configure(state=NORMAL)
                entrybox2_label_window = area_canvas.create_window(630, 350, window=entrybox2_label)
                entrybox2_label.configure(text= " Square has equal Sides!!!")
                entry_box_2.configure(state=DISABLED)


            elif (combo.get()=="Rectangle"):
                shape_name = 'rectangle'
                area_canvas.delete("tlabel")
                shape_label.configure(text="Rectangle")
                shape = PhotoImage(file='numbers/rectangle.png')
                tlabel = Label(area_canvas,image=shape)
                area_canvas.create_window(230, 230, window=tlabel)
                formula_label.configure(text="Formula: l x w")

                #length
                entrybox1_label.configure(text="Length:")
                entry_box_1.configure(state=NORMAL)
                #hwight
                entrybox2_label.configure(text="Width")
                entrybox2_label_window = area_canvas.create_window(545, 350, window=entrybox2_label)
                entry_box_2.configure(state=NORMAL)

            elif (combo.get()=="Circle"):
                shape_name = "circle"
                area_canvas.delete("tlabel")
                shape_label.configure(text="Circle")
                shape = PhotoImage(file='numbers/circle.png')
                tlabel = Label(area_canvas,image=shape)
                area_canvas.create_window(230, 230, window=tlabel)
                formula_label.configure(text="Formula: πr²")

                entrybox1_label.configure(text="Radius:")
                entry_box_1.configure(state=NORMAL)
                entrybox2_label_window = area_canvas.create_window(640, 350, window=entrybox2_label)
                entrybox2_label.configure(text=" Circles are made of points!!!")
                entry_box_2.configure(state=DISABLED)
            elif (combo.get() == "Select Shape"):
                button_calcul8.configure(state=DISABLED)
                formula_label.configure(text="Select a Shape!")
                entrybox1_label.configure(text="")
                entrybox2_label.configure(text="")
                entry_box_1.configure(state=DISABLED)
                entry_box_2.configure(state=DISABLED)


        combo=ttk.Combobox(area_window,font=("Lemonade Stand", 15),width=15,state="readonly")
        combo['values']= ("Select Shape","Triangle", "Square", "Rectangle", "Circle")
        combo.current(0)
        area_canvas.create_text(570,130,text="Select a shape:",font=("Lemonade Stand", 15))
        combo.bind('<<ComboboxSelected>>', Operation)
        area_canvas.create_window(730,130,window=combo)

        shape_label = Label(area_window,text=" Shape ", font=("Papaya sunrise",20))
        area_canvas.create_window(550,180,window=shape_label)

        formula_label = Label(area_window,text="  ", font=("Quick Pencil",30))
        area_canvas.create_window(640, 230, window=formula_label)

        area_label = Label(area_canvas, text="Area:", font=("Lemonade Stand", 20))
        area_label_window = area_canvas.create_window(530, 410, window=area_label)
        area_answer_label = Label(area_canvas, text=" ", font=("Lemonade Stand", 20))
        area_label_window = area_canvas.create_window(630, 410, window=area_answer_label)

        button_calcul8 = Button(area_window,text="Calcul8",font=("Lemonade Stand", 10), bg="#f2cd2f",borderwidth=10,command=lambda :calculate(shape_name), state= DISABLED)
        area_canvas.create_window(530,460,window=button_calcul8)

        button_aclear = Button(area_window,text="Clear", font=("Lemonade Stand", 10), bg="red",borderwidth=10,command=clear)
        area_canvas.create_window(620, 460, window=button_aclear)


        entry_box_1 = Entry(area_window, font=("Lemonade Stand", 20), borderwidth=5, width=8)
        entry_box_1_window = area_canvas.create_window(650, 280, window=entry_box_1)
        entrybox1_label = Label(area_window, text=" Base: ", font=("Lemonade Stand", 20))
        entrybox1_label_window = area_canvas.create_window(550, 280, window=entrybox1_label)


        entry_box_2 = Entry(area_window, font=("Lemonade Stand", 20), borderwidth=5, width=8)
        entry_box_2_window = area_canvas.create_window(650, 350, window=entry_box_2)
        entrybox2_label = Label(area_window, text=" Height: ", font=("Lemonade Stand", 20))
        entrybox2_label_window = area_canvas.create_window(545, 350, window=entrybox2_label)
        counter +=1
    else:
        messagebox.showinfo("Error","A window is running")
        counter-=1



def quadratic():
    global counter
    counter = 1
    if counter < 5:
        quad_window = Toplevel()
        quad_window.title("Quadratic Equation")
        quad_window.resizable(False,False)
        quad_window.geometry('840x500')

        def solve_quad():
            valid = 0
            global label_denominatorqe
            global label_numeratorqe
            global label_xsub1
            global label_xsub2
            if entrybox_A.get() != " ":
                try:
                    a = int(entrybox_A.get())
                    valid = 1
                except Exception as e:
                    messagebox.showerror("ValueError", "Input must be a number")
                    entrybox_A.delete(0,END)
                    entrybox_A.focus()

            if entrybox_B.get() != " " and valid == 1:
                try:
                    b = int(entrybox_B.get())
                    valid = 2
                except Exception as e:
                    messagebox.showerror("ValueError", "Input must be a number")
                    entrybox_B.delete(0,END)
                    entrybox_B.focus()

            if entrybox_C.get() != " " and valid == 2:
                try:
                    c = int(entrybox_C.get())
                    valid = 3
                except Exception as e:
                    messagebox.showerror("ValueError", "Input must be a number")
                    entrybox_C.delete(0,END)
                    entrybox_C.focus()

            if valid == 3:
                b4ac = ((b**2) - (4*a*c))

                if b4ac > 0:
                    sqr = math.sqrt(b4ac)
                    z1 = (-b + sqr)/(2*a)
                    (z1.real)
                    z2 = (-b - sqr) / (2 * a)
                    (z2.real)
                else:
                    b4ac = b4ac*-1
                    sqr = math.sqrt(b4ac)*-1
                    z1 = (-b + complex(0,sqr))/(2*a)
                    (z1.imag)
                    z2 = (-b - complex(0, sqr)) / (2 * a)
                    (z2.imag)
                entrybox_A.delete(0,END)
                entrybox_B.delete(0, END)
                entrybox_C.delete(0, END)

                label_xsub1 = Label(quad_window,text="X1: {0:.3f}".format(z1), font=("Quick Pencil", 40))
                quadbg_canvas.create_window(300,350,window=label_xsub1)

                label_xsub2 = Label(quad_window, text="X2: {0:.3f}".format(z2), font=("Quick Pencil", 40))
                quadbg_canvas.create_window(300, 400, window=label_xsub2)

                label_line = Label(quad_window, text="____________", font=("Verdana", 30))
                quadbg_canvas.create_window(450, 260, window=label_line)

                label_numeratorqe = Label(quad_window, text=f" -{b}  ±  √({b}² -  4({a})({c}))", font=("Quick Pencil", 30))
                label_numeratorqe.lift(aboveThis=label_line)
                quadbg_canvas.create_window(450, 260, window=label_numeratorqe)


                label_denominatorqe = Label(quad_window, text=f" 2({a})", font=("Quick Pencil", 30))
                label_denominatorqe.lift(aboveThis=label_line)
                quadbg_canvas.create_window(450, 300, window=label_denominatorqe)

        def clear():
            global label_numeratorqe
            global label_denominatorqe
            entrybox_A.delete(0,END)
            entrybox_B.delete(0, END)
            entrybox_C.delete(0, END)
            label_numeratorqe.configure(text=" ")
            label_denominatorqe.configure(text=" ")
            label_xsub1.configure(text=" ")
            label_xsub2.configure(text=" ")

            label_line = Label(quad_window, text="____________", font=("Verdana", 30))
            quadbg_canvas.create_window(450, 260, window=label_line)

            label_denominatorqe = Label(quad_window, text=f" 2(a)", font=("Quick Pencil", 30))
            label_denominatorqe.lift(aboveThis=label_line)
            quadbg_canvas.create_window(450, 300, window=label_denominatorqe)

            label_numeratorqe = Label(quad_window, text=f" -b  ±  √(b² -  4(a)(c))", font=("Quick Pencil", 30))
            label_numeratorqe.lift(aboveThis=label_line)
            quadbg_canvas.create_window(450, 260, window=label_numeratorqe)

        global quad_bg

        quad_bg = PhotoImage(file='numbers/quadraticbg.png')
        quadbg_canvas = Canvas(quad_window, width=800, height=500)
        quadbg_canvas.pack(fill='both', expand=True)
        quadbg_canvas.create_image(0, 0, image = quad_bg, anchor=NW)
        quadbg_canvas.create_text(320, 100, text="Quadratic Equation", font=("Lemonade Stand", 30))

        entrybox_A = Entry(quad_window, borderwidth=5, width=3,font=("Quick Pencil", 30))
        quadbg_canvas.create_window(280,180, window=entrybox_A)

        label_xsqrd = Label(quad_window,text="x²  +  ",font=("Quick Pencil", 30))
        quadbg_canvas.create_window(360, 180, window=label_xsqrd)

        entrybox_B = Entry(quad_window, borderwidth=5, width=3,font=("Quick Pencil", 30))
        quadbg_canvas.create_window(435,180, window=entrybox_B)

        label_x = Label(quad_window, text="x  + ", font=("Quick Pencil", 30))
        quadbg_canvas.create_window(500, 180, window=label_x)

        entrybox_C = Entry(quad_window, borderwidth=5, width=3,font=("Quick Pencil", 30))
        quadbg_canvas.create_window(570,180, window=entrybox_C)



        button_calcul8 = Button(quad_window,text="Calcul8",font=("Lemonade Stand", 15), bg="#f2cd2f",borderwidth=10,command=solve_quad)
        quadbg_canvas.create_window(700,350,window=button_calcul8)

        button_clear = Button(quad_window,text="Clear", font=("Lemonade Stand", 15), bg="red",borderwidth=10,command=clear)
        quadbg_canvas.create_window(700, 430, window=button_clear)
        quadbg_canvas.create_text(200,260, text="X = ",font=("Quick Pencil",30))
        counter +=1
    else:
        messagebox.showinfo("Error", "A window is running")
        counter -=1


#bg image
bg_image = PhotoImage(file='numbers/backgroubd.png')
canvas = Canvas(window,width=800,height=500)
canvas.pack(fill='both', expand=True)
canvas.create_image(0,0, image=bg_image,anchor=NW)
canvas.create_text(320,150,text="Welcome to Calc-U-l8!",font=("Lemonade Stand",30))

#quad eq button
button_quadeq_img = PhotoImage(file='numbers/quadeq.png')
button_quadeq = Button(window,image=button_quadeq_img,border=0, command=quadratic)
button_quadeq_window = canvas.create_window(250,250,window=button_quadeq)
canvas.create_text(250,320,text="Quadratic Equation",font=("Lemonade Stand",12))

#area button
button_area_img = PhotoImage(file='numbers/area.png')
button_area = Button(window,image=button_area_img,border=0,command=area)
button_area_window = canvas.create_window(400,250,window=button_area)
canvas.create_text(400,320,text="Area of a Polygon",font=("Lemonade Stand",12))

#perimeter button
button_perimeter_img = PhotoImage(file='numbers/perimeter.png')
button_perimeter = Button(window,image=button_perimeter_img,border=0,height=100, bg="orange",command=perimeter)
button_perimeter_window = canvas.create_window(550,250,window=button_perimeter)
canvas.create_text(550,320,text="Perimeter of a Polygon",font=("Lemonade Stand",12))

#fibonacci button
button_fibonacci_img = PhotoImage(file='numbers/fibonacci.png')
button_fibonacci = Button(window,image=button_fibonacci_img,border=0)
button_fibonacci_window = canvas.create_window(320,400,window=button_fibonacci)
canvas.create_text(320,470,text="Fibonacci Sequence",font=("Lemonade Stand",12))

#arithmetic button
button_arithmetic_img = PhotoImage(file='numbers/arithmetic.png')
button_arithmetic = Button(window,image=button_arithmetic_img,border=0,command=arithmetic)
button_arithmetic_window = canvas.create_window(500,400,window=button_arithmetic)
canvas.create_text(500,470,text="Arithmetic Sequence",font=("Lemonade Stand",12))


window.mainloop()