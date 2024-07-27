def obtener_letra(numero, alfabeto):
    if 0 <= numero < len(alfabeto):
        return alfabeto[numero]
    else:
        return "Número fuera de rango"    

def Encriptar_Cesar(mensaje):
    alfabeto = "QWERTYUIOPASDFGHJKLZXCVBNM"
    mensaje_encr = []
    mensaje = mensaje.upper()
    for i in mensaje: 
        if i in alfabeto:
            pos = alfabeto.index(i)
            nueva_pos = (pos + 3) % len(alfabeto)
            letras = obtener_letra(nueva_pos, alfabeto)
            mensaje_encr.append(letras)
        else:
            mensaje_encr.append(i)  
    return ''.join(mensaje_encr)

def Desencriptar_Cesar(mensaje):
    alfabeto = "QWERTYUIOPASDFGHJKLZXCVBNM"
    mensaje_desencr = []
    mensaje = mensaje.upper()
    for i in mensaje: 
        if i in alfabeto:
            pos = alfabeto.index(i)
            nueva_pos = (pos - 3) % len(alfabeto)
            letras = obtener_letra(nueva_pos, alfabeto)
            mensaje_desencr.append(letras)
        else:
            mensaje_desencr.append(i)
    return ''.join(mensaje_desencr)

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
            posiciones = Encriptar_Cesar(mensaje)
            print("Mensaje codificado: ", posiciones)

        elif opcion == '2':
            mensaje = input("Introducir el mensaje a desencriptar: ")
            posiciones = Desencriptar_Cesar(mensaje)
            print("Mensaje decodificado: ", posiciones)
            
        elif opcion == '3':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
