import tkinter as tk
ventana = tk.Tk()
ventana.title("Mi primer ventana - CAECLINA")
ventana.geometry("600x400+0+0")
ventana.minsize(400,200)
ventana.maxsize(800,600)
ventana.iconbitmap("robot02.ico")
ventana.configure(bg="steel blue")
ventana.attributes("-alpha",0.9)


ventana.mainloop()
