import os
import globales
import valores_aleatorios
import estadisticas

def menu_reportes():
    while True:
        os.system("cls")
        print("===== MENU =====")
        print("1. Asignar montos aleatorios")
        print("2. Ver estadísticas")
        print("3. Salir del programa")

        opcion = globales.seleccionar_opcion(3)

        if opcion == 1:
            os.system("cls")
            valores_aleatorios.generar_valores_aleatorios()
            print("Los montos aleatorios han sido asignados")
            input()
        elif opcion == 2:
            os.system("cls")    
            estadisticas.calcular_estadisticas()
            input()
        elif opcion == 3:
            print("Saliendo del programa . . .") 
            return

if __name__ == "__main__":
    menu_reportes()           