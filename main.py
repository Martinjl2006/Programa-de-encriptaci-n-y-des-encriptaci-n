import binascii
from PIL import Image
from skimage import io, filters
import numpy as np
import tkinter as tk
from tkinter import Toplevel, ttk, messagebox, filedialog


root = tk.Tk()
root.title("Desencriptacion y encriptacion con python")


label = tk.Label(root, text="Menu Principal", font= "minecraft")
label.pack()


style = ttk.Style()
style.theme_use('clam')





exit = tk.Button(root, text = 'Salir', 
                command = root.destroy,activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="red",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100) 



# Set the position of button on the top of window 
exit.pack(side ="bottom")


def texto_a_binario(texto):
    binario = ''.join(format(ord(char), '08b') for char in texto)
    return binario

# Convertir binario (unos y ceros) a texto
def binario_a_texto(binario):
    texto = ''.join(chr(int(binario[i:i+8], 2)) for i in range(0, len(binario), 8))
    return texto


def crear_imagen_binaria(binario,ancho):
    alto = len(binario) // ancho
    imagen = Image.new('1', (ancho, alto))  # '1' para imagen en blanco y negro
    pixeles = imagen.load()

    for i in range(alto):
        for j in range(ancho):
            if binario[i * ancho + j] == '1':
                pixeles[j, i] = 1  # Blanco
            else:
                pixeles[j, i] = 0  # Negro

    return imagen


def Decode():
    
    def obtener_nombre_y_ruta():
        global b, ruta, imgdc
        b = nombre_imagen.get()
        b = b + ".png"
        ruta = filedialog.askdirectory(title="Seleccione la carpeta que contiene la imagen")
        imgdc = f"{ruta}/{b}"
        
        try:
            imagen = io.imread(imgdc, as_gray=True)
            messagebox.showinfo("Éxito", f"Imagen cargada desde: {imgdc}")
            binaria = (imagen > 0.5).astype(np.uint8)
# Analizar la imagen píxel por píxel
            decode = ""
            for i in range(binaria.shape[0]):
                for j in range(binaria.shape[1]):
                    if binaria[i, j] == 1:  # Blanco
                            decode = decode + "1"
                    else:  # Negro
                            decode = decode + "0"
            binario =binario_a_texto(decode)
            print(f"decodificacion: {binario}")
            messagebox.showerror("Decodificacion", f"{binario}")
            # Aquí puedes añadir el código para procesar la imagen
        except FileNotFoundError:
            messagebox.showinfo("Error", "No se pudo cargar la imagen. Verifica la ruta y el nombre del archivo.")
        
        ventana_nombre.destroy()

    ventana_nombre = tk.Toplevel(root)
    ventana_nombre.title("Cargar Imagen")
    
    tk.Label(ventana_nombre, text="Ingrese el nombre de la imagen(sin la extension):").pack(pady=10)
    nombre_imagen = tk.Entry(ventana_nombre)
    nombre_imagen.pack(pady=10)
    
    tk.Button(ventana_nombre, text="Aceptar", command=obtener_nombre_y_ruta).pack(pady=10)


    


def Codificar(texto):
    a = texto
    print(a)
    if a != "":
        binario = texto_a_binario(a)
        print(f"Texto a binario: {binario}")
        return(binario)
    else:
        return("Error")


def mostrar_texto():
    
    abrir_nueva_ventana()
    


def Button_code(Texto):
    
    if Codificar(Texto) != "Error":
        b = ""
        alto = Codificar(Texto)
        ancho = 8  # Ancho de la imagen en píxeles
        imagen = crear_imagen_binaria(alto, ancho)
        def obtener_nombre_imagen():
            global b, ruta
            b = nombre_imagen.get()
            ruta = filedialog.askdirectory(title="Seleccione la carpeta para guardar la imagen")
            imgsv = f"{ruta}/{b}.png"
            imagen.save(imgsv, "PNG")
            messagebox.showinfo("Éxito", f"Imagen guardada en: {imgsv}")
            ventana_nombre.destroy()

        ventana_nombre = tk.Toplevel(root)
        ventana_nombre.title("Guardar Imagen")
        
        tk.Label(ventana_nombre, text="Ingrese el nombre de la imagen:").pack(pady=10)
        nombre_imagen = tk.Entry(ventana_nombre)
        nombre_imagen.pack(pady=10)
        
        tk.Button(ventana_nombre, text="Aceptar", command=obtener_nombre_imagen).pack(pady=10)
    else:
        messagebox.showerror("Ventana Emergente", "¡Ha ocurrido un error!")


# Función para mostrar el contenido del Entry

def abrir_nueva_ventana():
    nueva_ventana = Toplevel(root)
    nueva_ventana.title("Nueva Ventana")
    
    # Crear un campo de entrada de texto en la nueva ventana
    input_texto = tk.Entry(nueva_ventana)
    input_texto.pack(pady=10)
    
    # Función al presionar el botón de aceptar
    def aceptar():
        TextoCodificado = input_texto.get()
        print(TextoCodificado)
        Button_code(TextoCodificado)
        nueva_ventana.destroy()
    
    # Crear un botón de aceptar en la nueva ventana
    boton_aceptar = tk.Button(nueva_ventana, text="Aceptar", command=aceptar)
    boton_aceptar.pack(pady=10)

def NombreImagen():
    nueva_ventana2 = Toplevel(root)
    nueva_ventana2.title("Nombre de la imagen")
    nueva_ventana2.focus_set

    input_texto = tk.Entry(nueva_ventana2)
    input_texto.pack(pady=10)
    def aceptar():
        TextoCodificado = input_texto.get()
        print(TextoCodificado)
        return TextoCodificado
    
    boton_aceptar = tk.Button(nueva_ventana2, text="Aceptar", command=aceptar)
    boton_aceptar.pack(pady=10)



button = tk.Button(root, 
                   text="Encriptar", 
                   command=mostrar_texto,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

button2 = tk.Button(root, 
                   text="Desencriptar", 
                   command=Decode,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

button.pack(padx=20, pady=20)
button2.pack(padx=20, pady=20)

root.configure(background="#34495e")
root.mainloop()