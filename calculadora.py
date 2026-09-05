"""
Calculadora básica en Python.

Permite realizar las cuatro operaciones aritméticas fundamentales:
suma, resta, multiplicación y división.
"""


def sumar(a: float, b: float) -> float:
    """Devuelve la suma de dos números."""
    return a + b


def restar(a: float, b: float) -> float:
    """Devuelve la resta de dos números."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Devuelve la multiplicación de dos números."""
    return a * b


def dividir(a: float, b: float) -> float:
    """Devuelve la división de dos números.

    Lanza ValueError si se intenta dividir entre cero.
    """
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


OPERACIONES = {
    "1": ("Sumar", sumar),
    "2": ("Restar", restar),
    "3": ("Multiplicar", multiplicar),
    "4": ("Dividir", dividir),
}


def pedir_numero(mensaje: str) -> float:
    """Solicita al usuario un número por consola y lo valida."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Por favor ingresa un número.")


def mostrar_menu() -> None:
    """Muestra el menú de opciones disponibles."""
    print("\n--- Calculadora Básica ---")
    for clave, (nombre, _) in OPERACIONES.items():
        print(f"{clave}. {nombre}")
    print("5. Salir")


def main() -> None:
    """Bucle principal del programa."""
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "5":
            print("¡Hasta luego!")
            break

        if opcion not in OPERACIONES:
            print("Opción no válida, intenta de nuevo.")
            continue

        nombre, operacion = OPERACIONES[opcion]
        a = pedir_numero("Ingresa el primer número: ")
        b = pedir_numero("Ingresa el segundo número: ")

        try:
            resultado = operacion(a, b)
            print(f"Resultado de {nombre.lower()}: {resultado}")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
