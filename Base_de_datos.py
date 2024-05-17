import tkinter as tk
from tkinter import messagebox
import sqlite3

def conectar_bd():
    try:
        conn = sqlite3.connect('DATOSUSUARIOS.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS DATOSUSUARIO (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre_usuario VARCHAR(50),
                        contraseña VARCHAR(50),
                        apellido VARCHAR(10),
                        direccion VARCHAR(50),
                        comentarios VARCHAR(100)
                    )''')
        messagebox.showinfo("Éxito", "La base de datos se ha conectado correctamente.")
        return conn
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo conectar a la base de datos: {str(e)}")

# Función para limpiar los campos del formulario
def limpiar_campos():
    id_entry.delete(0, tk.END)
    nombre_entry.delete(0, tk.END)
    contraseña_entry.delete(0, tk.END)
    apellido_entry.delete(0, tk.END)
    direccion_entry.delete(0, tk.END)
    comentarios_entry.delete(0, tk.END)

# Funciones ABMC
def insertar_registro():
    nombre = nombre_entry.get()
    contraseña = contraseña_entry.get()
    apellido = apellido_entry.get()
    direccion = direccion_entry.get()
    comentarios = comentarios_entry.get()
    try:
        conn = conectar_bd()
        c = conn.cursor()
        c.execute("INSERT INTO DATOSUSUARIO (nombre_usuario, contraseña, apellido, direccion, comentarios) VALUES (?, ?, ?, ?, ?)",
                  (nombre, contraseña, apellido, direccion, comentarios))
        conn.commit()
        messagebox.showinfo("Éxito", "Registro insertado correctamente.")
        limpiar_campos()
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo insertar el registro: {str(e)}")

def consultar_registro():
    id_consulta = id_entry.get()
    try:
        conn = conectar_bd()
        c = conn.cursor()
        c.execute("SELECT * FROM DATOSUSUARIO WHERE ID=?", (id_consulta,))
        registro = c.fetchone()
        if registro:
            nombre_entry.delete(0, tk.END)
            nombre_entry.insert(0, registro[1])
            contraseña_entry.delete(0, tk.END)
            contraseña_entry.insert(0, registro[2])
            apellido_entry.delete(0, tk.END)
            apellido_entry.insert(0, registro[3])
            direccion_entry.delete(0, tk.END)
            direccion_entry.insert(0, registro[4])
            comentarios_entry.delete(0, tk.END)
            comentarios_entry.insert(0, registro[5])
        else:
            messagebox.showinfo("Información", "No se encontró ningún registro con ese ID.")
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo consultar el registro: {str(e)}")

def actualizar_registro():
    id_actualizar = id_entry.get()
    nombre = nombre_entry.get()
    contraseña = contraseña_entry.get()
    apellido = apellido_entry.get()
    direccion = direccion_entry.get()
    comentarios = comentarios_entry.get()
    try:
        conn = conectar_bd()
        c = conn.cursor()
        c.execute("UPDATE DATOSUSUARIO SET nombre_usuario=?, password=?, apellido=?, direccion=?, comentarios=? WHERE ID=?",
                  (nombre, contraseña, apellido, direccion, comentarios, id_actualizar))
        conn.commit()
        messagebox.showinfo("Éxito", "Registro actualizado correctamente.")
        limpiar_campos()
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo actualizar el registro: {str(e)}")

def borrar_registro():
    id_borrar = id_entry.get()
    try:
        conn = conectar_bd()
        c = conn.cursor()
        c.execute("DELETE FROM DATOSUSUARIO WHERE ID=?", (id_borrar,))
        conn.commit()
        messagebox.showinfo("Éxito", "Registro borrado correctamente.")
        limpiar_campos()
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo borrar el registro: {str(e)}")

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación ABMC")

# Crear widgets
menu_bar = tk.Menu(root)

bbdd_menu = tk.Menu(menu_bar, tearoff=0)
bbdd_menu.add_command(label="Conectar", command=conectar_bd)
bbdd_menu.add_separator()
bbdd_menu.add_command(label="Salir", command=root.quit)
menu_bar.add_cascade(label="BB.DD", menu=bbdd_menu)

borrar_menu = tk.Menu(menu_bar, tearoff=0)
borrar_menu.add_command(label="Borrar campos", command=limpiar_campos)
menu_bar.add_cascade(label="Borrar", menu=borrar_menu)

abmc_menu = tk.Menu(menu_bar, tearoff=0)
abmc_menu.add_command(label="Insertar", command=insertar_registro)
abmc_menu.add_command(label="Consultar", command=consultar_registro)
abmc_menu.add_command(label="Actualizar", command=actualizar_registro)
abmc_menu.add_command(label="Borrar", command=borrar_registro)
menu_bar.add_cascade(label="ABMC", menu=abmc_menu)

ayuda_menu = tk.Menu(menu_bar, tearoff=0)
ayuda_menu.add_command(label="Licencia", command=lambda: messagebox.showinfo("Licencia", "Registro en trámite"))
ayuda_menu.add_command(label="Acerca de", command=lambda: messagebox.showinfo("Acerca de", "El proyecto desarrollado en la materia Proyecto Integrador – Grupo 2 –Alejo Canton Pastrana, Ignacio Dibene, Damian Franceseschini y Valentino Jaime– E.E.S.T. Nº9 –La Plata"))
menu_bar.add_cascade(label="Ayuda", menu=ayuda_menu)

root.config(menu=menu_bar)

id_label = tk.Label(root, text="ID:")
id_label.grid(row=0, column=0, padx=5, pady=5)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, padx=5, pady=5)

nombre_label = tk.Label(root, text="Nombre:")
nombre_label.grid(row=1, column=0, padx=5, pady=5)
nombre_entry = tk.Entry(root)
nombre_entry.grid(row=1, column=1, padx=5, pady=5)

contraseña_label = tk.Label(root, text="Contraseña:")
contraseña_label.grid(row=2, column=0, padx=5, pady=5)
contraseña_entry = tk.Entry(root, show="*")
contraseña_entry.grid(row=2, column=1, padx=5, pady=5)

apellido_label = tk.Label(root, text="Apellido:")
apellido_label.grid(row=3, column=0, padx=5, pady=5)
apellido_entry = tk.Entry(root)
apellido_entry.grid(row=3, column=1, padx=5, pady=5)

direccion_label = tk.Label(root, text="Dirección:")
direccion_label.grid(row=4, column=0, padx=5,

 pady=5)
direccion_entry = tk.Entry(root)
direccion_entry.grid(row=4, column=1, padx=5, pady=5)

comentarios_label = tk.Label(root, text="Comentarios:")
comentarios_label.grid(row=5, column=0, padx=5, pady=5)
comentarios_entry = tk.Entry(root)
comentarios_entry.grid(row=5, column=1, padx=5, pady=5)

insertar_button = tk.Button(root, text="Insertar", command=insertar_registro)
insertar_button.grid(row=6, column=0, padx=5, pady=5)

consultar_button = tk.Button(root, text="Consultar", command=consultar_registro)
consultar_button.grid(row=6, column=1, padx=5, pady=5)

actualizar_button = tk.Button(root, text="Actualizar", command=actualizar_registro)
actualizar_button.grid(row=6, column=2, padx=5, pady=5)

borrar_button = tk.Button(root, text="Borrar", command=borrar_registro)
borrar_button.grid(row=6, column=3, padx=5, pady=5)

# Ejecutar la aplicación
root.mainloop()
