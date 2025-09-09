NUM_NOTAS = 10
MIN_NOTA = 0
MAX_NOTA = 10
UMBRAL_APROBADO = 6  # Opcional, para mostrar aprobado/suspenso

# Se deja una línea en blanco para separar la configuración de la lógica principal.
notas = []

# Bucle principal para recolectar las notas.
for i in range(1, NUM_NOTAS + 1):
    # Este bucle interno se asegura de no avanzar hasta obtener una nota válida.
    while True:
        try:
            entrada = input(f"Ingrese la nota #{i} ({MIN_NOTA}-{MAX_NOTA}): ")
            nota = float(entrada)
            
            # Se añade un espacio alrededor de los operadores <= para mayor claridad.
            if MIN_NOTA <= nota <= MAX_NOTA:
                notas.append(nota)
                break  # Sale del bucle 'while' si la nota es válida.
            else:
                print(f"Error: la nota debe estar entre {MIN_NOTA} y {MAX_NOTA}.")
        
        except ValueError:
            print("Error: ingrese un número válido.")

# Se deja otra línea en blanco para separar la recolección del cálculo final.
promedio = sum(notas) / len(notas)
print(f"\nEl promedio de las notas es: {promedio:.2f}")

# (Opcional) Clasificación
if promedio >= UMBRAL_APROBADO:
    print("¡Aprobado!")
else:
    print("Suspenso.")
