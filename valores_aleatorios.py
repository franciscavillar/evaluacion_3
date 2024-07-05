import globales
import random
import json

productos = [
"Café Americano",
"Té Chai",
"Croissant",
"Jugo Naranja",
"Panini de Pavo y Queso",
"Pastel de Zanahoria",
"Espresso Doble",
"Ba;do de Frutas",
"Muffin",
"Ensalada",
"Chocolate Caliente",
"Tarta de Frambuesa",
"Sándwich de Huevo",
"Galletas de Avena",
"Frappé de Caramelo"
]

def generar_valores_aleatorios():
    productos = []
    for producto in productos:
        productos = {
            "nombre": producto,
            "valor": random.randint(2000, 10000)
        },
      
        productos.append(productos)
    globales.guardar_archivo_json('valores.json', productos) 

if __name__ == "__main__":
    generar_valores_aleatorios()    




