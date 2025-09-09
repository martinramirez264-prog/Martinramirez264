# Definir cuántas notas vamos a pedir (reusing num_grades)
num_grades = 10

# Inicializar una lista vacía
notas = []

# Repetir 10 veces:
for i in range(num_grades): # reusing i
    while True:  # Loop para pedir la nota hasta que sea válida
        try:
            # a. Pedir al usuario la nota i
            entrada = input(f"Ingrese la nota #{i + 1} (0-10): ")

            # b. Intentar convertir la entrada a float (reusing nota)
            nota = float(entrada)

            # c. Validar que esté dentro del rango permitido (por defecto 0 ≤ nota ≤ 10)
            if 0 <= nota <= 10:
                # d. Si es válida, agregarla a notas
                notas.append(nota)
                break  # Salir del loop interior si la nota es válida
            else:
                # Si no, mostrar error y pedir de nuevo la misma nota
                print("Error: La nota debe estar entre 0 y 10.")
        except ValueError:
            # Si la conversión a float falla, mostrar error
            print("Error: Entrada no válida. Por favor, ingrese un número.")

# Una vez recolectadas las 10 notas, calcular la suma y dividir por la cantidad
promedio = sum(notas) / len(notas) # reusing promedio

# Mostrar el resultado con el formato deseado (p.ej. 2 decimales)
print(f"\nEl promedio de las {num_grades} notas es: {promedio:.2f}")

# (Opcional) Guardar resultados en un archivo o mostrar una clasificación
# Por ejemplo, mostrar una clasificación (aprobado/suspenso)
umbral_aprobado = 6.0  # Define el umbral para aprobar (reusing umbral_aprobado)

if promedio >= umbral_aprobado:
    print("Estado: Aprobado")
else:
    print("Estado: Suspenso")
