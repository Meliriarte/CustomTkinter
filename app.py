import customtkinter as ctk

class Contadordecaracteres:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300")
        self.root.title("Contador de caracteres")
        self.root.resizable(False, False)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        self.crear_interfaz()

    def crear_interfaz(self):
        self.etiqueta = ctk.CTkLabel(self.root, text="Ingrese un texto", font=("Helvetica", 20))
        self.etiqueta.pack(pady=10)

        self.entrada_texto = ctk.CTkTextbox(self.root, width=300, height=100, font =("Helvetica", 20))
        self.entrada_texto.pack(pady=10)

        self.boton_contar = ctk.CTkButton(self.root, text= "Contar caracteres", command=self.contar_caracteres, font=("Helvetica", 20))
        self.boton_contar.pack(pady=10)

        self.resultado = ctk.CTkLabel(self.root, text="", font=("Helvetica", 20))
        self.resultado.pack(pady=10)

    def contar_caracteres(self):
        texto = self.entrada_texto.get("1.0", "end-1c").strip()
        if texto:
            cantidad = len(texto)
            self.resultado.configure(text=f"El texto tiene {cantidad} caracteres")
        else:
            ctk.CTKMassageBox.showinfo("Error", "Por favor, ingrese un texto")

if __name__ == "__main__":
    root = ctk.CTk()
    app = Contadordecaracteres(root)
    root.mainloop()
