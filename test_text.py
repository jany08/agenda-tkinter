import tkinter as tk

root = tk.Tk()
root.title("Prueba Text")
root.geometry("400x200")

texto = tk.Text(root, width=40, height=5, relief="solid", borderwidth=1)
texto.pack(padx=20, pady=20)

root.mainloop()
