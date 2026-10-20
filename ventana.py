import math
import operaciones as op
import tkinter as tk
from tkinter import ttk, messagebox


class CalculadoraOperaciones(ttk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana, padding=20)
        self.pack(fill="both", expand=True)

       
        self.columnconfigure(1, weight=1)

     
        self.num1 = tk.StringVar(master=self)
        self.num2 = tk.StringVar(master=self)
        self.resultado = tk.StringVar(master=self, value="Resultado: Sin calcular")

       
        self.crear_widgets()

    def crear_widgets(self):
        
        ttk.Label(self, text="Número 1:").grid(row=0, column=0, sticky="w", pady=5)
        self.campo_num1 = ttk.Entry(self, textvariable=self.num1)
        self.campo_num1.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        ttk.Label(self, text="Número 2:").grid(row=1, column=0, sticky="w", pady=5)
        ttk.Entry(self, textvariable=self.num2).grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        
        panel_operaciones = ttk.LabelFrame(self, text="Operaciones", padding=10)
        panel_operaciones.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")

       
        for col in range(4):
            panel_operaciones.columnconfigure(col, weight=1)

        ttk.Button(panel_operaciones, text="+ Sumar", command=lambda: self.operar("+")).grid(row=0, column=0, padx=3)
        ttk.Button(panel_operaciones, text="- Restar", command=lambda: self.operar("-")).grid(row=0, column=1, padx=3)
        ttk.Button(panel_operaciones, text="× Multiplicar", command=lambda: self.operar("*")).grid(row=0, column=2, padx=3)
        ttk.Button(panel_operaciones, text="÷ Dividir", command=lambda: self.operar("/")).grid(row=0, column=3, padx=3)

       
        panel_utilidades = ttk.Frame(self)
        panel_utilidades.grid(row=3, column=0, columnspan=2, pady=5)

        ttk.Button(panel_utilidades, text="Limpiar", command=self.limpiar).pack(side="left", padx=5)
        ttk.Button(panel_utilidades, text="Salir", command=self.master.destroy).pack(side="left", padx=5)

        
        lbl_resultado = ttk.Label(self, textvariable=self.resultado, font=("Arial", 11, "bold"))
        lbl_resultado.grid(row=4, column=0, columnspan=2, pady=15)

       
        self.campo_num1.focus_set()

    def obtener_numeros(self):
       
        txt1 = self.num1.get().strip().replace(",", ".")
        txt2 = self.num2.get().strip().replace(",", ".")

        if not txt1 or not txt2:
            messagebox.showwarning("Campos vacíos", "Por favor ingresa ambos números.")
            return None

        try:
            val1 = float(txt1)
            val2 = float(txt2)

            if not (math.isfinite(val1) and math.isfinite(val2)):
                raise ValueError

            return val1, val2

        except ValueError:
            messagebox.showerror("Entrada inválida", "Ingresa números válidos y finitos.")
            return None

    def operar(self, operacion):
        val = self.obtener_numeros()
        if val is None:
            return

        a, b = val

        try:
            if operacion == "+":
                res = sumar(a, b)
                simbolo = "+"
            elif operacion == "-":
                res = restar(a, b)
                simbolo = "-"
            elif operacion == "*":
                res = multiplicar(a, b)
                simbolo = "×"
            elif operacion == "/":
                res = dividir(a, b)
                simbolo = "÷"

           
            res_formateado = f"{res:.2f}".rstrip('0').rstrip('.') if isinstance(res, float) else f"{res}"
            self.resultado.set(f"{a} {simbolo} {b} = {res_formateado}")

        except ZeroDivisionError as err:
            messagebox.showerror("Error de división", str(err))
            self.resultado.set("Resultado: Error (División por cero)")

    def limpiar(self):
        """Restablece los campos de entrada."""
        self.num1.set("")
        self.num2.set("")
        self.resultado.set("Resultado: Sin calcular")
        self.campo_num1.focus_set()


if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Calculadora Básica")
    ventana.minsize(420, 260)
    app = CalculadoraOperaciones(ventana)
    ventana.mainloop()