def calcular_promedio_con_clasificacion():
    """
    Calcula el promedio de 10 notas, valida el rango de 0 a 10 y
    determina si el resultado es aprobado o desaprobado.
    """
    num_notas = 10
    notas = []
    umbral_aprobacion = 6.0  # Umbral configurable para aprobar

    print(f"Por favor, ingrese {num_notas} notas para calcular el promedio.")
    print(f"El umbral de aprobación es {umbral_aprobacion}.\n")

    # Bucle para solicitar y validar las 10 notas
    while len(notas) < num_notas:
        try:
            entrada = input(f"Ingrese la nota #{len(notas) + 1} (0-10): ")
            nota = float(entrada)

            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print(" Error: La nota debe estar entre 0 y 10. Intente de nuevo.")
        except ValueError:
            print(" Error: Entrada no válida. Por favor, ingrese un número.")

    # Una vez que se tienen las 10 notas, se calcula el promedio
    if notas:
        promedio = sum(notas) / len(notas)
        
        # Muestra el resultado y la clasificación
        print("\n--- Resultado ---")
        print(f"El promedio de las {num_notas} notas es: {promedio:.2f}")

        if promedio >= umbral_aprobacion:
            print(" ¡Felicitaciones! Ha APROBADO.")
        else:
            print(" Lo siento, ha DESAPROBADO.")
    else:
        print("\nNo se pudieron ingresar notas válidas. No se puede calcular el promedio.")

# Llama a la función principal para ejecutar el programa
if __name__ == "__main__":
    calcular_promedio_con_clasificacion()
