import tkinter as tk
from tkinter import ttk

def longitud():
    formulario_longitud = tk.Tk()
    formulario_longitud.title("Longitud Conversión")
    formulario_longitud.geometry("480x300")
    formulario_longitud.config(bg="#80B85B")

    tk.Label(formulario_longitud, text="Seleccione la conversión para longitud:", bg="#b2e3a9", font=("Times New Roman", 20), width=30, height=1).grid(row=0, column =0, padx=10, pady=10)
    opciones = ["Metros a Kilómetros", "Pulgadas a Metros"]

    combo = ttk.Combobox(formulario_longitud, values=opciones, state="readonly", width=30, height=1)
    combo.grid(row=1, column =0, padx=10, pady=5)

    tk.Label(formulario_longitud, text="Número:", bg="#b2e3a9", font=("Times New Roman", 15), width=15, height=1).grid(row=2, column =0, padx=10, pady=5)
    entrada = tk.Entry(formulario_longitud)
    entrada.grid(row=3, column =0, padx=10, pady=5)

    def conversión_longitud():
        try:
            num = float(entrada.get())
            elección = combo.get()
            if elección == "Metros a Kilómetros":
                conversion = num*0.001
                resultado.config(text=f"Resultado: {conversion:.3f} km.",fg="#900C3F")
            elif elección == "Pulgadas a Metros":
                conversion = num*0.0254
                resultado.config(text=f"Resultado: {conversion:.4f} m.",fg="#900C3F")
            else:
                resultado.config(text="Selecciona una opción de longitud.",fg="#900C3F")
        except ValueError:
            resultado.config(text="¡Error! Ingresa un número válido.", fg="red")

    boton_conversion = tk.Button(formulario_longitud,text="Convertir", command=conversión_longitud, bg="#2d723d", fg="White", font=("Times New Roman", 15), width=10, height=1)
    boton_conversion.grid(row=4, column =0, padx=10, pady=5)

    resultado = tk.Label(formulario_longitud, text="", bg="#b2e3a9", font=("Times New Roman", 12))
    resultado.grid(row=5, column =0, padx=10, pady=5)

    formulario_longitud.mainloop()

def masa():
    formulario_masa = tk.Tk()
    formulario_masa.title("Masa Conversión")
    formulario_masa.geometry("480x300")
    formulario_masa.config(bg="#80B85B")

    tk.Label(formulario_masa, text="Seleccione la conversión para masa:", bg="#b2e3a9", font=("Times New Roman", 20), width=30, height=1).grid(row=0, column =0, padx=10, pady=10)
    opciones = ["Kilogramos a Gramos", "Libras a Kilogramos"]

    combo = ttk.Combobox(formulario_masa, values=opciones, state="readonly", width=30, height=1)
    combo.grid(row=1, column =0, padx=10, pady=5)

    tk.Label(formulario_masa, text="Número:", bg="#b2e3a9", font=("Times New Roman", 15), width=15, height=1).grid(row=2, column =0, padx=10, pady=5)
    entrada = tk.Entry(formulario_masa)
    entrada.grid(row=3, column =0, padx=10, pady=5)

    def conversión_masa():
        try:
            num = float(entrada.get())
            elección = combo.get()
            if elección == "Kilogramos a Gramos":
                conversion = num*1000
                resultado.config(text=f"Resultado: {conversion:.2f} g.",fg="#900C3F")
            elif elección == "Libras a Kilogramos":
                conversion = num*0.4536
                resultado.config(text=f"Resultado: {conversion:.4f} kg.",fg="#900C3F")
            else:
                resultado.config(text="Selecciona una opción de masa.",fg="#900C3F")
        except ValueError:
            resultado.config(text="¡Error! Ingresa un número válido.", fg="red")

    boton_conversion = tk.Button(formulario_masa,text="Convertir", command=conversión_masa, bg="#2d723d", fg="White", font=("Times New Roman", 15), width=10, height=1)
    boton_conversion.grid(row=4, column =0, padx=10, pady=5)

    resultado = tk.Label(formulario_masa, text="", bg="#b2e3a9", font=("Times New Roman", 12))
    resultado.grid(row=5, column =0, padx=10, pady=5)

    formulario_masa.mainloop() 

def tiempo():
    formulario_tiempo = tk.Tk()
    formulario_tiempo.title("Tiempo Conversión")
    formulario_tiempo.geometry("480x300")
    formulario_tiempo.config(bg="#80B85B")

    tk.Label(formulario_tiempo, text="Seleccione la conversión para tiempo:", bg="#b2e3a9", font=("Times New Roman", 20), width=30, height=1).grid(row=0, column =0, padx=10, pady=10)
    opciones = ["Segundos a Minutos", "Horas a Días"]

    combo = ttk.Combobox(formulario_tiempo, values=opciones, state="readonly", width=30, height=1)
    combo.grid(row=1, column =0, padx=10, pady=5)

    tk.Label(formulario_tiempo, text="Número:", bg="#b2e3a9", font=("Times New Roman", 15), width=15, height=1).grid(row=2, column =0, padx=10, pady=5)
    entrada = tk.Entry(formulario_tiempo)
    entrada.grid(row=3, column =0, padx=10, pady=5)

    def conversión_tiempo():
        try:
            num = float(entrada.get())
            elección = combo.get()
            if elección == "Segundos a Minutos":
                conversion = num/60
                resultado.config(text=f"Resultado: {conversion:.2f} min.",fg="#900C3F")
            elif elección == "Horas a Días":
                conversion = num/24
                resultado.config(text=f"Resultado: {conversion:.2f} días.",fg="#900C3F")
            else:
                resultado.config(text="Selecciona una opción de tiempo.",fg="#900C3F")
        except ValueError:
            resultado.config(text="¡Error! Ingresa un número válido.", fg="red")

    boton_conversion = tk.Button(formulario_tiempo,text="Convertir", command=conversión_tiempo, bg="#2d723d", fg="White", font=("Times New Roman", 15), width=10, height=1)
    boton_conversion.grid(row=4, column =0, padx=10, pady=5)

    resultado = tk.Label(formulario_tiempo, text="", bg="#b2e3a9", font=("Times New Roman", 12))
    resultado.grid(row=5, column =0, padx=10, pady=5)

    formulario_tiempo.mainloop()  

#ventana principal
ventana = tk.Tk()
ventana.title("Conversiones") 
ventana.config(bg="#80B85B")
ventana.geometry("300x300")

tk.Label(ventana, text = "Elija una Opción:", bg="#b2e3a9", font=("Times New Roman", 25), width=15, height=1).grid(row=0, column=0, padx=10, pady=5)

boton_longitud = tk.Button(ventana,text="Longitud", command=longitud, bg="#2d723d", fg="White", font=("Times New Roman", 20), width=15, height=1)
boton_longitud.grid(row=1, column =0, padx=10, pady=5)

boton_masa = tk.Button(ventana,text="Masa", command=masa, bg="#2d723d", fg="White", font=("Times New Roman", 20), width=15, height=1)
boton_masa.grid(row=2, column =0, padx=10, pady=5)

boton_tiempo = tk.Button(ventana,text="Tiempo", command=tiempo, bg="#2d723d", fg="White", font=("Times New Roman", 20), width=15, height=1)
boton_tiempo.grid(row=3, column =0, padx=10, pady=5)

ventana.mainloop()