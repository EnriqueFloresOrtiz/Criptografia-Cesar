def Encriptador_Cesar(mensaje):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    posiciones = []
    mensaje = mensaje.upper()
    mensaje = mensaje.replace(" ", "")
    for i in mensaje:
        alfabeto_pos = alfabeto.index(i)
        posiciones.append(alfabeto_pos)
    return posiciones


def Desencriptador_Cesar(posiciones):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mensaje = ""
    for i in posiciones:
        if 0 <= i < len(alfabeto):
            mensaje += alfabeto[i]
    return mensaje

def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Encriptar mensaje")
    print("2. Desencriptar mensaje")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1, 2, 3): ")

        if opcion == '1':
            mensaje = input("Introducir el mensaje a encriptar: ")
            posiciones = Encriptador_Cesar(mensaje)
            print("Mensaje codificado: ", posiciones)

        elif opcion == '2':
            arreglo = []
            print("Ingrese las posiciones (una por una) y escriba 'salir' para terminar:")
            while True:
                valor = input()
                if valor.lower() == 'salir':
                    break
                try:
                    arreglo.append(int(valor))
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            mensaje_des = Desencriptador_Cesar(arreglo)
            print("Mensaje decodificado: ", mensaje_des)

        elif opcion == '3':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
