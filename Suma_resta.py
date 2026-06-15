import tkinter as tk

def suma():
    try:
        n1 = int(numero1.get())
        n2 = int(numero2.get())
        res = n1 + n2
        resultado.config(text=f"Resultado: {res}")

    except:
        resultado.config(text="Ingresa solo numeros enteros")


#Crear Formulario
formulario = tk.Tk()
formulario.title("Suma De dos Numeros")
formulario.geometry("550x300")
numero1 = tk.StringVar()
numero2 = tk.StringVar()

tk.Label(formulario, text="Numero1:").pack(pady=10)
tk.Entry(formulario, textvariable=numero1, width=50).pack(pady=5)

tk.Label(formulario, text="Numero2:").pack(pady=10)
tk.Entry(formulario, textvariable=numero2, width=50).pack(pady=5)

tk.Button(formulario, text="Suma",command=suma, bg="red",fg="white").pack(pady=20)

resultado = tk.Label(formulario,  text="Resultado: ")
resultado.pack(pady=20)

#Inicio de ventana 
formulario.mainloop()