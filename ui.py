def pedir_departamento():
    nombre_departamento = input(
        "Ingrese el departamento: "
    ).strip().upper()

    return nombre_departamento


def pedir_limite_registros():
    while True:
        try:
            limite_registros = int(
                input("Ingrese la cantidad de registros: ")
            )

            if limite_registros > 0:
                return limite_registros

            print("La cantidad debe ser mayor que 0.")

        except ValueError:
            print("Por favor, ingrese un número entero.")