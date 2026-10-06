def sumar(a, b):
    # Rompemos la función original cambiando el + por un -
    return a - b

def funcion_nueva(a, b):
    # Error intencional: división por cero
    return a / 0

if __name__ == "__main__":
    print(f"Resultado de la suma 2+3: {sumar(2, 3)}")
    