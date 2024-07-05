import globales
import json
import math

def calcular_estadisticas():
    productos = globales.leer_archivo_json('valores.json')
    if not productos:
        print("No hay valores registrados")
        return
    
productos = globales.leer_archivo_json('valores.json')    
producto = [producto('valores') for producto in productos]
#valor_mas_alto = max(productos)
valor_iva_mas_bajo = min(productos) * (0,19)
Promedio_valores = sum(productos) / len(productos)
media_geometrica = math.exp(sum(math.log(producto) for producto in productos) / len(productos))

print("===== ESTADISTICAS =====")
#print(f"VALOR MAS ALTO: {valor_mas_alto}")
print(f"VALOR IBA MAS BAJO: {valor_iva_mas_bajo}")
print(f"PROMEDIO VALORES: {Promedio_valores}")
print(f"MEDIA GEOMETRICA: {media_geometrica}")

if __name__ == "__main__":
    calcular_estadisticas()
