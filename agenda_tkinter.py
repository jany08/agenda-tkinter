import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("650x400")

        # ----- FRAME PRINCIPAL -----
        frame_main = ttk.Frame(root, padding=10)
        frame_main.pack(fill="both", expand=True)

        # ----- FRAME PARA LISTA DE EVENTOS -----
        frame_lista = ttk.LabelFrame(frame_main, text="Eventos Programados", padding=10)
        frame_lista.pack(side="top", fill="both", expand=True, pady=10)

        columnas = ("Fecha", "Hora", "Descripción")
        self.tree = ttk.Treeview(frame_lista, columns=columnas, show="headings", height=8)
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # ----- FRAME PARA INGRESO DE DATOS -----
        frame_inputs = ttk.LabelFrame(frame_main, text="Nuevo Evento", padding=10)
        frame_inputs.pack(side="top", fill="x")

        # Fecha
        ttk.Label(frame_inputs, text="Fecha:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_fecha = DateEntry(frame_inputs, date_pattern="dd/mm/yyyy")
        self.entry_fecha.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Hora
        ttk.Label(frame_inputs, text="Hora:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_hora = tk.Entry(frame_inputs)
        self.entry_hora.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Descripción (con Entry en vez de Text para que no dé problemas)
        ttk.Label(frame_inputs, text="Descripción:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_desc = tk.Entry(frame_inputs, width=50)
        self.entry_desc.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # ----- FRAME PARA BOTONES -----
        frame_botones = ttk.Frame(frame_main, padding=10)
        frame_botones.pack(side="top", fill="x")

        ttk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Eliminar Seleccionado", command=self.eliminar_evento).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Salir", command=root.quit).pack(side="right", padx=5)

    def agregar_evento(self):
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()
        descripcion = self.entry_desc.get()

        if fecha and hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.entry_hora.delete(0, tk.END)
            self.entry_desc.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")

    def eliminar_evento(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Debe seleccionar un evento para eliminar")
            return
        confirmar = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar el evento seleccionado?")
        if confirmar:
            for item in seleccion:
                self.tree.delete(item)


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
