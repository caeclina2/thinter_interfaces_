import tkinter as tk
ventana = tk.Tk()
ventana.title("Mi primer ventana - CAECLINA")
ventana.geometry("600x400+0+0")
ventana.configure(bg="steel blue")
frame1 = tk.Frame(ventana)
frame1.configure(width=100, height=200, bg="red", bd=5)

frame2 = tk.Frame(frame1)
frame2.configure(width=100, height=100, bg="blue", bd=5)
frame1.pack()
frame2.pack()

boton=tk.Button(frame1, text="Caeclina")
boton.pack()

ventana.mainloop()
