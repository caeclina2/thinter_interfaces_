import tkinter as tk
ventana = tk.Tk()
ventana.title("Mi primer ventana - CAECLINA")
ventana.geometry("600x400+0+0")
ventana.configure(bg="steel blue")

labelFrame = tk.LabelFrame(ventana, text="Grupo de Widgets", bg="yellow", padx=10, pady=10)
labelFrame.configure(width=100, height=200)
labelFrame.pack()
ventana.mainloop()