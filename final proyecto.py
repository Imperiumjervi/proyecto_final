from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import os
import csv
import pandas as pd


def crear_archivo_csv():
    if not os.path.isfile('CLIENTES.csv'):
        with open('CLIENTES.csv', 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(['Nombre', 'Fecha Natal', 'Identificacion'])

def guardar_datos(name, date, id):
    if name == '' or date == '' or id == '':
        messagebox.showerror('Error', 'Debe llenar todas las casillas')
        return
    
    try:
        fecha_natal_formateada = datetime.strptime(date, '%d/%m/%Y').strftime('%Y-%m-%d')
    except ValueError:
        messagebox.showerror("Error", "Fecha inválida. Use el formato DD/MM/YYYY.")
        return

    # Check if ID already exists
    if os.path.isfile('CLIENTES.csv'):
        with open('CLIENTES.csv', 'r', newline='') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            next(lector_csv)  # Skip header
            for fila in lector_csv:
                if fila[2] == id:
                    messagebox.showerror('Error', 'La identificación ya existe.')
                    return

    # Save data to CSV
    with open('CLIENTES.csv', 'a', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow([name, fecha_natal_formateada, id])

    messagebox.showinfo('Éxito', 'Datos guardados exitosamente.')
    limpiar_entradas()

def limpiar_entradas():
    entrada_nombre.delete(0, END)
    entrada_F_N.delete(0, END)
    entrada_ID.delete(0, END)

CLIENTES = Tk()
CLIENTES.title('Registro de Clientes')
CLIENTES.geometry('500x300')

Label(CLIENTES, text="Nombre: ").pack(pady=10)
entrada_nombre = Entry(CLIENTES, width=40)
entrada_nombre.pack(pady=5)

Label(CLIENTES, text="Fecha de Nacimiento (DD/MM/YYYY): ").pack(pady=10)
entrada_F_N = Entry(CLIENTES, width=40)
entrada_F_N.pack(pady=5)

Label(CLIENTES, text="Identificación: ").pack(pady=10)
entrada_ID = Entry(CLIENTES, width=40)
entrada_ID.pack(pady=5)

boton_guardar = Button(CLIENTES, text="Guardar Datos", command=lambda: guardar_datos(entrada_nombre.get(), entrada_F_N.get(), entrada_ID.get()))
boton_guardar.pack(pady=10)

etiqueta_resultado = Label(CLIENTES, text="")
etiqueta_resultado.pack(pady=10)

crear_archivo_csv()

CLIENTES.mainloop()
