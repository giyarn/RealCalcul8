from tkinter import*
from PIL import ImageTk,Image
from math import*


window = Tk()
window.geometry('840x500')
window.resizable(False,False)

def quadratic():
    quad_window = Toplevel()
    quad_window.title("Quadratic Equation")
    quad_window.resizable(False,False)
    quad_window.geometry('840x500')

    def solve_quad():
        a = int(entrybox_A.get())
        b = int(entrybox_B.get())
        c = int(entrybox_C.get())
        b2_4ac = (b*b) - (4*a*c)
        total_1 = ((-b) + b2_4ac)/2*a
        total_2 = ((-b) - b2_4ac)/2*a
        entrybox_A.delete(0,END)
        entrybox_B.delete(0, END)

        label_total = Label(quad_window,text=f"({total_1},{total_2})", font=("Quick Pencil", 40))
        quadbg_canvas.create_window(430,300,window=label_total)

        #quadbg_canvas.create_text(400, 300, text=total, font=("Quick Pencil", 40))

    global quad_bg

    quad_bg = PhotoImage(file='numbers/quadraticbg.png')
    quadbg_canvas = Canvas(quad_window, width=800, height=500)
    quadbg_canvas.pack(fill='both', expand=True)
    quadbg_canvas.create_image(0, 0, image = quad_bg, anchor=NW)
    quadbg_canvas.create_text(320, 150, text="Quadratic Equation", font=("Lemonade Stand", 30))

    entrybox_A = Entry(quad_window, borderwidth=5, width=3,font=("Quick Pencil", 30))
    quadbg_canvas.create_window(310,250, window=entrybox_A)

    label_xsqrd = Label(quad_window,text="x²  +  ",font=("Quick Pencil", 30))
    quadbg_canvas.create_window(390, 250, window=label_xsqrd)

    entrybox_B = Entry(quad_window, borderwidth=5, width=3,font=("Quick Pencil", 30))
    quadbg_canvas.create_window(465,250, window=entrybox_B)

    label_x = Label(quad_window, text="x  + ", font=("Quick Pencil", 30))
    quadbg_canvas.create_window(530, 250, window=label_x)

    entrybox_C = Entry(quad_window, borderwidth=5, width=3,font=("Quick Pencil", 30))
    quadbg_canvas.create_window(600,250, window=entrybox_C)

    button_calcul8 = Button(quad_window,text="Calcul8",font=("Lemonade Stand", 15), bg="#f2cd2f",borderwidth=10,command=solve_quad)
    quadbg_canvas.create_window(700,400,window=button_calcul8)

    quadbg_canvas.create_text(300,300, text="X:",font=("Quick Pencil",40))



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
button_area = Button(window,image=button_area_img,border=0)
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