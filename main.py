from tkinter import*
from PIL import ImageTk,Image
from math import*
from tkinter import messagebox
from tkinter import ttk

window = Tk()
window.geometry('840x500')
window.resizable(False,False)
window.wm_attributes('-transparentcolor', '#ab23ff')

def area():
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
    global entry_box_1_window
    global entry_box_1
    global entrybox1_label
    global entrybox1_label_window
    global entry_box_2
    global entry_box_2_window
    global entrybox2_label
    global entrybox2_label_window

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
                    area_answer_label.configure(text=a)
    def Operation(event):
        global shape_name
        global shape
        global entry_box_1_window
        global entry_box_1
        global entrybox1_label
        global entrybox1_label_window
        global entry_box_2
        global entry_box_2_window
        global entrybox2_label
        global entrybox2_label_window


        if (combo.get()=="Triangle"):
            shape_name = "triangle"
            shape_label.configure(text="Triangle")
            shape = PhotoImage(file='numbers/triangle.png')
            tlabel = Label(area_canvas,image=shape)
            area_canvas.create_window(230,230,window=tlabel)
            formula_label.configure(text="Formula: (1/2) (b x h)")

            #base
            entrybox1_label.configure(text="Base:")

            #height
            entrybox2_label.configure(text="Height")
            entry_box_2.configure(state=NORMAL)

        elif (combo.get()=="Square"):
            shape_name = 'square'
            shape_label.configure(text="Square")
            shape = PhotoImage(file='numbers/square.png')
            tlabel = Label(area_canvas,image=shape)
            area_canvas.create_window(230, 230, window=tlabel)
            formula_label.configure(text="Formula: S²")

            entrybox1_label.configure(text="Side")
            entrybox2_label.configure(text= " Square has equal Sides!!!           ")
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

            #hwight
            entrybox2_label.configure(text="Width")
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
            entrybox2_label.configure(text=" Circles are made of points!!!           ")
            entry_box_2.configure(state=DISABLED)






    combo=ttk.Combobox(area_window,font=("Lemonade Stand", 15),width=15,state="readonly")
    combo['values']= ("Triangle", "Square", "Rectangle", "Circle")
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

    button_calcul8 = Button(area_window,text="Calcul8",font=("Lemonade Stand", 10), bg="#f2cd2f",borderwidth=10,command=lambda :calculate(shape_name))
    area_canvas.create_window(530,460,window=button_calcul8)

    button_clear = Button(area_window,text="Clear", font=("Lemonade Stand", 10), bg="red",borderwidth=10,command=clear)
    area_canvas.create_window(620, 460, window=button_clear)


    entry_box_1 = Entry(area_window, font=("Lemonade Stand", 20), borderwidth=5, width=8)
    entry_box_1_window = area_canvas.create_window(650, 280, window=entry_box_1)
    entrybox1_label = Label(area_window, text=" Base: ", font=("Lemonade Stand", 20))
    entrybox1_label_window = area_canvas.create_window(550, 280, window=entrybox1_label)


    entry_box_2 = Entry(area_window, font=("Lemonade Stand", 20), borderwidth=5, width=8)
    entry_box_2_window = area_canvas.create_window(650, 350, window=entry_box_2)
    entrybox2_label = Label(area_window, text=" Height: ", font=("Lemonade Stand", 20))
    entrybox2_label_window = area_canvas.create_window(545, 350, window=entrybox2_label)




def quadratic():
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
            total_1 = ((b*b)+(4*a*c))**0.5/2*a
            total_1 = abs(total_1)
            total_2 = ((b*b)-(4*a*c))**0.5/2*a
            total_2 = abs(total_2)
            entrybox_A.delete(0,END)
            entrybox_B.delete(0, END)
            entrybox_C.delete(0, END)

            label_xsub1 = Label(quad_window,text=f"x₁ = {total_1}", font=("Quick Pencil", 40))
            quadbg_canvas.create_window(280,350,window=label_xsub1)

            label_xsub2 = Label(quad_window, text=f"x₂ = {total_2}", font=("Quick Pencil", 40))
            quadbg_canvas.create_window(280, 400, window=label_xsub2)

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
button_perimeter = Button(window,image=button_perimeter_img,border=0,height=100, bg="orange")
button_perimeter_window = canvas.create_window(550,250,window=button_perimeter)
canvas.create_text(550,320,text="Perimeter of a Polygon",font=("Lemonade Stand",12))

#fibonacci button
button_fibonacci_img = PhotoImage(file='numbers/fibonacci.png')
button_fibonacci = Button(window,image=button_fibonacci_img,border=0)
button_fibonacci_window = canvas.create_window(320,400,window=button_fibonacci)
canvas.create_text(320,470,text="Fibonacci Sequence",font=("Lemonade Stand",12))

#arithmetic button
button_arithmetic_img = PhotoImage(file='numbers/arithmetic.png')
button_arithmetic = Button(window,image=button_arithmetic_img,border=0)
button_arithmetic_window = canvas.create_window(500,400,window=button_arithmetic)
canvas.create_text(500,470,text="Arithmetic Sequence",font=("Lemonade Stand",12))


window.mainloop()