from tkinter import*
from PIL import ImageTk,Image


window = Tk()
window.geometry('840x500')
window.resizable(False,False)

#bg image
bg_image = PhotoImage(file='numbers/backgroubd.png')
canvas = Canvas(window,width=800,height=500)
canvas.pack(fill='both', expand=True)
canvas.create_image(0,0, image=bg_image,anchor=NW)
canvas.create_text(320,150,text="Welcome to Calc-U-l8!",font=("Lemonade Stand",30))

#quad eq button
button_quadeq_img = PhotoImage(file='numbers/quadeq.png')
button_quadeq = Button(window,image=button_quadeq_img,border=0)
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










window.mainloop()